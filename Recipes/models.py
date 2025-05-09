from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes', null=True)