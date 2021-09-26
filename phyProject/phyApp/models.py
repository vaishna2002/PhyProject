from django.db import models

# Create your models here.


class Simulation_Project(models.Model):
    project_name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)
    geogebra_link = models.CharField(max_length=1000)
    youtube_link = models.CharField(max_length=1000)
    image = models.CharField(max_length=1000)

class Video_Project(models.Model):
    project_name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)
    youtube_link = models.CharField(max_length=1000)
    image = models.CharField(max_length=1000)