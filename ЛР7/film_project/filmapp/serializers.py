# -*- coding: utf-8 -*-

from filmapp.models import Director, Film
from rest_framework import serializers

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ["id", "name", "year"]

class FilmSerializer(serializers.ModelSerializer):
    directors = serializers.StringRelatedField(many=True)
    class Meta:
        model = Film
        fields = ["id", "name", "original_name", "year", "directors"]