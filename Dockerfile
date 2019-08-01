FROM python:3.6-alpine
RUN apk add --update gcc postgresql-dev musl-dev zlib-dev nodejs nodejs-npm jpeg-dev libpng-dev
COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt
