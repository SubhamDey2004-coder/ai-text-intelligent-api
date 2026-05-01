FROM python:3.11-slim

WORKDIR /app

# Prevent Python from buffering logs
ENV PYTHONUNBUFFERED=1

# Copy requirements first (cache optimization)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy full project
COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
