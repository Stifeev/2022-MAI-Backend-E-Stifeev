# Описание репозитория

- film_project Python-исходники для бэкенд-сервера на джанго;
  - filmapp;
    - models.py - модели для базы данных;
    - views.py     - обработчики запросов
  - filmapp_main;
    - settings.py - конфиг;
    - url.py          - логика соответствия запросу обработчика.

Реализовано отношение "многие ко многим" через промежуточную таблицу.

```shell
film_base-> \dt
```

Список отношений

| Схема  |            Имя             |   Тип   |  Владелец
| ---- | ---- | ---- | ---- |
| public | auth_group                 | таблица | film_admin
| public | auth_group_permissions     | таблица | film_admin
| public | auth_permission            | таблица | film_admin
| public | auth_user                  | таблица | film_admin
| public | auth_user_groups           | таблица | film_admin
| public | auth_user_user_permissions | таблица | film_admin
| public | django_admin_log           | таблица | film_admin
| public | django_content_type        | таблица | film_admin
| public | django_migrations          | таблица | film_admin
| public | django_session             | таблица | film_admin
| public | filmapp_director           | таблица | film_admin
| public | filmapp_film               | таблица | film_admin
| public | filmapp_filmdirector       | таблица | film_admin

(13 строк)

```shell
film_base-> \d filmapp_film
```

Таблица "public.filmapp_film"

| Столбец |          Тип           | Правило сортировки | Допустимость NULL |  По умолчанию
| ---- | ---- | ---- | ---- | ---- |
| id      | bigint                 |                    | not null          | nextval('filmapp_film_id_seq'::regclass)
| name    | character varying(100) |                    | not null   |
| date    | integer                |                    |            |

Индексы:

​	"filmapp_film_pkey" PRIMARY KEY, btree (id)

Ссылки извне:

TABLE "filmapp_filmdirector" CONSTRAINT "filmapp_filmdirector_film_id_ab6d1d93_fk_filmapp_film_id" FOREIGN KEY (film_id) REFERENCES filmapp_film(id) DEFERRABLE INITIALLY DEFERRED

```shell
film_base-> \d filmapp_director
```

​                                            Таблица "public.filmapp_director"

| Столбец |          Тип           | Правило сортировки | Допустимость NULL |  По умолчанию
| ---- | ---- | ---- | ---- | ---- |
 id      | bigint                 |                    | not null          | nextval('filmapp_director_id_seq'::regclass)
 name    | character varying(100) |                    | not null          |
 year    | integer                |                    |                   |

Индексы:

​	"filmapp_director_pkey" PRIMARY KEY, btree (id)

Ссылки извне:

TABLE "filmapp_filmdirector" CONSTRAINT "filmapp_filmdirector_director_id_6fb624db_fk_filmapp_d" FOREIGN KEY (director_id) REFERENCES filmapp_director(id) DEFERRABLE INITIALLY DEFERRED

```shell
film_base-> \d filmapp_filmdirector
```

Таблица "public.filmapp_filmdirector"

| Столбец   |  Тип   | Правило сортировки | Допустимость NULL |                   По умолчанию
| ---- | ---- | ---- | ---- | ---- |
 id          | bigint |                    | not null          | nextval('filmapp_filmdirector_id_seq'::regclass)
 director_id | bigint |                    |                   |
 film_id     | bigint |                    |                   |

Индексы:
    "filmapp_filmdirector_pkey" PRIMARY KEY, btree (id)
    "filmapp_filmdirector_director_id_6fb624db" btree (director_id)
    "filmapp_filmdirector_film_id_ab6d1d93" btree (film_id)
Ограничения внешнего ключа:
    "filmapp_filmdirector_director_id_6fb624db_fk_filmapp_d" FOREIGN KEY (director_id) REFERENCES

​      filmapp_director(id) DEFERRABLE INITIALLY DEFERRED

​    "filmapp_filmdirector_film_id_ab6d1d93_fk_filmapp_film_id" FOREIGN KEY (film_id) REFERENCES

​     filmapp_film(id) DEFERRABLE INITIALLY DEFERRED
