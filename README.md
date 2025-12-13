📌 Project Overview
The Medication Reminder Chatbot (Label-Aware) is an intelligent, retrieval-based chatbot that answers user questions using official drug label information and generates medication reminder schedules. The system also provides awareness about food–drug interactions, helping users take medicines safely and on time.
This project uses Retrieval-Augmented Generation (RAG) techniques and works entirely with free/open-source tools, making it suitable for academic mini-projects and PBL submissions.

🎯 Problem Statement
Medication errors, missed doses, and lack of awareness about food–drug interactions are common healthcare issues. Drug labels contain important safety information, but they are often long and difficult for patients to understand.
There is a need for an intelligent system that can:
Answer questions based on official drug labels
Explain dosage, warnings, and food–drug interactions clearly
Generate a medication reminder schedule
Work without paid APIs or SMS/phone integration

💡 Solution Description
This project implements a label-aware medication chatbot using a RAG architecture. Drug label data is ingested, split into chunks, converted into embeddings, and stored in a ChromaDB vector database.
When a user asks a question, the system retrieves the most relevant drug label information and provides an accurate response. The chatbot can also detect food-related queries and explain possible food–drug interactions. Additionally, it generates a structured medication reminder plan in JSON format.

🚀 Features
📄 Drug label–based question answering
🍽️ Food–drug interaction awareness
⏰ Medication reminder plan generation (JSON)
🧠 Retrieval-Augmented Generation (RAG)
🆓 Uses free HuggingFace embeddings (no paid APIs)
🧩 Modular and scalable design

🛠️ Technology Stack
Language: Python
Framework: LangChain
Vector Database: ChromaDB
Embeddings: HuggingFace (Sentence Transformers)]
API (Optional): FastAPI]
Data Source: Drug label JSON (openFDA-style)
