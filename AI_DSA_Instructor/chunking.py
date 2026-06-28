from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Read the PDF
reader = PdfReader("data/dsa.pdf")

text = ""

for page in reader.pages:
    extracted = page.extract_text()
    if extracted:
        text += extracted

print("Total characters:", len(text))

# Split the text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_text(text)

print("Total chunks:", len(chunks))

print("\nFirst chunk:\n")
print(chunks[0])
