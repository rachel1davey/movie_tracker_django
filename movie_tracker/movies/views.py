import requests
from django.conf import settings 
from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm


# Create your views here.

def movie_detail(request, movie_id):
    reviews = Review.objects.filter(movie_id=movie_id)

# review form post
    if request.method == "POST":
        if request.user.is_authenticated:
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.author = request.user
                review.movie_id = movie_id
                review.save()
                return redirect("movie_detail", movie_id=movie_id)
    else:
        form = ReviewForm()

    # Fetch movie from TMDB for movie details
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={settings.TMDB_API_KEY}&language=en-US"
    response = requests.get(url)
    data = response.json()

    context = {
        "movie": data,
        "reviews": reviews,
        "form": form,
    }
    return render(request, "movies/movie_detail.html", context)

    