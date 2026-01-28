def chunk_pages(pages: list[str], max_len=500) -> list[str]:
    chunks = []

    for page in pages:
        blocks = page.split("\n\n")
        current = ""

        for block in blocks:
            if len(current) + len(block) <= max_len:
                current += " " + block
            else:
                chunks.append(current.strip())
                current = block

        if current.strip():
            chunks.append(current.strip())

    return chunks
