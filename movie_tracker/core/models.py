from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS_CHOICES = [
    ('plan', 'Plan to Watch'),
    ('watching', 'Watching'),
    ('completed', 'Completed'), 
]
class MovieList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    is_public = models.BooleanField(default=False)
    added_at = models.DateTimeField(auto_now=True)
    

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField()
    avatar = cloud('Image', null=True, blank=True)

    def __str__(self):
        return f"{self.user}"
    
