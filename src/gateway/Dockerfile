FROM python:3.8-slim-buster

RUN apt-get update \
      && apt-get install -y --no-install-recommends --no-install-suggests \
      build-essential \
      && pip install --no-cache-dir --upgrade pip

WORKDIR /app
COPY ./requirements.txt /app
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY . /app 

EXPOSE 8002

CMD ["python3", "server.py"]
