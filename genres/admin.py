from django.views.decorators.csrf import csrf_exempt
from genres.models import Genre
from django.contrib import admin

class GenreAdmin(admin.ModelAdmin):
    list_display = ['name',]
    search_fields = ['name',]

admin.site.register(Genre, GenreAdmin)
