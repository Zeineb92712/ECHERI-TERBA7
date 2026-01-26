from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct

COLLECTION_NAME = "product_catalog"

client = QdrantClient(path="ai/data/qdrant")

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

    for i, (chunk, vector) in enumerate(zip(chunks, embeddings)):
        points.append(
            PointStruct(
                id=i,
                vector=vector.tolist(),
                payload={"text": chunk}
            )
        )

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )
