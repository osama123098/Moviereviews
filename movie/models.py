from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Movie(models.Model):
    """Class to manage the app"""
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1500)
    image = models.ImageField(upload_to='movie/image')
    url = models.URLField(blank=True)

class Review(models.Model):
    """Class to manage the review of the movie added by user"""
    text = models.CharField(max_length=1000)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    watchAgain = models.BooleanField()

    def __str__(self):
        return self.text
