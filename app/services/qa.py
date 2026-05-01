from app.services.model_loader import qa

def answer_question(context: str, question: str):
    result = qa(question=question, context=context)
    
    return {
        "answer": result["answer"],
        "score": float(result["score"])
    }