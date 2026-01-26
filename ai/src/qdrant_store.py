from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

COLLECTION_NAME = "products"

client = QdrantClient(
    url="YOUR_QDRANT_URL",
    api_key="YOUR_API_KEY"
)

def setup_collection():
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=384,
            distance=Distance.COSINE
        )
    )

def store(chunks, embeddings):
    points = []
    for i, (text, vector) in enumerate(zip(chunks, embeddings)):
        points.append({
            "id": i,
            "vector": vector.tolist(),
            "payload": {"text": text}
        })

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )
    print(f"[INFO] Stored {len(points)} vectors")
