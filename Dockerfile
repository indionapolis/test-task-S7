FROM python:3.7

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y python python-pip
RUN pip3 install --cache-dir=/cache -r requirements.txt

COPY . .

ENV API_HOST=0.0.0.0
ENV API_PORT=8000

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

ENTRYPOINT uvicorn src.app:app --host $API_HOST --port $API_PORT
