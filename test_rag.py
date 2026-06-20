from src.rag_pipeline import load_documents

documents = load_documents("data")

print("Documents Loaded:", len(documents))

for doc in documents:
    print(doc["file_name"])