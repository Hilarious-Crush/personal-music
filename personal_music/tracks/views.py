from django.shortcuts import render
from django.core.urlresolvers import reverse
from .models import Track, Artist, Album, Genre

def index(request):

	tracks = Track.objects.all()

	context = {
		"tracks": tracks
    }

	return render(request, "tracks/index.html", context)

def artist(request):
    return render(request, "tracks/artist.html", {})

def genre(request):
    return render(request, "tracks/genre.html", {})

def artist_list(request):
    artists = Artist.objects.all()
    context = {
        "artists": artists 
    }

    print(artists)
    return render(request, "tracks/artist_list.html", context)
