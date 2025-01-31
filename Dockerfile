# Use the official Python image from the Docker Hub
FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["python", "app.py"]