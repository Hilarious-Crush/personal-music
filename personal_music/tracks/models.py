from django.db import models
from django.core.urlresolvers import reverse
from datetime import datetime

class Track(models.Model):
	name = models.CharField(max_length=200)
	artist = models.ManyToManyField('Artist')
	album = models.ManyToManyField('Album')
	date_added = models.DateTimeField(default=datetime.now, blank=True)
	duration = models.IntegerField()
	favorite = models.BooleanField(default=False)
	genre = models.ForeignKey('Genre')

	def get_album_name(self):
		album_names = [album.album_name for album in self.album.all()]
		return ", ".join(album_names)

	def __str__(self):
		return self.name

	def get_artist_names(self):
		artist_names = [artist.first_name for artist in self.artist.all()]
		return ", ".join(artist_names)



class Artist(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	group_name = models.CharField(max_length=200)

	def __str__(self):
		return "{} {}".format(self.first_name, self.last_name)

	def get_absolute_url(self):
		return reverse('tracks:artist_page', kwargs={'id': self.pk})

	
class Genre(models.Model):
	genre_name = models.CharField(max_length=200)


	def __str__(self):
		return self.genre_name

	def get_absolute_url(self):
		return reverse('tracks:genre_page', kwargs={'id': self.pk})


class Album(models.Model):
	album_name = models.CharField(max_length=200)

	def __str__(self):
		return self.album_name

