FROM python:3.11.8-alpine3.19

WORKDIR /app

COPY . /app
COPY .env /app/.env

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]