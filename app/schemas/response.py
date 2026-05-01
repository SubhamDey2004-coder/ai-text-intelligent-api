from pydantic import BaseModel

class SummaryResponse(BaseModel):
    summary: str
    
class SentimentResponse(BaseModel):
    label: str
    score: float
    
class ClassificationResponse(BaseModel):
    label: str
    score: float
    
class QAResponse(BaseModel):
    answer: str
    score: float