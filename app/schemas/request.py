from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str
    
class ClassificationRequest(BaseModel):
    text: str
    labels: list[str]
    
class QARequest(BaseModel):
    context: str
    question: str