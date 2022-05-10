# Описание репозитория

- django_server - исходники для веб-сервера django в контейнере;
  - film_project Python-исходники для бэкенд-сервера на джанго;
    - filmapp;
      - admin.py    - настройка привилегий администратора;
      - models.py  - модели для базы данных;
      - views.py     - обработчики запросов.

    - filmapp_main;
      - settings.py - конфиг;
      - url.py          - логика соответствия запросу обработчика.

- nginx - исходники для веб-сервера nginx в контейнере;
- postgreSQL - исходники для базы данных в контейнере.

## Запуск

```bash
$ docker-compose build
$ docker-compose up
```

## Ссылки для веб-интерфейса

- http://localhost/ стартовая страница nginx
- http://localhost/public/index.html отдача статики с nginx
- http://localhost/jango/ переход с nginx на django (upstream)
- http://localhost:8000/ прямая ссылка на django
- http://localhost:8000/admin/login/?next=/admin/ админка django (username: admin, password: admin)
