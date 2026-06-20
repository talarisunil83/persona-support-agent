import streamlit as st

from src.rag_pipeline import load_documents, search_documents
from src.classifier import classify_persona
from src.llm import generate_answer

st.title("Persona Support Agent")

documents = load_documents("data")

query = st.text_input("Ask your question")

if st.button("Submit"):

    if query:

        persona = classify_persona(query)

        result = search_documents(query, documents)

        if result:

            answer = generate_answer(
                query,
                result["content"],
                persona
            )

            st.success(f"Detected Persona: {persona}")
            st.write(answer)

        else:
            st.error("No relevant document found.")