FROM python:3.8-alpine

RUN apk add --update alpine-sdk && apk add libffi-dev openssl-dev

ENV PYTHONUNBUFFERED 1

COPY  ./requirements.txt /requirements.txt

RUN pip3 install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user