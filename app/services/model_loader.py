from transformers import pipeline

summarizer = pipeline("summarization", model="google/flan-t5-small")

sentiment = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

qa = pipeline(
    "question-answering",
    model="deepset/roberta-base-squad2"
)