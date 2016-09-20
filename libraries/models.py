from django.db import models

# class Library(models.Model):
# 	name = models.CharField(max_length=50)

# 	def __str__(self):
# 		return self.name

class Album(models.Model):
	title = models.CharField(max_length=200)
	# library = models.ForeignKey('Library')

	def __str__(self):
		return self.title