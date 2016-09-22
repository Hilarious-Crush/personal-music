from django.db import models
from datetime import datetime

class Track(models.Model):
	name = models.CharField(max_length=200)
	artist = models.ManyToManyField('Artist')
	album = models.ManyToManyField('Album')
	date_added = models.DateTimeField(default=datetime.now, blank=True)
	duration = models.IntegerField()
	favorite = models.BooleanField(default=False)
	genre = models.ManyToManyField('Genre')

	def __str__(self):
		return self.name

class Artist(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	group_name = models.CharField(max_length=200)

	def __str__(self):
		return "{} {}".format(self.first_name, self.last_name)

	
class Genre(models.Model):
	genre_name = models.CharField(max_length=200)

	def __str__(self):
		return self.genre_name


class Album(models.Model):
	album_name = models.CharField(max_length=200)

	def __str__(self):
		return self.album_name

