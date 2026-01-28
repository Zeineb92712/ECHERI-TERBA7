from ai.src.pdf_loader import load_pdf
from ai.src.product_chunker import chunk_pages
from ai.src.embedder import embed_texts
from ai.src.qdrant_store import recreate_collection, upsert_chunks
from ai.src.config import PDF_PATH

def main():
    print("[START] PIPELINE")

    pages = load_pdf(PDF_PATH)
    chunks = chunk_pages(pages)
    vectors = embed_texts(chunks)

    recreate_collection()
    upsert_chunks(chunks, vectors)

    print("[DONE] Data indexed into Qdrant")

if __name__ == "__main__":
    main()
