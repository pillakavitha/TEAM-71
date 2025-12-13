from fastapi import FastAPI
from rag_chatbot import ask_drug
from reminder import create_reminder

app = FastAPI(title="Medication Reminder Chatbot")

@app.post("/ask")
def ask(question: str):
    return {"answer": ask_drug(question)}

@app.post("/reminder")
def reminder(drug: str, dosage: str, frequency: str):
    return create_reminder(drug, dosage, frequency)
