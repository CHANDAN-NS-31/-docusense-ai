# 🤖 DocuSense AI

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://docusense-ai.streamlit.app/)

> AI-powered research assistant for **multi-PDF question-answering, summarization, and secure document handling** — built with OpenRouter, LangChain, Hugging Face, and Streamlit.

---

## 📽️ Live Demo

🔗 **App URL**: [https://docusense-ai.streamlit.app](https://docusense-ai.streamlit.app)

Upload multiple research PDFs and interact with them using natural language. Perfect for students, researchers, or professionals analyzing large documents.

---

## 🧠 What is DocuSense AI?

DocuSense AI is a **multi-PDF conversational assistant** that uses LLMs to answer questions and summarize information across documents. It offers:

- 📂 Upload and select from multiple PDFs  
- 💬 Ask intelligent, contextual questions  
- 📄 Summarize documents in one click  
- ✂️ Redact sensitive info like emails and phone numbers  
- 💾 Export Q&A logs as downloadable PDFs  
- 📜 Clean UI, deployable on Streamlit Cloud

---

## ✨ Key Features

| Feature                          | Description |
|----------------------------------|-------------|
| 📥 Upload multiple PDFs          | Analyze multiple documents in one session |
| 🔍 Ask context-aware questions   | Uses FAISS + embeddings to ground responses |
| 🧠 Powered by OpenRouter LLMs    | LLaMA-3 or Mistral available |
| 📜 Summarization button          | Click to summarize any uploaded PDF |
| 🧼 Redaction of sensitive data   | Automatically removes PII (emails, phones, etc.) |
| 📚 Q&A history log               | Logged to `qa_log.txt` during usage |
| 📤 PDF export                    | Save or email generated answers (optional) |
| 🌐 Live streamlit deployment     | Publicly accessible link with your branding |

---

## 🧩 Tech Stack

- 🔗 [LangChain](https://www.langchain.com/) — document loading, text splitting, and retrievers
- 🧬 [Hugging Face](https://huggingface.co/) — `all-MiniLM-L6-v2` sentence embeddings
- 🧠 [OpenRouter](https://openrouter.ai/) — LLMs like LLaMA-3 and Mistral for answer generation
- 📦 [FAISS](https://github.com/facebookresearch/faiss) — vector similarity search
- 📄 [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) — PDF parsing
- 🎨 [Streamlit](https://streamlit.io) — user interface and deployment
- 🧼 `re` + `utils.py` — redaction using regex patterns
- 🔐 `.env` — stores API key securely (never pushed to GitHub)

---

## 📁 Folder Structure

docusense-ai/
├── app.py # Streamlit frontend logic
├── utils.py # Helper functions like redaction
├── requirements.txt # Python dependencies
├── .env.example # Template for env variable
├── qa_log.txt # Q&A log file (auto-generated)
├── pdfs/ # Uploaded PDF storage
└── README.md # You're here!
![Screenshot 2025-06-26 002254](https://github.com/user-attachments/assets/39051685-733d-45cf-9eeb-e6e74633fc00)



Pull requests and feature suggestions are welcome!
