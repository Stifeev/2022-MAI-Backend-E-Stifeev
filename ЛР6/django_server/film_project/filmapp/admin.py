from django.contrib import admin
from filmapp.models import Director, Film

class FilmAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "year")
    list_filter = ("year",)
    
class DirectorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "year")
    list_filter = ("year",)
    
admin.site.register(Film, FilmAdmin)
admin.site.register(Director, DirectorAdmin)
