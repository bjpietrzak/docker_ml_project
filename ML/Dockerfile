FROM python:3.9

WORKDIR /app

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y


COPY ./requirements.txt /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt
