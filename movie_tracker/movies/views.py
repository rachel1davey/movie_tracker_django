import requests
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from .forms import ReviewForm
from django.db import models


# Create your views here.

def movie_detail(request, movie_id):
    # 1. Fetch movie details from TMDB API
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {"api_key": settings.TMDB_API_KEY, "language": "en-US"}
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        movie = None  # fallback if movie not found
    else:
        movie = response.json()
    
    # get all reviews for this movie
    reviews = Review.objects.filter(movie_id=movie_id).select_related("author")
    
    # check if the user already has a review
    user_review = None
    if request.user.is_authenticated:
        user_review = reviews.filter(author=request.user).first()
    
    # average rating (optional)
    avg_rating = reviews.aggregate(models.Avg("rating"))["rating__avg"]

    context = {
        "movie": movie,
        "reviews": reviews,
        "user_review": user_review,
        "avg_rating": avg_rating,
    }
    return render(request, "movies/movie_detail.html", context)


# add watchlist functionality
'''
def add_to_watchlist(request, movie_id):
'''


    