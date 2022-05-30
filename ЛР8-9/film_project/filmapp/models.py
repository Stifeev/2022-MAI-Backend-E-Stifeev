from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy

def validate_positive(value):
    if value < 0:
        raise ValidationError(gettext_lazy("%d < 0" % value))

class Director(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, 
                            verbose_name="Имя и фамилия",
                            help_text="Полное имя и фамилия режиссёра")
    year = models.IntegerField(null=True, validators=[validate_positive],
                               verbose_name="Год рождения",
                               help_text="Год рождения режиссёра")
    
    class Meta:
        verbose_name = "Режиссёр"
        verbose_name_plural = "Режиссёры"
        ordering = ("name", "-year")
    
    def __str__(self):
        return self.name + (", " + str(self.year) if self.year else "")

class Film(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False,
                            verbose_name="Название",
                            help_text="Название на русском языке")
    original_name = models.CharField(max_length=100, blank=True, null=True,
                                     verbose_name="Оригинальное название",
                                     help_text="Оригинальное название, данное при создании")
    year = models.IntegerField(null=True, validators=[validate_positive],
                               verbose_name="Год",
                               help_text="Год создания фильма")
    cover = models.ImageField(upload_to="films_cover/", blank=True, null=True,
                              verbose_name="Обложка фильма",
                              help_text="Обложка фильма. Может быть как на языке оригинала, так и русская адаптированная")
    
    directors = models.ManyToManyField(Director)
    
    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
        ordering = ("name", "-year", "original_name")
    
    def __str__(self):
        return self.name + (", " + str(self.year) if self.year else "")
