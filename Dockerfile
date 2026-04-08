# Dockerfile
# -------------------------
# Phase 1 safe Dockerfile for OpenEnv
# -------------------------

# Base Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy only necessary files for Phase 1
COPY inference.py /app
COPY requirements.txt /app

# Upgrade pip
RUN python -m pip install --upgrade pip

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose FastAPI default port
EXPOSE 8000

# Run FastAPI app for Phase 1
CMD ["uvicorn", "inference:app", "--host", "0.0.0.0", "--port", "8000"]
