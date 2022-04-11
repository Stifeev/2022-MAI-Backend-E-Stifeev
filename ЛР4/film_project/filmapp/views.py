from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

def index(request):
    http = \
    """
    <html lang="ru">
    <head>
        <title>Веб-сервер</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" /></meta>
    </head>
    <body>
        <h1>Приветствую на бэкенд-сервере Jango!</h1>
        <p>Сделайте запрос</p>
    </html>
    """
    return HttpResponse(http)

@csrf_exempt # разрешаем делать POST запрос без куки
def products(request):
    if request.method == "GET":
        film_id = request.GET.get("film_id", 666)
        name = request.GET.get("name", "Самый лучший фильм")
        genre = request.GET.get("genre", "Ужасы")
        return JsonResponse({"film_id": film_id, "name": name, "genre": genre})
    elif request.method == "POST":
        film_id = request.GET.get("film_id", 888)
        name = request.GET.get("name", "Как я встретил вашу маму")
        genre = request.GET.get("genre", "Комедия")
        # Сохраняем в базу данных
        return JsonResponse({"film_id": film_id, "status": "OK"})
    else:
        return HttpResponseBadRequest("<h2>Bad Request</h2>")
