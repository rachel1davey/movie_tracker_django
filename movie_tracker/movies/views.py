import requests
from django.conf import settings 
from django.shortcuts import render, redirect
from .models import Review

# Create your views here.

def movie_detail(request, movie_id):
    # fetch reviews only for this movie
    reviews = Review.objects.filter(movie_id=movie_id)

    # handle review submission
    if request.method == "POST":
        body = request.POST.get("body")
        rating = request.POST.get("rating")

        # only create review if user is logged in
        if request.user.is_authenticated:
          existing_review = Review.objects.filter(author=request.user, movie_id=movie_id).first()
        if not existing_review:
          Review.objects.create(
              author=request.user,
              movie_id=movie_id,
              body=body,
              rating=rating
          )
        # Redirect back to the same movie detail page
        return redirect("movie_detail", movie_id=movie_id)

    # fetch movie details from TMDB
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={settings.TMDB_API_KEY}&language=en-US"
    response = requests.get(url)
    data = response.json()
    # render the template with movie data and reviews
    context = {
        "movie": data,
        "reviews": reviews
    }
    return render(request, "movies/movie_detail.html", context)

    