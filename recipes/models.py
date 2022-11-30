from django.db import models
from accounts.models import Profile

class Category(models.Model):
    name = models.CharField(max_length=30, blank=False, unique=True,)

class Recipe(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='category',
    )
    prepTime = models.DecimalField(decimal_places=1, max_digits=4,)
    cookTime = models.DecimalField(decimal_places=1,max_digits=4,)
    servings = models.IntegerField()

    method = models.TextField()

class Ingredients(models.Model):
    recipes = models.ManyToManyField(
        Recipe,
        related_name='recipes'
    )
    name = models.CharField(max_length=30, blank=False, unique=True,)
