FROM python:3.7.2-slim-stretch

WORKDIR /api
ADD . /api

RUN pip install -r requirements_dev.txt
