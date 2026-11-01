
import mysql.connector
import chromadb
from sentence_transformers import SentenceTransformer

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="real_estate_db"
)

cursor = connection.cursor(dictionary=True)

cursor.execute("SELECT * FROM properties")
properties = cursor.fetchall()

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="real_estate_properties"
)

# Store property information
for property in properties:
    text = (
        f"Title: {property['title']}, "
        f"Type: {property['propertyType']}, "
        f"Locality: {property['locality']}, "
        f"Bedrooms: {property['bedrooms']}, "
        f"Price: {property['price']}, "
        f"Area: {property['areaSqFt']} square feet, "
        f"Amenities: {property['amenities']}, "
        f"Description: {property['description']}"
    )

    embedding = model.encode(text).tolist()

    collection.upsert(
        ids=[property["propertyId"]],
        documents=[text],
        embeddings=[embedding]
    )

print("Properties successfully stored in ChromaDB!")
print("Total properties:", collection.count())

cursor.close()
connection.close()
