from re import template
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
import requests
from django.contrib.auth import authenticate, login, logout

def homePage(request):
    template_name = "homepage.html"
    return render(request, template_name)

def loginPage(request):
    template_name = "login.html"
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

    return render(request, template_name)

def popularanime(request):
    url = 'https://gogoanime.consumet.org/popular'
    populars = requests.get(url)
    data_populars = populars.json()
    template_name = "popularanime.html"
    context = {'data_populars':data_populars}
    return render(request, template_name, context)

def detailanime(request, animeId):
    url = f'https://gogoanime.consumet.org/anime-details/{animeId}'
    details = requests.get(url)
    data_details = details.json()
    template_name = "detailanime.html"
    context = {'data_details' :data_details}
    return render (request , template_name, context)


def topratedanime(request):
    url = f'https://gogoanime.consumet.org/top-airing'
    toprateds = requests.get(url)
    data_toprateds = toprateds.json()
    template_name = "topratedanime.html"
    context = {'data_toprateds' :data_toprateds}
    return render (request , template_name, context)

def movieanime(request):
    url = 'https://gogoanime.consumet.org/anime-movies'
    movies = requests.get(url)
    data_movies = movies.json()
    template_name = "animemovie.html"
    context = {'data_movies':data_movies}
    return render(request, template_name, context)

def contact(request):
    template_name = "contact.html"
    context = {}
    return render(request, template_name, context)

