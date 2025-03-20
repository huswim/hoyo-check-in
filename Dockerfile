FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1

ENV LTOKEN_V2=""
ENV LTUID_V2=""

RUN pip install --no-cache-dir requests

WORKDIR /app
COPY src /app

ENTRYPOINT [ "python3", "main.py" ]