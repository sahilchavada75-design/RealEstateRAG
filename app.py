
import streamlit as st
import chromadb
from sentence_transformers import SentenceTransformer
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import re
import html

load_dotenv()

st.set_page_config(
    page_title="Real Estate AI Assistant",
    page_icon="🏠",
    layout="wide"
)

# Custom UI design
st.markdown("""
<style>
.stApp {
    background-color: #f4f7fb;
}
.main-title {
    font-size: 36px;
    font-weight: 800;
    color: #17365d;
    text-align: center;
}
.sub-title {
    color: #64748b;
    text-align: center;
    font-size: 17px;
}
.property-card {
    background: white;
    padding: 20px;
    border-radius: 14px;
    border: 1px solid #e2e8f0;
    margin-bottom: 15px;
}
.price {
    color: #087e65;
    font-size: 23px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="main-title">🏠 Real Estate AI Assistant</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="sub-title">Find your perfect property using AI-powered search</div>',
    unsafe_allow_html=True
)

st.write("")

# Load Sentence Transformer model
@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()

# ChromaDB connection
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_collection(
    name="real_estate_properties"
)

# Gemini connection
client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY"),
    http_options=types.HttpOptions(timeout=20000)
)

# Extract complete property details
def parse_property(doc):
    data = {}

    pattern = (
        r'(Title|Type|Locality|Bedrooms|Price|Area|Amenities|Description):\s*'
        r'(.*?)(?=,\s*(?:Title|Type|Locality|Bedrooms|Price|Area|Amenities|Description):|$)'
    )

    matches = re.findall(pattern, doc)

    for key, value in matches:
        data[key] = value.strip()

    return data


# Filter properties according to user requirements
def filter_properties(properties, question):

    q = question.lower()
    filtered = []

    bedroom_match = re.search(r'(\d+)\s*bhk', q)

    city = None
    if "ahmedabad" in q:
        city = "ahmedabad"
    elif "gandhinagar" in q:
        city = "gandhinagar"

    property_type = None
    if "villa" in q:
        property_type = "villa"
    elif "plot" in q:
        property_type = "plot"
    elif "flat" in q or "apartment" in q:
        property_type = "apartment"

    amenity_keywords = [
        "parking", "lift", "gym", "garden",
        "pool", "swimming pool", "road", "water"
    ]

    requested_amenities = [
        word for word in amenity_keywords if word in q
    ]

    for item in properties:

        data = item["data"]

        # Bedroom filter
        if bedroom_match:
            if data.get("Bedrooms", "").strip() != bedroom_match.group(1):
                continue

        # City filter
        if city:
            if data.get("Locality", "").lower() != city:
                continue

        # Property type filter
        if property_type:
            actual_type = data.get("Type", "").lower()
            title = data.get("Title", "").lower()

            if property_type not in actual_type and property_type not in title:
                continue

        # Amenities filter
        amenities_text = (
            data.get("Amenities", "") + " " +
            data.get("Description", "")
        ).lower()

        if requested_amenities:
            if not all(
                amenity in amenities_text
                for amenity in requested_amenities
            ):
                continue

        filtered.append(item)

    return filtered


st.markdown("### 🔍 Search Properties")

question = st.text_input(
    "Enter your requirement",
    placeholder="Example: Find a 2 BHK flat in Ahmedabad"
)

if st.button("Search Properties 🔎", type="primary"):

    if question.strip():

        with st.spinner("Finding suitable properties..."):

            try:
                query_embedding = model.encode(question).tolist()

                results = collection.query(
                    query_embeddings=[query_embedding],
                    n_results=collection.count()
                )

                documents = results["documents"][0]

                # Parse all retrieved properties
                properties = []

                for doc in documents:
                    properties.append({
                        "document": doc,
                        "data": parse_property(doc)
                    })

                # Apply exact filters
                filtered = filter_properties(properties, question)

            except Exception as e:
                st.error(f"Search error: {e}")
                filtered = []

        st.write("")

        if filtered:

            property_info = "\n".join(
                item["document"] for item in filtered
            )

            prompt = f"""
You are a real estate assistant.
Answer the user in simple language using only the property data.
Do not invent any details.

Property data:
{property_info}

Question:
{question}
"""

            st.markdown("### 🤖 AI Answer")

            try:
                with st.spinner("AI is preparing your answer..."):

                    response = client.models.generate_content(
                        model="gemini-3.8-flash",
                        contents=prompt
                    )

                if response.text:
                    st.success(response.text)
                else:
                    st.info("AI could not generate an answer.")

            except Exception:
                st.info(
                    "Gemini is temporarily unavailable. "
                    "Showing results in backup mode."
                )

            st.markdown("### 🏡 Matching Properties")

            st.write(f"Found {len(filtered)} matching properties.")

            for item in filtered:

                data = item["data"]

                title = html.escape(data.get("Title", "Property"))
                price = html.escape(data.get("Price", "Not available"))
                locality = html.escape(data.get("Locality", "Not available"))
                bedrooms = html.escape(data.get("Bedrooms", "Not available"))
                area = html.escape(data.get("Area", "Not available"))
                amenities = html.escape(data.get("Amenities", "Not available"))
                description = html.escape(data.get("Description", ""))

                st.markdown(f"""
                <div class="property-card">
                    <h3>{title}</h3>
                    <div class="price">₹ {price}</div>
                    <p>📍 {locality}</p>
                    <p>🛏️ {bedrooms} Bedrooms &nbsp; | &nbsp; 📐 {area}</p>
                    <p>✨ {amenities}</p>
                    <p>{description}</p>
                </div>
                """, unsafe_allow_html=True)

        else:
            st.warning(
                "No matching properties found. "
                "Please try another search."
            )

    else:
        st.warning("Please enter your requirement.")

st.divider()
st.caption(
    "Real Estate Assistant Using RAG | MySQL + ChromaDB + Gemini AI"
)
