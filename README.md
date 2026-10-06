# AI Text Intelligence API

A modular FastAPI backend for common NLP inference tasks using Hugging Face Transformers.

## What It Does

The API exposes multiple text-intelligence capabilities behind REST endpoints:

- Text summarization
- Sentiment analysis
- Zero-shot classification
- Extractive question answering
- API-key authentication
- Health checking

## Architecture

```text
Client Request
      ↓
FastAPI Router
      ↓
Request Validation
      ↓
NLP Service
      ↓
Hugging Face Transformer Pipeline
      ↓
Structured JSON Response
```

## Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.11 |
| API | FastAPI |
| NLP models | Hugging Face Transformers |
| Validation | Pydantic |
| Authentication | API key |
| Server | Uvicorn |
| Containerization | Docker |

## API Endpoints

| Endpoint | Purpose |
|---|---|
| `POST /summarize` | Summarize input text |
| `POST /sentiment` | Analyze sentiment |
| `POST /classify` | Zero-shot classification |
| `POST /qa` | Question answering |
| `GET /health` | Health check |

All inference endpoints require the configured API key.

## Project Structure

```text
ai-text-intelligent-api/
├── app/
│   ├── main.py
│   ├── api/
│   ├── services/
│   ├── schemas/
│   └── utils/
├── requirements.txt
├── Dockerfile
├── .env
└── README.md
```

## Run Locally

```bash
python -m venv venv
```

Windows:

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure the API key in the environment:

```env
API_KEY=your_secret_key
```

Start the server:

```bash
uvicorn app.main:app --reload
```

Open the interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

## Example Request

### Zero-shot classification

```json
{
  "text": "The new model improves inference latency.",
  "labels": ["technology", "sports", "finance"]
}
```

## Engineering Notes

Transformer models can require substantial memory and the first request may be slower because model weights need to be loaded.

The project is intentionally structured around reusable model services rather than putting all inference logic inside a single API route.

## Future Improvements

- Model caching and optimized loading
- Rate limiting
- More robust authentication
- Docker deployment optimization
- Monitoring and inference metrics
- Production deployment

## Author

**Subham Dey**
