FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/etl_ratings.py .
COPY data ./data

CMD ["python", "etl_ratings.py"]