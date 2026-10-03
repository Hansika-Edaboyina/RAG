from src.pdf_loader import extract_pages


PDF_PATH = "data/Deep learning.pdf"


pages = extract_pages(PDF_PATH)

print("Number of pages:", len(pages))

for page in pages[:3]:

    print("\n====================")
    print("PAGE:", page["page_number"])
    print(page["text"][:500])