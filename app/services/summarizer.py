from app.services.model_loader import summarizer


def summarize_text(text: str):
    cleaned_text = text.strip()

    if not cleaned_text:
        return "Empty input"

    if len(cleaned_text.split()) < 10:
        return cleaned_text

    prompt = f"summarize in 1 short sentence: {cleaned_text}"

    try:
        result = summarizer(prompt)
        return result[0]["summary_text"]
    except Exception:
        return "Unable to generate a summary."
