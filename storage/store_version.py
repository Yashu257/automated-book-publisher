# storage/store_version.py

import chromadb

def store_version(doc_id: str, final_text: str):
    """
    Stores the final approved version of the chapter in ChromaDB (new API format).
    """
    #  Create a client using new config (no Settings import)
    client = chromadb.PersistentClient(path="./chroma_storage")

    #  Get or create the collection
    collection = client.get_or_create_collection("book_chapters")

    #  Add the document
    collection.add(
        documents=[final_text],
        ids=[doc_id]
    )

    print(f" Stored version for: {doc_id}")
