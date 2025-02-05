FROM python:3.10-slim

RUN apt-get update && apt-get install -y curl \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs build-essential

RUN apt-get update && apt-get install -y git

WORKDIR /workspace

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY frontend/ ./frontend/
RUN cd frontend && npm install

COPY . .

CMD ["python", "backend/app.py"]
