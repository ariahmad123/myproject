from re import template
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
import requests
from series.models import *
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
    data_populars = Animepopular.objects.all()
    URL = 'https://gogoanime.consumet.org/popular'
    r = requests.get(URL)
    data = r.json()
    for i in data:
        popular_cek = Animepopular.objects.filter(animeId=i['animeId'])
        if popular_cek.exists():
            pop = popular_cek.first()
            pop.animeTitle = i['animeTitle']
            pop.animeImg = i['animeImg']
            pop.releasedDate = i['releasedDate']
            pop.animeUrl = i['animeUrl']
        else:
            Animepopular.objects.create(
                animeId=i['animeId'],
                animeTitle=i['animeTitle'],
                animeImg=i['animeImg'],
                releasedDate=i['releasedDate'],
                animeUrl=i['animeUrl']
            )
    context = {
        'data':data,
        'data_populars':data_populars
        }
    template_name = "popularanime.html"
    return render(request, template_name, context)

def detailanime(request, animeId):
    URL = f'https://gogoanime.consumet.org/anime-details/{animeId}'
    r = requests.get(URL)
    data = r.json()
    detail_cek = Detailanime.objects.filter(animeTitle=data['animeTitle'])
    if detail_cek.exists():
        det = detail_cek.first()
        det.animeTitle = data['animeTitle']
        det.type = data['type']
        det.releasedDate = data['releasedDate']
        det.status = data['status']
        det.otherNames = data['otherNames']
        det.synopsis = data['synopsis']
        det.animeImg = data['animeImg']
        det.totalEpisodes = data['totalEpisodes']
    else:
        Detailanime.objects.create(
            animeId=animeId,
            animeTitle=data['animeTitle'],
            type=data['type'],
            releasedDate=data['releasedDate'],
            status=data['status'],
            otherNames=data['otherNames'],
            synopsis=data['synopsis'],
            animeImg=data['animeImg'],
            totalEpisodes=data['totalEpisodes']
        )
    data_details = Detailanime.objects.get(animeId=animeId)
    context = {
        'data':data,
        'data_details': data_details
        }
    
    template_name = "detailanime.html"
    return render(request, template_name, context)
    
    # url = f'https://gogoanime.consumet.org/anime-details/{animeId}'
    # details = requests.get(url)
    # data_details = details.json()
    # template_name = "detailanime.html"
    # context = {'data_details' :data_details}
    # return render (request , template_name, context)


def topratedanime(request):
    data_toprateds = Topratedanime.objects.all()
    URL = 'https://gogoanime.consumet.org/top-airing'
    r = requests.get(URL)
    data = r.json()
    for i in data:
        toprated_cek = Topratedanime.objects.filter(animeId=i['animeId'])
        if toprated_cek.exists():
            top = toprated_cek.first()
            top.animeTitle = i['animeTitle']
            top.animeImg = i['animeImg']
            top.latestEpisode = i['latestEp']
            top.animeUrl = i['animeUrl']
        else:
            Topratedanime.objects.create(
                animeId=i['animeId'],
                animeTitle=i['animeTitle'],
                animeImg=i['animeImg'],
                latestEpisode=i['latestEp'],
                animeUrl=i['animeUrl']
            )
    context = {
        'data_toprateds1':data,
        'data_toprateds':data_toprateds
        
        }
    template_name = "topratedanime.html"
    return render(request, template_name, context)

def movieanime(request):
    data_movies = MovieAnime.objects.all()
    URL = 'https://gogoanime.consumet.org/anime-movies'
    r = requests.get(URL)
    data = r.json()
    for i in data:
        movie_cek = MovieAnime.objects.filter(animeId=i['animeId'])
        if movie_cek.exists():
            mov = movie_cek.first()
            mov.animeTitle = i['animeTitle']
            mov.animeImg = i['animeImg']
            mov.releasedDate = i['releasedDate']
            mov.animeUrl = i['animeUrl']
        else:
            MovieAnime.objects.create(
                animeId=i['animeId'],
                animeTitle=i['animeTitle'],
                animeImg=i['animeImg'],
                releasedDate=i['releasedDate'],
                animeUrl=i['animeUrl']
            )
    context = {
        'data':data,
        'data_movies':data_movies
        }
    template_name = "animemovie.html"
    return render(request, template_name, context)

def contact(request):
    template_name = "contact.html"
    context = {}
    return render(request, template_name, context)

