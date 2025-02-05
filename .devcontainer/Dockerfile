# Minimal Docker setup
FROM python:3.10-slim

# Install WeasyPrint system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libcairo2 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set up working directory
WORKDIR /workspace

# Pre-install Python dependencies (layer caching)
COPY ../../backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
