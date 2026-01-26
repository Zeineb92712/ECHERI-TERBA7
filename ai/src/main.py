from pdf_loader import extract_text
from product_chunker import chunk_text
from embedder import embed_chunks
from qdrant_store import setup_collection, store

PDF_PATH = "ai/data/pdfs/Decathlon.pdf"

def run_pipeline():
    print("[START] Pipeline")

    # 1️⃣ Extract text
    text = extract_text(PDF_PATH)
    print(f"[OK] Extracted text length: {len(text)}")

    # 2️⃣ Chunk text into products
    chunks = chunk_text(text)
    print(f"[OK] Number of product chunks: {len(chunks)}")

    # 3️⃣ Embed chunks
    embeddings = embed_chunks(chunks)
    print("[OK] Embeddings created")

    # 4️⃣ Store in Qdrant
    setup_collection()
    store(chunks, embeddings)
    print("[DONE] Data stored in Qdrant")


if __name__ == "__main__":
    run_pipeline()
