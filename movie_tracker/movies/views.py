import requests
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from .forms import ReviewForm
from django.db import models
from django.contrib.auth.decorators import login_required

# Create your views here.

def movie_detail(request, movie_id):
    # fetch movie details from TMDB API
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {"api_key": settings.TMDB_API_KEY, "language": "en-US"}
    response = requests.get(url, params=params)
    
    movie = response.json() if response.status_code == 200 else None
    
    # get all reviews for this movie
    reviews = Review.objects.filter(movie_id=movie_id).select_related("author")
    
    # check if the user already has a review
    user_review = None
    if request.user.is_authenticated:
        user_review = reviews.filter(author=request.user).first()
    
    # handle review submission
    if request.method == "POST" and request.user.is_authenticated:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.movie_id = movie_id
            review.save()
            return redirect("movies:movie_detail", movie_id=movie_id)
    else:
        form = ReviewForm()

    # average rating for movie page
    avg_rating = reviews.aggregate(models.Avg("rating"))["rating__avg"]

    avg_rating_name = None

    if avg_rating is not None:
        if avg_rating < 2:
            avg_rating_name = "Mostly Negative"
        elif avg_rating < 3:
            avg_rating_name = "Negative"
        elif avg_rating < 4:
            avg_rating_name = "Positive"
        else:
            avg_rating_name = "Mostly Positive"

    context = {
        "movie": movie,
        "reviews": reviews,
        "user_review": user_review,
        "avg_rating": avg_rating,
        "avg_rating_name": avg_rating_name,
        "form": form,  # pass form to template
    }
    return render(request, "movies/movie_detail.html", context)

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, author=request.user)

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect("movies:movie_detail", movie_id=review.movie_id)
    else:
        form = ReviewForm(instance=review)

    context = {
        "form": form,
        "review": review,
    }
    return render(request, "movies/edit_review.html", context)


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, author=request.user)

    if request.method == "POST":  # confirm delete
        movie_id = review.movie_id
        review.delete()
        return redirect("movies:movie_detail", movie_id=movie_id)

    return render(request, "movies/delete_review.html", {"review": review})

'''
def add_to_watchlist(request, movie_id):
'''


    