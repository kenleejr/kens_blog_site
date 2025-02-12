FROM python:3.12.8-slim
EXPOSE 8080
WORKDIR /app

COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src .
COPY markdown /app/markdown

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]