from ai.src.qdrant_store import get_client
from ai.src.embedder import embed_texts
from ai.src.config import COLLECTION_NAME

def search(query: str, limit=5):
    client = get_client()
    vector = embed_texts([query])[0]

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=vector,
        limit=limit,
        with_payload=True
    )

    return results.points
