FROM python:3.9.20-slim

RUN apt update && apt upgrade -y

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install dirigera

COPY . .

ENTRYPOINT ["python", "./listener.py"]
