# Dockerfile con la imagen y pasos para dejar funcionando el servicio
# puede ser igual al del servicio-2 y servicio-3

FROM python:3.12.3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python", "service.py"]