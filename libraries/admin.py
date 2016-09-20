from django.contrib import admin

from .models import Album

# class LibraryAdmin(admin.ModelAdmin):
# 	list_display = ('title', )

class AlbumAdmin(admin.ModelAdmin):
	list_display = ['title',]

	# def track_info(self, obj):
	# 	titles = [tracks.track.title for track in obj.tracks.track.all()]

	# 	return titles

# admin.site.register(Library, LibraryAdmin)
admin.site.register(Album, AlbumAdmin)
