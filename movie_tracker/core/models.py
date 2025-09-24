from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MovieList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField((""), max_length=50)
    avatar = models.ImageField
