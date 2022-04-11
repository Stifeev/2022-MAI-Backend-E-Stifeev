from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy

def validate_positive(value):
    if value < 0:
        raise ValidationError(gettext_lazy("%d < 0" % value))

class Film(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    date = models.IntegerField(null=True, validators=[validate_positive])
    
class Director(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    year = models.IntegerField(null=True, validators=[validate_positive]) # год рождения
    
class FilmDirector(models.Model):
    film = models.ForeignKey(Film, null=True, on_delete = models.SET_NULL)
    director = models.ForeignKey(Director, null=True, on_delete = models.SET_NULL)