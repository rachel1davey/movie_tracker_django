from django.db import models
from django.contrib.auth import User

# Create your models here.

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=500)
    rating = models.IntegerField(default=0,validators=[MinValueValidator(1), MaxValueValidator(5)], movie_id = models.IntegerField(), created_at = models.DateTimeField(auto_now_add=True), updated_at = models.DateTimeField(auto_now=True)
)

