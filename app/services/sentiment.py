from app.services.model_loader import sentiment

def analyze_sentiment(text: str):
    result = sentiment(text)
    return {
        "label": result[0]["label"],
        "score": float(result[0]["score"])
    }