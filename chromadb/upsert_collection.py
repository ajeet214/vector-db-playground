import chromadb
from chromadb.utils.embedding_functions import OllamaEmbeddingFunction


# 1. Initialize Chroma client (local persistence)
client = chromadb.PersistentClient(path="./chromadb/chroma_data")

# 2. Create a collection
collection = client.get_or_create_collection(
    name="demo_collection",
    embedding_function=OllamaEmbeddingFunction(
        url="http://localhost:11434",
        model_name="embeddinggemma"
    )
)


# upserting a collection -> upadte+add (add if not present, update if ids are present)
collection.upsert(
    ids=["doc22"],
    documents=["this is the text in doc22"]
)
