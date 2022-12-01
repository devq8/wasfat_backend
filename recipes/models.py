from django.db import models
from accounts.models import Profile


class Category(models.Model):
    title = models.CharField(max_length=30, blank=False, unique=True,)
    # image = models.ImageField()

    def __str__(self) :
        return self.title

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
    title = models.CharField(max_length=30,)
    prepTime = models.IntegerField(blank=True,)
    cookTime = models.IntegerField(blank=True,)
    servings = models.IntegerField(blank=True,)
    method = models.TextField()
    # image = models.ImageField()
    # ingredients = models.TextField()

    def __str__(self) :
        return self.title

class Ingredient(models.Model):
    recipes = models.ManyToManyField(
        Recipe,
        related_name='recipes'
    )
    title = models.CharField(max_length=30, blank=False, unique=True,)

    def __str__(self) :
        return self.title


class Quantity(models.Model):
    ingredient = models.OneToOneField(
        Ingredient,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    qty = models.CharField(max_length=30, )
    unit = models.CharField(max_length=30, )

    def __str__(self) :
        return self.qty



# class Rate(models.Model):
#     profile = models.ForeignKey(
#         Profile,
#         on_delete=models.CASCADE,
#         related_name='profile',
#     )
#     recipe = models.ForeignKey(
#         Recipe,
#         on_delete=models.CASCADE,
#         related_name='recipe',
#     )
#     rate = models.IntegerField(blank=False,)

# class Report(models.Model):
#     profile = models.ForeignKey(
#         Profile,
#         on_delete=models.CASCADE,
#         related_name='profile',
#     )
#     category = models.ForeignKey(
#         Category,
#         on_delete=models.CASCADE,
#         related_name='category',
#     )
#     details = models.CharField(max_length=30, blank=False,)