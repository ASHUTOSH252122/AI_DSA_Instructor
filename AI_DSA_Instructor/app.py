import streamlit as st
from dotenv import load_dotenv

from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI,
)
from langchain_community.vectorstores import FAISS

# -----------------------------
# Load API Key
# -----------------------------
load_dotenv()

# -----------------------------
# Streamlit Page
# -----------------------------
st.set_page_config(
    page_title="AI DSA Instructor",
    page_icon="📘",
    layout="wide",
)

st.title("📘 AI DSA Instructor")
st.write("Ask any question from your DSA PDF.")

# -----------------------------
# Load Embeddings
# -----------------------------
@st.cache_resource
def load_db():
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001"
    )

    db = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True,
    )

    return db


db = load_db()

st.success("✅ FAISS Database Loaded")

# -----------------------------
# Retriever
# -----------------------------
retriever = db.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 4},
)

st.success("✅ Retriever Ready")

# -----------------------------
# Gemini Model
# -----------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3,
)

st.success("✅ Gemini Connected")

# -----------------------------
# User Input
# -----------------------------
question = st.text_input(
    "💬 Ask your DSA Question"
)

# -----------------------------
# Answer Generation
# -----------------------------
if question:

    with st.spinner("Searching your DSA notes..."):

        docs = retriever.invoke(question)

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        prompt = f"""
You are an expert Data Structures and Algorithms instructor.

Answer ONLY using the context provided below.

If the answer is not available in the context,
reply exactly:

"I couldn't find this information in the provided DSA PDF."

Context:
{context}

Question:
{question}

Answer:
"""

        response = llm.invoke(prompt)

    st.subheader("📖 Answer")

    st.write(response.content)

    with st.expander("📚 Source Chunks"):

        for i, doc in enumerate(docs, start=1):

            st.markdown(f"### Chunk {i}")

            st.write(doc.page_content)

            st.divider()