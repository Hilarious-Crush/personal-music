from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .models import Track, Artist, Album, Genre

def index(request):

	tracks = Track.objects.all()

	context = {
		"tracks": tracks
    }

	return render(request, "tracks/index.html", context)

def artist(request):
    return render(request, "tracks/artist.html",  {})

def genre(request):
    
    genres = Genre.objects.all()
    context= {
        "genres": genres
    }

    print(genres)
    return render(request, "tracks/genre.html", context)


def artist_list(request):
    artists = Artist.objects.all()
    context = {
        "artists": artists 
    }

    print(artists)
    return render(request, "tracks/artist_list.html", context)


def artist_page(request, id):
    artist = get_object_or_404(Artist, pk=id)
    tracks = artist.track_set()
    context = {
        "tracks": tracks,
        "artist": artist,

    }

    return render(request, "tracks/artist_page.html", context)
