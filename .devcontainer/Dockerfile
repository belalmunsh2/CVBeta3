FROM python:3.10-slim

WORKDIR /app

COPY .devcontainer/requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

CMD ["python", "backend/app.py"]
