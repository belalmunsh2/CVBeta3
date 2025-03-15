# Use Python 3.11-slim as the base image for a smaller footprint
FROM python:3.11-slim

# Set environment variables to improve Python performance in containers
ENV PYTHONDONTWRITEBYTECODE=1  # Prevents Python from writing .pyc files
ENV PYTHONUNBUFFERED=1         # Ensures Python output is sent straight to terminal

# Set the working directory inside the container
WORKDIR /app

# Copy requirements file first to leverage Docker caching
COPY requirements.txt .

# Install dependencies
# Using --break-system-packages flag to handle externally managed environment in Python 3.11
RUN pip install --no-cache-dir --break-system-packages -r requirements.txt

# Copy the rest of the application code
# This is done after installing dependencies to leverage Docker's layer caching
COPY . .

# Expose the port that will be used by the application
# Railway will set the $PORT environment variable dynamically
EXPOSE ${PORT:-8000}

# Start the FastAPI application using uvicorn
# The CMD instruction is used as it allows for command line overrides
# We use shell form to ensure environment variable substitution works correctly
CMD uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}
