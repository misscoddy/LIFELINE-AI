FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Run FastAPI server continuously
CMD ["uvicorn", "inference:app", "--host", "0.0.0.0", "--port", "80"]
