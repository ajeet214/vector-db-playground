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

# -----------------------------------------------------
# retrieving items by ids
print(collection.get(ids=['doc']))
"""
{'ids': ['doc'], 
 'embeddings': None, 
 'documents': ['this is the source text'], 
 'uris': None, 
 'included': ['metadatas', 'documents'], 
 'data': None, 
 'metadatas': [None]
}
"""