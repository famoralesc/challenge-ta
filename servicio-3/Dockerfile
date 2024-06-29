# Dockerfile con la imagen y pasos para dejar funcionando el servicio
# puede ser igual al del servicio-1 y servicio-2

FROM python:3.12.3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

EXPOSE 8080
