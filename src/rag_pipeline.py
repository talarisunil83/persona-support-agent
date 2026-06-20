import os

def load_documents(data_path):

    documents = []

    for file_name in os.listdir(data_path):

        file_path = os.path.join(data_path, file_name)

        if os.path.isfile(file_path):

            with open(file_path, "r", encoding="utf-8") as file:

                content = file.read()

                documents.append(
                    {
                        "file_name": file_name,
                        "content": content
                    }
                )

    return documents

def search_documents(query, documents):

    query = query.lower()

    for doc in documents:

        if any(word in doc["content"].lower() for word in query.split()):
            return doc

    return None