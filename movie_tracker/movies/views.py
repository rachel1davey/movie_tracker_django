import requests
from django.conf import settings 
from django.shortcuts import render

# Create your views here.

def movie_detail(request, movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={settings.TMDB_API_KEY}&language=en-US " # api url
    response = requests.get(url)
    data = response.json()
    return render(request, 'movies/movie_detail.html', {"movie": data})

