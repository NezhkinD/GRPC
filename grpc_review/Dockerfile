# server/Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Копируем requirements и устанавливаем
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код сервера (включая helloworld_pb2.py, helloworld_pb2_grpc.py)
COPY . .

CMD [ "python", "server.py" ]
