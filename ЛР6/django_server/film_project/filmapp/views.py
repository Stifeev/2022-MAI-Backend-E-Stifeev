from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from filmapp import models
from django.shortcuts import render
import datetime

def index(request):
   return render(request, "index.html", context={"data" : datetime.datetime.now()})

@csrf_exempt # разрешаем делать POST запрос без куки
def film_handler(request):
    if request.method == "GET": # получение фильма по id
        film_id = request.GET.get("id", -1)
        
        try:
            film = models.Film.objects.get(id=film_id)
            return JsonResponse({"id": film.id, "name": film.name, "original_name": film.original_name, "year": film.year})
        except models.Film.DoesNotExist:
            return JsonResponse({})
        
    elif request.method == "POST": # добавление нового фильма
        name = request.GET.get("name", None)
        if not name:
            return JsonResponse({"status": "Bad name param"})
        original_name = request.GET.get("original_name", None)
        year = request.GET.get("year", None)
        
        # Сохраняем в базу данных
        try:
            film = models.Film()
            film.name = name
            film.original_name = original_name
            film.year = year
            
            exists = True
            try:
                _ = models.Film.objects.get(name=name, original_name=original_name, year=year)
            except models.Film.DoesNotExist:
                exists = False
            except models.Film.MultipleObjectsReturned:
                pass
                
            if not exists:
                film.save()
            return JsonResponse({"status": ("OK" if not exists else "Already exists")})
        except:
            return JsonResponse({"status": "Field error"})
    else:
        return HttpResponseBadRequest("<h2>Bad Request</h2>")
