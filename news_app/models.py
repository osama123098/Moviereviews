from django.db import models

# Create your models here.
class News(models.Model):
    """Class to manage the model of news"""
    headline = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField()

    def __str__(self):
        """display the object more readible form"""
        return self.headline