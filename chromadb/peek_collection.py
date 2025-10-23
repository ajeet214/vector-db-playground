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
# peeking at the first 10 items
print(collection.peek(limit=23))
"""
{'ids': ['doc', 'doc-1', 'doc-2'], 
 'embeddings': array([[-0.1839793 ,  0.01579099,  0.00901553, ..., -0.02383419,
        -0.02873562, -0.00143125],
       [-0.17177053,  0.0231358 ,  0.01016444, ..., -0.02677561,
        -0.01005194, -0.01157658],
       [-0.16160643,  0.02028787,  0.00803689, ...,  0.00064366,
        -0.04541512, -0.01955493]], shape=(3, 768)), 
 'documents': ['this is the source text', 'this is the source text 1', 'this is the source text 2'], 
 'uris': None, 
 'included': ['metadatas', 'documents', 'embeddings'], 
 'data': None, 
 'metadatas': [None, None, None]
}
"""