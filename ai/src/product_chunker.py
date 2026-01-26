from llama_index.core.node_parser import TokenTextSplitter

def chunk_text(text: str):
    splitter = TokenTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    return splitter.split_text(text)
