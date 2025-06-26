# 🤖 DocuSense AI

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://docusense-ai.streamlit.app/)

> AI-powered research assistant for **multi-PDF question-answering, summarization, redaction, and secure export** — built with OpenRouter, LangChain, Hugging Face, and Streamlit.

---

## 📽️ Live Demo

🔗 **App URL**: [https://docusense-ai.streamlit.app](https://docusense-ai.streamlit.app)

Upload multiple PDFs and ask questions, generate summaries, toggle redaction, and export logs — all in one clean, professional UI.

---

## 🧠 What is DocuSense AI?

**DocuSense AI** is your smart PDF research assistant that allows you to upload academic papers, government docs, or technical reports and:

- 📂 Upload and interact with **multiple PDFs**
- 💬 Ask **natural language questions**
- 📜 Summarize documents in one click
- 🔐 **Toggle PII redaction** ON/OFF from the UI
- 💾 Export question-answer **logs as PDF**
- 🧠 Review **chat history** across sessions

---

## ✨ Key Features

| Feature                          | Description |
|----------------------------------|-------------|
| 📥 Upload multiple PDFs          | Analyze multiple documents in one session |
| 🔍 Ask context-aware questions   | Uses FAISS + HuggingFace embeddings to provide grounded answers |
| 🧠 Powered by OpenRouter LLMs    | Choose between LLaMA-3, Mistral, etc. |
| 📜 One-click summarization       | Summarize any document instantly |
| 🧼 Redaction toggle (ON/OFF)     | Automatically removes PII like email, phone, Aadhaar, PAN, student IDs, DOB |
| 🧠 Q&A history log               | Conversation is saved within the app |
| 📤 Export as PDF                 | Save full Q&A chat to a file |
| 🌐 Live Streamlit deployment     | Public link with your branding |
| 🎨 Modern UI/UX                  | SaaS-style sidebar, emoji-rich design, responsive interface |

---

## 🛡️ What Gets Redacted?

When the **redaction switch is ON**, the following types of sensitive information are hidden:

- 📧 Email addresses
- 📱 Phone numbers (Indian format)
- 🆔 Aadhaar numbers
- 💳 PAN numbers
- 🏫 College or student IDs (e.g., ENG22CS0038)
- 🔢 Application/reference numbers
- 📅 Dates of birth (in multiple formats)
- 🧑 Named titles like “Mr./Dr./Prof. [Name]”
- 🧾 Generic government ID formats (e.g., DL-042021...)

---

## 🧩 Tech Stack

- 🔗 [LangChain](https://www.langchain.com/) — document loading, splitting, retrieval
- 🧬 [Hugging Face](https://huggingface.co/) — sentence embeddings via `all-MiniLM-L6-v2`
- 🧠 [OpenRouter](https://openrouter.ai/) — LLMs like LLaMA-3 and Mistral
- 📦 [FAISS](https://github.com/facebookresearch/faiss) — vector similarity search
- 📄 [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) — PDF parsing
- 🎨 [Streamlit](https://streamlit.io) — UI and live hosting
- 🧼 `utils.py` — regex-based redaction system
- 🔐 `.env` / Streamlit Secrets — stores your API key securely

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




Pull requests and feature suggestions are welcome!
