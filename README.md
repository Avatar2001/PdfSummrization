# 📄 PDF Summarizer using LangChain and Streamlit

This is a simple yet powerful PDF summarization tool built with **LangChain**, **FAISS**, **OpenAI's GPT models**, **HuggingFace embeddings**, and **Streamlit**. Upload a PDF file and get a concise summary of its contents using LLM-powered question answering.

## 🔍 Features

- 📄 Upload and read PDF files
- 🧠 Chunk and embed the PDF content with HuggingFace BGE embeddings
- 🔎 Store chunks in a FAISS vector store for semantic similarity search
- 🧾 Query the vector store to retrieve relevant content
- 🤖 Use OpenAI GPT-3.5-turbo to generate a high-quality summary
- 🖥️ Simple and intuitive Streamlit UI

---

## 🛠️ Tech Stack

- [LangChain](https://github.com/langchain-ai/langchain)
- [FAISS](https://github.com/facebookresearch/faiss)
- [OpenAI GPT-3.5](https://platform.openai.com/)
- [HuggingFace Sentence Transformers](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
- [PyPDF](https://pypi.org/project/pypdf/)
- [Streamlit](https://streamlit.io/)
- [dotenv](https://pypi.org/project/python-dotenv/)

---

## 🚀 How It Works

1. Upload a PDF file in the Streamlit app.
2. The PDF is parsed and split into chunks using `CharacterTextSplitter`.
3. Each chunk is embedded using `sentence-transformers/all-MiniLM-L6-v2`.
4. FAISS is used to create a vector store from these embeddings.
5. A query ("Summarize the content of the uploaded PDF file") is run against the vector store.
6. The most relevant chunks are passed to an OpenAI GPT model using LangChain's QA chain to generate a summary.

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/pdf-summarizer.git
cd pdf-summarizer
