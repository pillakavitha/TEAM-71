import json
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Load drug label data
with open("data/drug_label.json", "r") as f:
    data = json.load(f)

text = f"""
Drug: {data['drug']}
Indications: {data['indications']}
Dosage: {data['dosage']}
Warnings: {data['warnings']}
Food Interactions: {data['food_interactions']}
Contraindications: {data['contraindications']}
"""

# Split text
splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
docs = splitter.create_documents([text])

# Free embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Store in ChromaDB
vectordb = Chroma.from_documents(
    docs,
    embedding=embeddings,
    persist_directory="db"
)

vectordb.persist()
print("✅ Drug label indexed successfully")
