from src.rag_pipeline import load_documents, search_documents
from src.classifier import classify_persona
from src.llm import generate_answer

documents = load_documents("data")

while True:

    query = input("\nAsk a question (type exit to quit): ")

    if query.lower() == "exit":
        break

    persona = classify_persona(query)

    result = search_documents(query, documents)

    if result:

        answer = generate_answer(
            query,
            result["content"],
            persona
        )

        print("\nPersona:", persona)
        print("\nAnswer:")
        print(answer)

    else:
        print("No relevant document found.")