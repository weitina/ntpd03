# Laboratorium 04: Docker i konteneryzacja modelu ML

## Instrukcja uruchamiania aplikacji

### 1. Lokalnie
* Zainstaluj zależności: `pip install -r requirements.txt` [cite: 10]
* Uruchom aplikację: `python app.py` 

### 2. Za pomocą Dockera
* Zbuduj obraz: `docker build -t ml-model-lab .` 
* Uruchom kontener: `docker run -d -p 8000:8000 --name ml-container ml-model-lab` 

### 3. Za pomocą Docker Compose
* Uruchom serwis aplikacji i bazy danych: `docker-compose up -d` 

## Parametry i zasoby
* Zasoby: Obraz bazowy `python:3.9-slim`, ok. 200MB RAM
* Endpointy: POST `/predict` (predykcja), GET `/health` (status)