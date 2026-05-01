from app.services.model_loader import summarizer

def summarize_text(text: str):
    try:
        if not text.strip():
            return "Empty input"
        if len(text.split()) < 10:
            return text
        
        prompt = f"summarize in 1 short sentence: {text}"
        result = summarizer(prompt)
        
        return result[0]["summary_text"]
    except Exception as e:
        return f"Error: {str(e)}"