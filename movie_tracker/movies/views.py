import requests
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from .forms import ReviewForm


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
    
    # check if the user is authenticated and has a review
    user_review = None
    if request.user.is_authenticated:
        user_review = Review.objects.filter(
            movie_id=movie_id, author=request.user
        ).first()
    
    '''
    ADD AVG RATING CALC HERE TO DISPLAY ON CARDS
    rating_avg = Review.objects.filter(movie_id=movie_id)
    '''

    # 3. Render template with movie and review info
    context = {
        "movie": movie,
        "user_review": user_review
    }
    return render(request, "movies/movie_detail.html", context)

# add watchlist functionality
'''
def watchlist(request, movie_id):
'''


    