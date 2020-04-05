from django.contrib import admin
from .models import Film


# admin.site.register(Film)     # Prostszy sposób

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    # fields = ["tytul", "opis", "rok"]
    # exclude = ["opis"]
    list_display = ["tytul", "imdb_rating", "rok"]
    list_filter = ("rok",)      # Na końcu krotki musi być przecinek!
    search_fields = ('tytul', 'opis')  # Na końcu krotki musi być przecinek!
