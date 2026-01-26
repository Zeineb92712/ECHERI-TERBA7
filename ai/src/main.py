from ai.src.pdf_loader import extract_text
from ai.src.product_chunker import chunk_text
from ai.src.embedder import embed_chunks
from ai.src.qdrant_store import setup_collection, store

def run():
    print("[START] PIPELINE")

    text = extract_text("ai/data/pdfs/Decathlon.pdf")
    chunks = chunk_text(text)
    embeddings = embed_chunks(chunks)

    setup_collection()
    store(chunks, embeddings)

    print("[DONE] Data indexed into Qdrant")

if __name__ == "__main__":
    run()
