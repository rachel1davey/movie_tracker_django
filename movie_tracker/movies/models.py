from django.db import models
from allauth import User

# Create your models here.

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length="500")
    rating = models.IntegerField(default=0)


