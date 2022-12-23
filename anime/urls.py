from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("dashboard", include('series.urls')),
    path("", homePage, name='home'),
    path("popular-anime/", popularanime, name='popularanime'),
    path("login/", loginPage, name='login'),
    path("detail-anime/<str:animeId>", detailanime, name='detailanime'),
    path("toprated-anime/", topratedanime, name='topratedanime'),
    path("movie-anime/", movieanime, name='movieanime'),
    path("contact/", contact, name='contact'),

]