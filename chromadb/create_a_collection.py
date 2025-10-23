import chromadb
from chromadb.utils.embedding_functions import OllamaEmbeddingFunction
from chromadb.errors import InternalError


# 1. Initialize Chroma client (local persistence)
client = chromadb.PersistentClient(path="./chromadb/chroma_data")

try:
    #  Create a collection
    collection = client.create_collection(
        name="demo_collection",
        embedding_function=OllamaEmbeddingFunction(
            url="http://localhost:11434",
            model_name="embeddinggemma"
        )
    )
    print(f"Collection [{collection.name}] created!")

except InternalError as e:
    print(e.message())