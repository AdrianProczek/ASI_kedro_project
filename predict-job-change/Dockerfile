FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

# Wczytaj zmienne środowiskowe z .env
ENV GOOGLE_APPLICATION_CREDENTIALS="gcp-key.json"

# Uruchomienie domyślne
CMD ["kedro", "run"]
