import chromadb
from chromadb.utils.embedding_functions import OllamaEmbeddingFunction


# 1. Initialize Chroma client (local persistence)
# client = chromadb.Client(chromadb.config.Settings(persist_directory="./chroma_data"))
client = chromadb.PersistentClient(path="./chromadb/chroma_data")

## For an in-memory database (data is lost when the script ends)
# client = chromadb.Client()

# 2. Create a collection
# collection = client.create_collection()
collection = client.get_or_create_collection(
    name="demo_collection",
    embedding_function=OllamaEmbeddingFunction(
        url="http://localhost:11434",
        model_name="embeddinggemma"
    )
)

# List the available collections
print(client.list_collections())
