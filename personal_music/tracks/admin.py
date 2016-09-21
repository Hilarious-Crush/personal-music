from django.contrib import admin
from .models import Track, Genre, Album, Artist

admin.site.register(Track)
admin.site.register(Genre)
admin.site.register(Album)
admin.site.register(Artist)
