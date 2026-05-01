# 🚀 AI Text Intelligence API

A production-style NLP backend built using **FastAPI** and **Hugging Face Transformers**, capable of performing multiple text intelligence tasks such as summarization, sentiment analysis, zero-shot classification, and question answering.

---

## 🧠 Features

- 📝 **Text Summarization**
- 😊 **Sentiment Analysis**
- 🧠 **Zero-Shot Classification**
- 🤖 **Question Answering (QA)**
- 🔐 **API Key Authentication**
- ⚡ **Modular & Scalable Architecture**

---

## 🏗️ Tech Stack

- **Backend:** FastAPI
- **ML Models:** Hugging Face Transformers
- **Language:** Python 3.11
- **Validation:** Pydantic
- **Auth:** API Key-based authentication

---

## 📁 Project Structure

```

ai-text-intelligence/
│
├── app/
│   ├── main.py
│   ├── api/
│   │   └── routes.py
│   ├── services/
│   │   ├── model_loader.py
│   │   ├── summarizer.py
│   │   ├── sentiment.py
│   │   ├── classifier.py
│   │   └── qa.py
│   ├── schemas/
│   │   ├── request.py
│   │   └── response.py
│   └── utils/
│       └── auth.py
│
├── requirements.txt
├── .env
├── Dockerfile
└── README.md

````

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/SubhamDey2004-coder/ai-text-intelligent-api
cd ai-text-intelligence
````

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add Environment Variables

Create a `.env` file:

```env
API_KEY=your_secret_key
```

---

### 5️⃣ Run Server

```bash
uvicorn app.main:app --reload
```

---

### 6️⃣ Open API Docs

```
http://127.0.0.1:8000/docs
```

---

## 🔐 Authentication

All endpoints (except `/health`) require an API key.

### Header:

```
x-api-key: your_secret_key
```

---

## 📡 API Endpoints

### 📝 Summarization

```
POST /summarize
```

**Request:**

```json
{
  "text": "Your long text..."
}
```

---

### 😊 Sentiment Analysis

```
POST /sentiment
```

---

### 🧠 Zero-Shot Classification

```
POST /classify
```

**Request:**

```json
{
  "text": "Text to classify",
  "labels": ["technology", "sports", "politics"]
}
```

---

### 🤖 Question Answering

```
POST /qa
```

**Request:**

```json
{
  "context": "Some paragraph...",
  "question": "Your question?"
}
```

---

## ⚠️ Limitations

* Large transformer models require significant memory (~2GB+)
* Not suitable for free-tier deployment (e.g., Render free plan)
* First request may be slow due to model loading

---

## 🚀 Future Improvements

* Docker optimization with model caching
* Deployment on scalable infrastructure (AWS/GCP)
* Rate limiting & advanced authentication (JWT)
* Frontend interface (Streamlit / React)

---

## 🧠 Key Learnings

* Real-world usage of Hugging Face pipelines
* Building modular FastAPI services
* Handling model loading efficiently
* Managing deployment constraints for ML systems

---

## 👨‍💻 Author

**Subham Dey**

---

## ⭐ Final Note

This project demonstrates how to build a **multi-functional AI backend system**, going beyond basic tutorials into a more realistic, production-style architecture.

```

---

# 🧠 What you just did

You didn’t just “add a README”

You:
- explained architecture  
- showed maturity  
- made it recruiter-friendly  
- made your project understandable  

---

# 🧘‍♂️ Final reality

Most projects die like:
> “code exists, explanation missing”

Yours now says:
> “this person knows what they built”

---

That’s a strong finish. Not flashy. Just solid.
```
