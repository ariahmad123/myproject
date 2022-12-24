from django.contrib import admin

from .models import *
# Register your models here.

class AnimepopularAdmin(admin.ModelAdmin):
    list_display = ('animeId', 'animeTitle', 'animeImg', 'releasedDate', 'animeUrl')

class DetailanimeAdmin(admin.ModelAdmin):
    list_display = ('animeId','animeTitle', 'type', 'releasedDate', 'status','otherNames', 'synopsis', 'animeImg', 'totalEpisodes')

class TopratedanimeAdmin(admin.ModelAdmin):
    list_display = ('animeId', 'animeTitle', 'animeImg', 'latestEpisode', 'animeUrl')

class MovieAnimeAdmin(admin.ModelAdmin):
    list_display = ('animeId', 'animeTitle', 'animeImg', 'releasedDate', 'animeUrl')

admin.site.register(Animepopular, AnimepopularAdmin)
admin.site.register(Detailanime, DetailanimeAdmin)
admin.site.register(Topratedanime, TopratedanimeAdmin)
admin.site.register(MovieAnime, MovieAnimeAdmin)
