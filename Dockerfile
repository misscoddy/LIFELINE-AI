# Use Python 3.9 slim
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . /app

# Upgrade pip and install dependencies
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Run FastAPI app via uvicorn (Phase 1 compatible)
CMD ["uvicorn", "inference:app", "--host", "0.0.0.0", "--port", "8000"]
