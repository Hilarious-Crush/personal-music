from django.shortcuts import render
from .models import Track, Artist, Album, Genre

def index(request):

	tracks = Track.objects.all()

	context = {
		"tracks": tracks

	}

	return render(request, "tracks/index.html", context)
