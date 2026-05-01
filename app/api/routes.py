from fastapi import APIRouter, Depends
from app.utils.auth import verify_api_key
from app.services.summarizer import summarize_text
from app.schemas.request import TextRequest
from app.schemas.response import SummaryResponse
from app.services.sentiment import analyze_sentiment
from app.schemas.response import SentimentResponse
from app.services.classifier import classify_text
from app.schemas.request import ClassificationRequest
from app.schemas.response import ClassificationResponse
from app.services.qa import answer_question
from app.schemas.request import QARequest
from app.schemas.response import QAResponse

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "OK"}

@router.post("/summarize", response_model=SummaryResponse)
def summarize(request: TextRequest, api_key: str = Depends(verify_api_key)):
    summary = summarize_text(request.text)
    return {"summary": summary}

@router.post("/sentiment", response_model=SentimentResponse)
def sentiment(request: TextRequest, api_key: str = Depends(verify_api_key)):
    return analyze_sentiment(request.text)

@router.post("/classify", response_model=ClassificationResponse)
def classify(request: ClassificationRequest, api_key: str = Depends(verify_api_key)):
    return classify_text(request.text, request.labels)

@router.post("/qa", response_model=QAResponse)
def qa(request: QARequest, api_key: str = Depends(verify_api_key)):
    return answer_question(request.context, request.question)