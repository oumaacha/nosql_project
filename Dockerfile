FROM python:3.12

ENV PYTHONUNBUFFERED=1

RUN pip install minio pika pymongo

COPY ./src/1_rabbit_to_minio.py ./

ENTRYPOINT python -u 1_rabbit_to_minio.py