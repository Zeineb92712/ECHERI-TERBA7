from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
from ai.src.config import COLLECTION_NAME, VECTOR_SIZE, QDRANT_PATH

def get_client():
    return QdrantClient(path=QDRANT_PATH)

def recreate_collection():
    client = get_client()
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=VECTOR_SIZE,
            distance=Distance.COSINE
        )
    )

def upsert_chunks(texts: list[str], vectors: list[list[float]]):
    client = get_client()

    points = [
        PointStruct(
            id=i,
            vector=vectors[i],
            payload={"text": texts[i]}
        )
        for i in range(len(texts))
    ]

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )
