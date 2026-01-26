from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient

model = SentenceTransformer("all-MiniLM-L6-v2")

client = QdrantClient(
    url="YOUR_QDRANT_URL",
    api_key="YOUR_API_KEY"
)

def search(query: str, limit=5):
    vector = model.encode(query).tolist()

    results = client.search(
        collection_name="products",
        query_vector=vector,
        limit=limit
    )

    for r in results:
        print("----")
        print(r.payload["text"])
