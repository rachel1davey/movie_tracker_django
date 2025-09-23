import requests
from django.conf import settings 
from django.shortcuts import render

def index(request):
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={settings.TMDB_API_KEY}&language=en-US&page=1" # api url
    response = requests.get(url) 
    data = response.json()
    movies = data.get('results', [])

    return render(request, "core/index.html", {"movies": movies})