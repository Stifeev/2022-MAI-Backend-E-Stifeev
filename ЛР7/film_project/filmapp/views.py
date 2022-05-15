from django.shortcuts import render, get_object_or_404

from filmapp.models import Director, Film
from filmapp.serializers  import DirectorSerializer, FilmSerializer

from rest_framework import status, viewsets
from rest_framework.response import Response

import datetime

def index(request):
   return render(request, "index.html", context={"data" : datetime.datetime.now()})

class DirectorViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Director.objects.all()
        serializer = DirectorSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = DirectorSerializer(data=request.data)
        
        if serializer.is_valid():
            director = Director()
            director.name = serializer.validated_data["name"]
            director.year = serializer.validated_data["year"]
            director.save()
            return Response({"status": "OK"})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        queryset = Director.objects.all() # помним про lazy-логику
        
        director = None
        try:
            director = get_object_or_404(queryset, pk=pk)
        except:
            pass
        serializer = DirectorSerializer(director)
        return Response(serializer.data)
    
class FilmViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Film.objects.all()
        serializer = FilmSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = FilmSerializer(data=request.data)
        
        if serializer.is_valid():
            film = Film()
            film.name = serializer.validated_data["name"]
            film.year = serializer.validated_data["year"]
            film.original_name = serializer.validated_data["original_name"]
            film.save()
            return Response({"status": "OK"})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        queryset = Film.objects.all() # помним про lazy-логику
        
        film = None
        try:
            film = get_object_or_404(queryset, pk=pk)
        except:
            pass
        serializer = FilmSerializer(film)
        return Response(serializer.data)


