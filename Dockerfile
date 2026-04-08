FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Start uvicorn server so container stays alive
CMD ["uvicorn", "inference:app", "--host", "0.0.0.0", "--port", "8080"]
