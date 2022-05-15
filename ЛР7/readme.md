# Описание репозитория

- django_server - исходники для веб-сервера django;
  - film_project Python-исходники для бэкенд-сервера на джанго;
    - filmapp;
      - admin.py       - настройка привилегий администратора;
      - models.py      - модели для базы данных;
      - serializers.py - сериализация модели в json-формат и обратно
      - views.py         - обработчики запросов.
      
    - filmapp_main;
      - settings.py - конфиг;
      - url.py          - логика соответствия запросу обработчика.

## Запуск

```bash
$ cd film_project
$ python ./manage.py runserver
```

## Ссылки для веб-интерфейса

- http://localhost:8000/ стартовая страница django
- http://localhost:8000/admin админка django (username: admin, password: admin)

## Ссылки для api

- GET http://localhost:8000/api/director/ вернуть список всех режиссёров в формате массива json
- GET http://localhost:8000/api/film/3      вернуть фильм с id = 3
- POST http://localhost:8000/api/film/      добавить фильм
  - В параметрах передать name, original_name и year
