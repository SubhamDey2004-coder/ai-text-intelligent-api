from app.services.model_loader import classifier

def classify_text(text: str, labels: list):
    result = classifier(text, candidate_labels=labels)
    
    return {
        "label": result["labels"][0],
        "score": float(result["scores"][0])
    }