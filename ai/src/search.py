from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient

COLLECTION_NAME = "product_catalog"

model = SentenceTransformer("all-MiniLM-L6-v2")

client = QdrantClient(
    path="ai/data/qdrant"
)

def search(query: str, limit: int = 5):
    vector = model.encode(query).tolist()

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=vector,
        limit=limit
    )

    print("\n🔎 SEARCH RESULTS:\n")

    for point in results.points:
        print("-----")
        print(point.payload["text"])
