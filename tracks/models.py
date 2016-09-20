from django.db import models

class Track(models.Model):
	title = models.CharField(max_length=100)
	album = models.ForeignKey('libraries.Album', null=True, blank=True)
	artists = models.ManyToManyField('Artist', blank=True)
	genres = models.ManyToManyField('Genre', blank=True)
	track_number = models.CharField(max_length=10, null=True, blank=True)

	def __str__(self):
		return self.title

class Artist(models.Model):
	artist_name = models.CharField(max_length=50)

	def __str__(self):
		return self.artist_name

class Genre(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name
