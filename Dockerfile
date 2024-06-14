FROM python:3.11-slim
WORKDIR /app
COPY length.py /app
CMD ["python", "./length.py", "/app"]
