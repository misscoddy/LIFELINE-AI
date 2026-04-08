# Dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt uvicorn fastapi

# Run FastAPI server
CMD ["python", "inference.py"]
