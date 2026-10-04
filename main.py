from src.pdf_loader import extract_pages
from src.chunker import create_chunks
import json


PDF_PATH = "data/Deep learning.pdf"


# Step 1: Extract text from PDF
pages = extract_pages(PDF_PATH)

print("\n============================")
print("PDF PROCESSING COMPLETE")
print("============================")

print("Pages with text:", len(pages))


# Step 2: Create chunks
chunks = create_chunks(pages)

print("\n============================")
print("CHUNKING COMPLETE")
print("============================")

print("Total chunks:", len(chunks))


# Step 3: Save chunks
with open(
    "vector_store/chunks.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        chunks,
        file,
        ensure_ascii=False,
        indent=4
    )

print("Chunks saved to vector_store/chunks.json")


# Step 4: Show first 5 chunks
for chunk in chunks[:5]:

    print("\n----------------------------")
    print("Chunk ID:", chunk["chunk_id"])
    print("Page:", chunk["page_number"])
    print("Text:")
    print(chunk["text"][:300])
