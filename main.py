import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

# data will be persisted to disk
client = chromadb.PersistentClient(path="/path/to/save/to")

# create a collections
collection = client.create_collection(
    name="",
    embedding_function=OpenAIEmbeddingFunction(
        model_name="",
        api_key=""
    )
)

# List the collections
print(client.list_collections())

# insert single doc
collection.add(
    ids=["my-doc"],
    documents=["this is the source text"]
)


# insert multiple doc
collection.add(
    ids=["my-doc-1", "my-doc-2"],
    documents=["this is the source text 1", "this is the source text 1"]
)

# count documents in a collection
collection.count()

# peeking at the first 10 items
collection.peek()

# retrieving items by ids
collection.get(ids=['s56'])

# Retrieve the netflix_titles collection
collection = client.get_collection(
  name="netflix_titles",
  embedding_function=OpenAIEmbeddingFunction(model_name="text-embedding-3-small", api_key="<OPENAI_API_TOKEN>")
)

# --------------------------------------------------------------------------

# estimating token cost
import tiktoken

enc = tiktoken.encoding_for_model("text-embedding-3-small")

total_tokens = sum(len(enc.encode(text)) for text in documents)

cost_per_1k_tokens = 0.00002

print(f"Total tokens: {total_tokens}")
print(f"Cost: {cost_per_1k_tokens*total_tokens/1000}")

# --------------------------------------------------------------------------

# query the collection
result = collection.query(
    query_texts=[""],
    n_results=3
)
print(result)

"""
{
"ids": [...],
"embeddings": None,
"documents": [...],
"metadatas": [...],
"distances": [...],
}
"""

# update a collection
collection.update(
    ids=["ids1", "ids2"],
    documents=["this is doc1", "this is doc2"]
)

# upserting a collection -> upadte+add (add if not present, update if ids are present)
collection.upsert(
    ids=["ids1", "ids2"],
    documents=["this is doc1", "this is doc2"]
)

# delete items from a collection
collection.delete(ids=["id1", "id2"])

# delete all collections and items
client.reset()

# --------------------------------------------------------------------------
#multiple query texts

reference_ids = ['s8170', 's8013']

reference_texts = collection.get(ids=reference_ids)['documents']

result = collection.query(
    query_texts=reference_texts,
    n_results=3
)

# adding metadata
import csv

ids = []
metadatas = []

with open("netflix_titles.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for i, row in enumerate(reader):
        ids.append(row['show_id'])
        metadatas.append({
            "type": row['type'],
            "release_year": int(row['release_year'])
        })

# adding and quering metadatas
collection.update(ids=ids, metadatas=metadatas)

result = collection.query(
    query_texts=reference_texts,
    n_results=3,
    where={
        "type": "Movie"
    }
)
"""
where={
        "type": "Movie"
    }
or 
where={
        "type": {
            "$eq": "Movie"
        }
    }
other operators:
$eq
$ne
$gt
$gte
$lt
$lte

multiple where filters:

where = {
    "$and": [
        {
           "type": {"$eq": "Movie"}
        },
        {
           "release_year": {"$gt": 2020}
        }
    ]
}

$or
"""