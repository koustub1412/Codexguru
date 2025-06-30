# 🧠 CodexGuru

CodexGuru is a full-stack AI-powered tool that helps developers **summarize** and **debug** code instantly using cutting-edge LLMs like **Mistral** and **LLaMA**. It provides an intuitive interface where users can paste code, get AI-generated summaries, detect bugs, and view analysis history securely.

---

## 🚀 Features

- 🔍 **Code Summarization** using Mistral-7B via OpenRouter API
- 🛠️ **Bug Detection** with LLaMA and DeepSeek Coder APIs
- 🔐 **JWT-based Authentication** for secure login/register
- 🧾 **History Tracking** for past code analyses
- 🌐 **Modern UI** with React + Material UI
- ⚡ Fast backend using FastAPI and MongoDB

---

## 🧩 Tech Stack

| Layer     | Technology           |
|-----------|----------------------|
| Frontend  | React, Material UI   |
| Backend   | FastAPI (Python)     |
| AI Models | Mistral, LLaMA       |
| Auth      | JWT Token Auth       |
| Database  | MongoDB              |
| Hosting   | GitHub (codebase)    |

---

## 📁 Folder Structure

```plaintext
Codexguru/
├── backend/                   # FastAPI backend
│   ├── app/
│   │   ├── main.py
│   │   ├── routes/
│   │   │   ├── analyze.py
│   │   │   └── debug.py
│   │   ├── services/
│   │   │   ├── mistral_7b.py
│   │   │   ├── llama_3_8b.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── test.py
│   └── requirements.txt
│
├── frontend/                  # React frontend
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── App.js
│   │   └── index.js
│   ├── .env
│   └── package.json
│
├── .gitignore
├── README.md

```

---

## 🔧 Setup Instructions

### 🐍 Backend (FastAPI)

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 🌐 Frontend (React)
```bash
cd frontend
npm install
npm start
```
🔐 Add .env files as needed for API keys

👥 Contributors
@koustub1412
@RIGVED0
