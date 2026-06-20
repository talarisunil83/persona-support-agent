from src.rag_pipeline import load_documents, search_documents

documents = load_documents("data")

result = search_documents(
    "How do I reset my password?",
    documents
)

if result:
    print("Found Document:")
    print(result["file_name"])
    print(result["content"])
else:
    print("No document found")  


