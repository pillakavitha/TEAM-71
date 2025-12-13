from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

vectordb = Chroma(
    persist_directory="db",
    embedding_function=embeddings
)

def ask_drug(question):
    docs = vectordb.similarity_search(question, k=2)
    answer = "\n".join([doc.page_content for doc in docs])
    return answer

if __name__ == "__main__":
    while True:
        q = input("Ask a drug question (type exit to quit): ")
        if q.lower() == "exit":
            break
        print("\nAnswer:\n", ask_drug(q))
