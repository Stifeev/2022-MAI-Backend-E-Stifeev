FROM ubuntu:20.04

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update

RUN apt install -y python3 pip

RUN apt install -y libpq-dev
RUN apt install -y postgresql

RUN pip install Django==4 psycopg2

WORKDIR /usr/src/app

RUN mkdir film_project
COPY film_project film_project
COPY script.py .
