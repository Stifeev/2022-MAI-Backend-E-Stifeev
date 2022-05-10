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

# COPY pg_hba.conf /etc/postgresql/12/main

# CMD ["sh", "-c", "python3 film_project/manage.py migrate                                    \
#                   && echo \"from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'stifeev99@mail.ru', 'admin')\" | python3 film_project/manage.py shell \
#                   && python3 film_project/manage.py runserver 0.0.0.0:8000"]

# CMD ["sh", "-c", "service postgresql stop                                                      \
#                   && service postgresql start                                                  \
#                   && psql -U postgres -c \"CREATE USER IF NOT EXISTS film_admin WITH password '567765'\"     \
#                   && psql -U postgres -c \"CREATE DATABASE IF NOT EXISTS film_base OWNER film_admin\"        \
#                   && python3 film_project/manage.py migrate                                    \
#                   && echo \"from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'stifeev99@mail.ru', 'admin')\" | python3 film_project/manage.py shell \
#                   && python3 film_project/manage.py runserver 0.0.0.0:8000"]

#CMD ["sh", "-c", "service postgresql start && python3 film_project/manage.py runserver 0.0.0.0:8000"]

# RUN apt install -y tree

# CMD ["tree"]
