# Dockerfile at repo root
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command to run inference.py
CMD ["python", "inference.py"]
