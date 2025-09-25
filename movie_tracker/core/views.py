import requests
from django.conf import settings 
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import User, Profile

def index(request):
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={settings.TMDB_API_KEY}&language=en-US&page=1" # api url
    response = requests.get(url) 
    data = response.json()
    movies = data.get('results', [])

    page_number = request.GET.get("page", 1) # get page num from url
    paginator = Paginator(movies, 12) # 12 movies per page
    page_obj = paginator.get_page(page_number) #

    return render(request, "core/index.html", {"page_obj": page_obj})

# search functionality
def search_bar(request):
    query = request.GET.get("query", "") # default to empty string if no query
    url = f"https://api.themoviedb.org/3/search/movie?api_key={settings.TMDB_API_KEY}&query={query}" # query url
    response = requests.get(url)
    data = response.json() #response in json format 
    movies = data.get('results', [])  #get results

    page_number = request.GET.get("page", 1) # get page num from url
    paginator = Paginator(movies, 12) # 12 movies per page
    page_obj = paginator.get_page(page_number) # returns requested page




    return render(request, "core/results.html", {"page_obj": page_obj, "query": query}) #render, pass movies datato template


@login_required
def own_profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, "core/own_profile.html", {"profile": profile})

@login_required
def user_profile(request):
    return render(request, "core/user_profile.html")