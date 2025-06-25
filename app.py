# app.py (Premium SaaS-Styled Version)

import os
import time
import textwrap
import requests
import streamlit as st
from dotenv import load_dotenv
from utils import redact_sensitive_info
from fpdf import FPDF
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from utils import redact_sensitive_info


# -------------------- CONFIG --------------------
st.set_page_config(page_title="📄 DocuSense AI", layout="wide")
st.markdown("""
    <style>
    body {font-size: 1.1rem;}
    .stMarkdown h1 {color: #FF4B4B; font-size: 2.6rem;}
    .stMarkdown p, .stMarkdown li, .stMarkdown div {font-size: 1.05rem !important;}
    </style>
    """, unsafe_allow_html=True)

# -------------------- HEADER --------------------
st.sidebar.title("📥 Upload PDFs")
uploaded_files = st.sidebar.file_uploader("Upload one or more PDFs", type=["pdf"], accept_multiple_files=True)

# ⛨ Sidebar: Redaction toggle
st.sidebar.markdown("## 🛡️ Privacy Settings")
st.sidebar.toggle("🔒 Enable Redaction", value=True, key="enable_redaction")


st.title("📄 DocuSense AI — Multi-PDF Q&A Assistant")
st.caption("Your smart, private PDF research assistant 🧠 — powered by LLMs")

# -------------------- ENV + API --------------------
load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "meta-llama/llama-3-8b-instruct"

# -------------------- DATA HANDLING --------------------
os.makedirs("pdfs", exist_ok=True)
filenames = []
for file in uploaded_files:
    filepath = os.path.join("pdfs", file.name)
    with open(filepath, "wb") as f:
        f.write(file.read())
    filenames.append(filepath)

retrievers = {}
if filenames:
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    for fname in filenames:
        docs = splitter.split_documents(PyMuPDFLoader(fname).load())
        db = FAISS.from_documents(docs, embeddings)
        retrievers[fname] = db.as_retriever()

# -------------------- SESSION STATE --------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -------------------- FUNCTION: OpenRouter --------------------
def call_openrouter_api(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://chat.openai.com",
        "X-Title": "DocuSense AI"
    }
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }
    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ Error: {e}"

# -------------------- FUNCTION: Export to PDF --------------------
def export_to_pdf(history):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for i, (q, a) in enumerate(history):
        pdf.multi_cell(0, 10, f"Q{i+1}: {q}\nA{i+1}: {a}\n{'-'*60}")
    pdf.output("DocuSense_QA_Export.pdf")
    st.success("✅ Exported to DocuSense_QA_Export.pdf")

# -------------------- FUNCTION: Ask Question --------------------
def ask_question(query, retriever):
    results = retriever.get_relevant_documents(query)
    context = "\n\n".join([doc.page_content for doc in results[:2]])
    context = redact_sensitive_info(context)
    prompt = f"""You are a helpful assistant. Use the following PDF content to answer the question.\n\n📘 Context:\n{context}\n\n❓ Question:\n{query}\n\n🧠 Answer:"""
    prompt = redact_sensitive_info(prompt)
    with st.spinner("🤖 Generating answer..."):
        response = call_openrouter_api(prompt)
    return response

# -------------------- FUNCTION: Summarize PDF --------------------
def summarize_pdf(retriever):
    results = retriever.get_relevant_documents("summarize this document")
    context = "\n\n".join([doc.page_content for doc in results[:4]])
    context = redact_sensitive_info(context)
    prompt = f"""Summarize the following PDF content:\n\n{context}"""
    with st.spinner("📄 Summarizing document..."):
        return call_openrouter_api(prompt)

# -------------------- MAIN UI --------------------
if retrievers:
    selected = st.selectbox("📚 Choose a PDF", filenames, format_func=os.path.basename)
    retriever = retrievers[selected]

    col1, col2 = st.columns([3, 1])
    with col1:
        query = st.text_input("❓ Ask a question about the selected PDF:")
        if st.button("Ask") and query:
            answer = ask_question(query, retriever)
            st.session_state.chat_history.append((query, answer))
            st.success("✅ Answer:")
            for line in textwrap.wrap(answer.strip(), width=100):
                st.markdown(line)
                time.sleep(0.2)



    with col2:
        if st.button("📜 Summarize This PDF"):
            summary = summarize_pdf(retriever)
            st.info(summary)

        if st.button("📥 Export Q&A to PDF"):
            export_to_pdf(st.session_state.chat_history)

    # Show chat history
    if st.session_state.chat_history:
        st.markdown("---")
        st.subheader("🧠 Q&A History")
        for i, (q, a) in enumerate(reversed(st.session_state.chat_history)):
            st.markdown(f"**Q{i+1}:** {q}")
            st.markdown(f"_A{i+1}:_ {a}")
else:
    st.info("📂 Upload one or more PDFs to begin.")
