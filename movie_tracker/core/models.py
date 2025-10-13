from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    avatar = CloudinaryField(
        'Image',
        null=True,
        blank=True,
        default=(
            'https://res.cloudinary.com/dxjuw4mek/image/upload/v1759254836/'
            'placeholder_avatar_gyj9na.png'
        ),
    )

    def __str__(self):
        return f"{self.user}"

