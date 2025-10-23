import chromadb
from chromadb.utils.embedding_functions import OllamaEmbeddingFunction


# 1. Initialize Chroma client (local persistence)
client = chromadb.PersistentClient(path="./chromadb/chroma_data")


# Retrieve the demo_collection collection
collection = client.get_collection(
    name="demo_collection",
    embedding_function=OllamaEmbeddingFunction(
        url="http://localhost:11434",
        model_name="embeddinggemma"
    )
)

# query the collection
search1 = collection.query(
    query_texts=["quantum computing"],
    n_results=1,
    where_document={"$contains": "quantum"}
)
print(search1)

search2 = collection.query(
    query_texts=["computing"],
    n_results=1,
    where={
        "$and": [
            {
               "topic": {"$eq": "quantum computing"}
            },
            {
               "source": {"$eq": "research"}
            }
        ]
    }
)
print(search2)
