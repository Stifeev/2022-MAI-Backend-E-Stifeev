# Описание репозитория

- film_project - Python-исходники для бэкенд-сервера на джанго;
  - filmapp;
    - admin.py       - настройка привилегий администратора;
    - models.py      - модели для базы данных;
    - serializers.py - сериализация модели в json-формат и обратно;
    - tests.py           - тесты;
    - views.py         - обработчики запросов;
  - filmapp_main;
    - settings.py - конфиг;
    - url.py          - логика соответствия запросу обработчика;
  - templates  - исходники шаблонных веб-страниц;
- docker - исходники для запуска сервера nginx в контейнере;
- Обложки - картинки для использования в тестах.

## Запуск

Перез запуском необходимо в файле settings.py указать правильные поля с доступом к БД *postgresSQL*:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'film_base',  # <------

        'USER': 'film_admin', # <------

        'PASSWORD': '567765', # <------

        'HOST': 'localhost',  # <------

        'PORT': '5432',       # <------
    }
}
```

Путь к driver'у для Chrome:

```python
PATH_2_DRIVER = "D:/Program Files/Chrome/chromedriver_102.exe" # <------
```

Параметры доступа к S3-хранилищу:

```python
DEFAULT_FILE_STORAGE =    "storages.backends.s3boto3.S3Boto3Storage"
AWS_ACCESS_KEY_ID =       "Sample_text"      # <------
AWS_SECRET_ACCESS_KEY =   "Sample_text"      # <------
AWS_STORAGE_BUCKET_NAME = "mai-film-project" # <------
AWS_S3_ENDPOINT_URL =     "https://storage.yandexcloud.net"
```

### Сервер Jango

```bash
$ cd film_project
$ python ./manage.py migrate
$ python ./manage.py runserver
```

### Тесты для Jango

```bash
$ cd film_project
$ python ./manage.py test film_app
```

### Сервер nginx

```bash
$ cd docker
$ docker-compose up
```

## Ссылки для веб-интерфейса

- http://localhost:8000/ стартовая страница django
- http://localhost:8000/admin админка django (нужно будет создать аккаунт через консольную оболочку (метод create_superuser))
- http://localhost:80/ стартовая страница nginx

## Ссылки для api

- GET http://localhost:8000/api/director/ вернуть список всех режиссёров в формате массива json
- GET http://localhost:8000/api/film/        вернуть список всех фильмов в формате массива json
- GET http://localhost:8000/api/film/3      вернуть фильм с id = 3
- POST http://localhost:8000/api/film/      добавить фильм
  - В параметрах передать name, original_name, year, cover (в виде бинарного файла-изображения) и directors (в виде массива id). Все параметры опциональны
- PATCH http://localhost:8000/api/film/3 обновить информацию и фильме с id = 3
  - В параметрах передать name, original_name, year, cover (в виде бинарного файла-изображения) и directors (в виде массива id). Все параметры опциональны


## Покрытие тестами

```shell
Name                                    Stmts   Miss  Cover
-----------------------------------------------------------
boto.py                                    26     26     0%
filmapp\__init__.py                         0      0   100%
filmapp\admin.py                           10      0   100%
filmapp\apps.py                             4      0   100%
filmapp\migrations\0001_initial.py          6      0   100%
filmapp\migrations\0002_film_cover.py       4      0   100%
filmapp\migrations\__init__.py              0      0   100%
filmapp\models.py                          27      3    89%
filmapp\serializers.py                     11      0   100%
filmapp\tests.py                          100      4    96%
filmapp\views.py                           81     34    58%
filmapp_main\__init__.py                    0      0   100%
filmapp_main\asgi.py                        4      4     0%
filmapp_main\settings.py                   27      0   100%
filmapp_main\urls.py                       12      0   100%
filmapp_main\wsgi.py                        4      4     0%
manage.py                                  12      2    83%
-----------------------------------------------------------
TOTAL                                     328     77    77%
```

