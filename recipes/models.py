from django.db import models
from accounts.models import Profile


class Category(models.Model):
    title = models.CharField(max_length=30, blank=False, unique=True,)
    image = models.ImageField(upload_to='images/categories', blank=True,)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


    def __str__(self) :
        return self.title


class Ingredient(models.Model):
    # recipes = models.ManyToManyField(
    #     Recipe,
    #     related_name='recipes'
    # )
    title = models.CharField(max_length=30, blank=False, unique=True,)

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
    prepTime = models.IntegerField(blank=True, null= True,)
    cookTime = models.IntegerField(blank=True, null= True,)
    servings = models.IntegerField(blank=True, null= True,)
    method = models.TextField(blank=True, null= True,)
    image = models.ImageField(upload_to='images/recipes', blank=True,)
    # ingredient = models.ManyToManyField(
    #     Ingredient,
    #     related_name='ingredients',
    # )

    def __str__(self) :
        return self.title


class Quantity(models.Model):
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='ingredient',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe'
    )
    qty = models.CharField(max_length=30, )
    unit = models.CharField(max_length=30, )

    class Meta:
        verbose_name = 'Quantity'
        verbose_name_plural = 'Quantities'

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