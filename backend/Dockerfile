# Use Python 3.11-slim as the base image for a smaller footprint
FROM python:3.11-slim

# Install system dependencies for WeasyPrint and related libraries
RUN apt-get update && apt-get install -y \
    libcairo2 \
    libpango-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libglib2.0-0 \
    libffi-dev \
    shared-mime-info \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables to improve Python performance in containers
ENV PYTHONDONTWRITEBYTECODE=1
# Prevents Python from writing .pyc files
ENV PYTHONUNBUFFERED=1
# Ensures Python output is sent straight to terminal

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first to leverage Docker caching
COPY requirements.txt .

# Install Python dependencies using the --break-system-packages flag
RUN pip install --no-cache-dir --break-system-packages -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 8000 (Railway will map $PORT to this container port)
EXPOSE 8000

# Start the FastAPI application using uvicorn, using /bin/sh to enable env var substitution
CMD ["/bin/sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
