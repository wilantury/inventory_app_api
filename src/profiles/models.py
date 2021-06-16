from django.db import models
from django.contrib.auth.models import User

class City(models.Model):
    name = models.CharField(max_length=80, unique=True)

    def __str__(self) -> str:
        return f'{self.name}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profiles', default='no_picture.png')
    bio = models.TextField(max_length=300)
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'bio:{self.bio}'
