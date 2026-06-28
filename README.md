<img width="1918" height="966" alt="chatbot png" src="https://github.com/user-attachments/assets/4c1bc4b0-cbb0-44a4-9e96-f1cddc9759cd" />

# AI DSA Instructor

An AI-powered chatbot that answers Data Structures and Algorithms (DSA) questions from a PDF using Retrieval-Augmented Generation (RAG).

## Features

- Upload and read DSA PDF
- Split PDF into chunks
- Generate embeddings
- Store embeddings in FAISS
- Retrieve relevant content
- Answer questions using Google Gemini
- Streamlit web interface

## Technologies Used

- Python
- Streamlit
- LangChain
- FAISS
- Google Gemini API
- Hugging Face Embeddings

## Project Structure

AI_DSA_Instructor/
│
├── data/
│ └── dsa.pdf
│
├── faiss_index/
├── app.py
├── ingest.py
├── vector_store.py
├── requirements.txt
└── README.md

## Run

```bash
pip install -r requirements.txt

streamlit run app.py
```
