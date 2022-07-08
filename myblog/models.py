from django.db import models
from django.contrib.auth.models import User

"""
class Auteur(models.Model):
    name = models.CharField("name",max_length=55)
    prenom = models.CharField("prenom",max_length=55)
"""

class Blog(models.Model):
    auteur = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField("title",max_length=255)
    content = models.TextField("content")

# Create your models here.
