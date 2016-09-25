from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .models import Track, Artist, Album, Genre

def index(request):

	tracks = Track.objects.all()

	context = {
		"tracks": tracks
    }

	return render(request, "tracks/index.html", context)


def artist_list(request):
    artists = Artist.objects.all()
    context = {
        "artists": artists 
    }

    return render(request, "tracks/artist_list.html", context)

def genre_list(request):
    genres = Genre.objects.all()
    context = {
        "genres": genres 
    }

    return render(request, "tracks/genre_list.html", context)


def artist_page(request, id):
    artist = get_object_or_404(Artist, pk=id)
    tracks = artist.track_set.all()


    context = {
        "artist": artist,
        "tracks": tracks, 
    }

    return render(request, "tracks/artist_page.html", context)

def genre_page(request, id):
    genre = get_object_or_404(Genre, pk=id)
    tracks = genre.track_set.all()


    context = {
        "genre": genre,
        "tracks": tracks, 
    }

    return render(request, "tracks/genre_page.html", context)


