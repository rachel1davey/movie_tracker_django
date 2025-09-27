from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
import requests

from movies.models import Review
from django.db import models

from .models import Profile
from .forms import ProfileForm

User = get_user_model()

def index(request):
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={settings.TMDB_API_KEY}&language=en-US&page=1" # api url
    response = requests.get(url) 
    data = response.json()
    movies = data.get('results', [])

    #avg_rating_name for each movie
    for movie in movies:
        movie_id = movie["id"]
        reviews = Review.objects.filter(movie_id=movie_id)
        avg_rating = reviews.aggregate(models.Avg("rating"))["rating__avg"]

        if avg_rating is not None:
            if avg_rating < 2:
                movie["avg_rating_name"] = "Mostly Negative"
            elif avg_rating < 3:
                movie["avg_rating_name"] = "Negative"
            elif avg_rating < 4:
                movie["avg_rating_name"] = "Positive"
            else:
                movie["avg_rating_name"] = "Mostly Positive"
        else:
            movie["avg_rating_name"] = None  # no reviews yet
            
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
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, "core/own_profile.html", {"profile": profile})

def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    profile, created = Profile.objects.get_or_create(user=user)
    return render(request, "core/user_profile.html", {
        "profile_user": user,
        "profile": profile
    })

@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("core:own_profile")  # Redirect back to profile page
    else:
        form = ProfileForm(instance=profile)

    return render(request, "core/edit_profile.html", {"form": form})