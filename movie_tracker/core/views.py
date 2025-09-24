import requests
from django.conf import settings 
from django.shortcuts import render

def index(request):
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={settings.TMDB_API_KEY}&language=en-US&page=1" # api url
    response = requests.get(url) 
    data = response.json()
    movies = data.get('results', [])

    return render(request, "core/index.html", {"movies": movies})

# search functionality
def search_bar(request):
    query = request.GET.get("query", "") # default to empty string if no query
    url = f"https://api.themoviedb.org/3/search/movie?api_key={settings.TMDB_API_KEY}&query={query}" # query url
    response = requests.get(url)
    data = response.json() #response in json format 
    movies = data.get('results', [])  #get results

    return render(request, "core/results.html", {"movies": movies, "query": query}) #render, pass movies datato template