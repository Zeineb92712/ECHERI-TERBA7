from llama_index.core.node_parser import TokenTextSplitter

def chunk_text(text: str):
    splitter = TokenTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    chunks = splitter.split_text(text)
    print(f"[INFO] Created {len(chunks)} chunks")
    return chunks
