
# 🏠 Real Estate Assistant Using RAG

## 📌 Project Overview
Real Estate Assistant Using RAG is an AI-powered web application that helps users find suitable properties by entering their requirements in simple natural language.

The system retrieves relevant property information from ChromaDB and uses Gemini AI to generate answers.

## 🎯 Project Objectives
- Help users search properties easily.
- Find properties using natural language queries.
- Retrieve relevant property details.
- Display property information in a simple interface.

## 🚀 Technologies Used
- Python
- Streamlit
- MySQL
- ChromaDB
- Sentence Transformers
- Google Gemini API
- HTML and CSS

## ✨ Features
- Natural language property search.
- AI-powered responses using Gemini.
- Semantic search using ChromaDB.
- Property details with price, location and amenities.
- Backup mode when Gemini is unavailable.

## ⚙️ Project Workflow
1. User enters a property requirement.
2. Sentence Transformer converts the query into an embedding.
3. ChromaDB retrieves relevant property information.
4. Gemini AI generates a response using retrieved data.
5. Streamlit displays the answer and matching properties.

## 💻 Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Go to the project folder:

```bash
cd RealEstateRAG
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your Gemini API key:

```env
GOOGLE_API_KEY=your_api_key
```

Create the vector database:

```bash
python create_vector_db.py
```

Run the application:

```bash
streamlit run app.py
```

## 👩‍💻 Developed As
MCA Academic Project

## 📄 Note
Keep your API key private. Never upload your `.env` file to GitHub.
