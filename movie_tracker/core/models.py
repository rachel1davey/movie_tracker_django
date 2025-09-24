from django.db import models
from allauth import User

# Create your models here.
class MovieList(models.Model)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Profile(models.Model):
    user = models.models.ForeignKey(User,on_delete=models.CASCADE)
    bio = models.CharField(_(""), max_length=50)
    avatar = models.ImageField
