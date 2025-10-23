import chromadb
from chromadb.utils.embedding_functions import OllamaEmbeddingFunction


# 1. Initialize Chroma client (local persistence)
client = chromadb.PersistentClient(path="./chromadb/chroma_data")

# 2. Create a collection
collection = client.get_collection(
    name="demo_collection",
    embedding_function=OllamaEmbeddingFunction(
        url="http://localhost:11434",
        model_name="embeddinggemma"
    )
)

# -----------------------------------------------------
# insert single doc
collection.add(
    ids=["doc"],
    documents=["this is the source text"]
)


# insert multiple doc
collection.add(
    documents=[
        "This is a document about electric vehicles and renewable energy.",
        "A detailed blog on healthy eating and plant-based diets.",
        "Research paper discussing quantum computing breakthroughs in 2025.",
        "News article covering the latest updates in space exploration.",
        "A tutorial explaining how to build REST APIs with FastAPI.",
        "An essay analyzing climate change and global warming impacts.",
        "A case study on how AI is transforming the healthcare industry.",
        "A transcript of an interview with a famous startup founder.",
        "Guide to mastering Python for data science and automation.",
        "Product review comparing the top 5 smartphones of 2025.",
        "Documentation about deploying ML models using Docker containers.",
        "A travel diary from a backpacking trip across Southeast Asia.",
        "Technical blog post about cybersecurity and ethical hacking.",
        "Whitepaper explaining blockchain scalability solutions.",
        "A fictional story set in a futuristic smart city powered by AI.",
        "An opinion piece discussing the ethics of gene editing.",
        "A step-by-step guide to personal finance and investing basics.",
        "Research summary on ocean biodiversity and coral reef loss.",
        "An educational note on the history of the Roman Empire.",
        "Interview summary with an artist about modern digital art."
    ],
    metadatas = [
        {"source": "journal", "topic": "automotive"},
        {"source": "blog", "topic": "health"},
        {"source": "research", "topic": "quantum computing"},
        {"source": "news", "topic": "space"},
        {"source": "tutorial", "topic": "web development"},
        {"source": "essay", "topic": "environment"},
        {"source": "case_study", "topic": "AI"},
        {"source": "interview", "topic": "entrepreneurship"},
        {"source": "guide", "topic": "data science"},
        {"source": "review", "topic": "technology"},
        {"source": "documentation", "topic": "machine learning"},
        {"source": "travel", "topic": "tourism"},
        {"source": "blog", "topic": "cybersecurity"},
        {"source": "whitepaper", "topic": "blockchain"},
        {"source": "fiction", "topic": "AI", },
        {"source": "opinion", "topic": "bioethics"},
        {"source": "guide", "topic": "finance"},
        {"source": "research", "topic": "marine biology"},
        {"source": "educational", "topic": "history"},
        {"source": "interview", "topic": "art"}
    ],
    ids=[
        "doc1", "doc2", "doc3", "doc4", "doc5",
        "doc6", "doc7", "doc8", "doc9", "doc10",
        "doc11", "doc12", "doc13", "doc14", "doc15",
        "doc16", "doc17", "doc18", "doc19", "doc20"
    ]
)
