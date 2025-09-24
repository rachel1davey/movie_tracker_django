from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    rating = models.IntegerField(default=0,validators=[MinValueValidator(1), MaxValueValidator(5)])
    movie_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('author', 'movie_id')

    def __str__(self):
        return f"{self.author} - {self.movie_id}"


