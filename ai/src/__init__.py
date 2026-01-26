from pdf_extractor import extract_text_from_pdf
from chunker import chunk_text
from embedder import embed_chunks
from qdrant_store import setup_collection, store_chunks

PDF_PATH = "ai/data/pdfs/Decathlon.pdf"

if __name__ == "__main__":
    text = extract_text_from_pdf(PDF_PATH)
    print("Text extracted")

    chunks = chunk_text(text)
    print("Chunks:", len(chunks))

    embeddings = embed_chunks(chunks)
    print("Embeddings ready")

    setup_collection()
    store_chunks(chunks, embeddings)
    print("Stored in Qdrant")
