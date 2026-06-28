from pypdf import PdfReader

# Load the PDF
pdf = PdfReader("data/dsa.pdf")

# Print number of pages
print(f"Number of pages: {len(pdf.pages)}")

# Read each page
for page_number, page in enumerate(pdf.pages, start=1):
    text = page.extract_text()

    print(f"\n========== Page {page_number} ==========")

    if text:
        print(text[:500])   # Print first 500 characters
    else:
        print("No text found on this page.")