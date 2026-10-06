# AI Text Intelligence API

A modular FastAPI service that exposes common NLP inference tasks through REST endpoints using Hugging Face Transformers.

## Capabilities

- Text summarization
- Sentiment analysis
- Zero-shot text classification
- Extractive question answering
- API-key authentication
- Health checking

## Architecture

~~~text
Client
  ↓
FastAPI Router
  ↓
Pydantic Request Validation
  ↓
NLP Service Layer
  ↓
Hugging Face Transformer Pipeline
  ↓
Structured JSON Response
~~~

## Models

The current implementation uses these pretrained Hugging Face models:

| Task | Model |
|---|---|
| Summarization | google/flan-t5-small |
| Sentiment | distilbert-base-uncased-finetuned-sst-2-english |
| Zero-shot classification | facebook/bart-large-mnli |
| Question answering | deepset/roberta-base-squad2 |

Models are loaded when the application imports the model service, so startup and memory usage can be significant.

## Tech Stack

| Component | Technology |
|---|---|
| API | FastAPI |
| NLP | Hugging Face Transformers |
| Deep learning runtime | PyTorch |
| Validation | Pydantic |
| Authentication | API key |
| Server | Uvicorn |
| Containerization | Docker |

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | / | Basic service response |
| GET | /health | Health check |
| POST | /summarize | Summarize text |
| POST | /sentiment | Analyze sentiment |
| POST | /classify | Zero-shot classification |
| POST | /qa | Extract an answer from supplied context |

The inference endpoints require the `X-API-Key` request header.

FastAPI interactive documentation is available at:

~~~text
http://127.0.0.1:8000/docs
~~~

## Example Requests

### Zero-shot classification

~~~json
{
  "text": "The new model improves inference latency.",
  "labels": ["technology", "sports", "finance"]
}
~~~

Send it to `POST /classify` with:

~~~text
X-API-Key: your_secret_key
~~~

### Question answering

~~~json
{
  "context": "FastAPI is a Python framework for building APIs.",
  "question": "What is FastAPI?"
}
~~~

## Project Structure

~~~text
ai-text-intelligent-api/
├── app/
│   ├── api/
│   │   └── routes.py
│   ├── schemas/
│   │   ├── request.py
│   │   └── response.py
│   ├── services/
│   │   ├── classifier.py
│   │   ├── model_loader.py
│   │   ├── qa.py
│   │   ├── sentiment.py
│   │   └── summarizer.py
│   ├── utils/
│   │   └── auth.py
│   └── main.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
~~~

## Run Locally

### 1. Create an environment

~~~bash
python -m venv .venv
~~~

Windows:

~~~powershell
.\.venv\Scripts\Activate.ps1
~~~

### 2. Install dependencies

~~~bash
pip install -r requirements.txt
~~~

### 3. Configure the API key

Set `API_KEY` in your local environment. Do not commit a `.env` file containing a real key.

PowerShell:

~~~powershell
$env:API_KEY="your_secret_key"
~~~

### 4. Start the API

~~~bash
uvicorn app.main:app --reload
~~~

The service runs at `http://127.0.0.1:8000`.

### 5. Docker

Build the image:

~~~bash
docker build -t ai-text-intelligent-api .
~~~

Run it while supplying the API key:

~~~bash
docker run --rm -p 8000:8000 -e API_KEY=your_secret_key ai-text-intelligent-api
~~~

## Engineering Focus

This project demonstrates:

- Designing a modular FastAPI application
- Separating API routes, validation schemas, and inference services
- Serving multiple Transformer pipelines through one REST API
- API-key authentication
- Dockerized application packaging
- Structured response models with Pydantic

## Limitations

- Models are loaded at application startup and can consume significant RAM.
- The summarization and classification models are general-purpose pretrained models.
- Authentication is intentionally simple API-key authentication, not a full identity system.
- No rate limiting or production monitoring is currently included.

## Future Improvements

- Lazy model loading and caching
- Batch inference
- Rate limiting
- Structured logging and monitoring
- Model performance evaluation
- Production deployment

## Author

**Subham Dey**
