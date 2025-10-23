import chromadb
from chromadb.errors import NotFoundError


# Initialize Chroma client (local persistence)
client = chromadb.PersistentClient(path="./chromadb/chroma_data")

try:
    # delete the collection demo_collection
    client.delete_collection("demo_collection")

except NotFoundError as e:
    print(e.message())
