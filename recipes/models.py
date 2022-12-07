from django.db import models
from accounts.models import Profile
from django.contrib.auth import get_user_model

User = get_user_model

class Category(models.Model):
    title = models.CharField(max_length=30, blank=False, unique=True,)
    image = models.ImageField(upload_to='images/categories', blank=True,)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


    def __str__(self) :
        return self.title

class Quantity(models.Model):
    
    # recipe = models.ForeignKey(
    #     Recipe,
    #     on_delete=models.CASCADE,
    #     related_name='recipe'
    # )
    qty = models.CharField(max_length=30, )
    unit = models.CharField(max_length=30, )

    # class Meta:
    #     verbose_name = 'Quantity'
    #     verbose_name_plural = 'Quantities'

    def __str__(self) :
        return f'{self.qty} {self.unit}'



class Ingredient(models.Model):
    # recipe = models.ManyToManyField(
    #     Recipe,
    #     related_name='ingredient'
    # )
    qty = models.ForeignKey(
        Quantity,
        on_delete=models.CASCADE,
        related_name='ingredient',
    )
    title = models.CharField(max_length=30, blank=False, unique=True,)

    def __str__(self) :
        return f'{self.qty} of {self.title}'
 

class Recipe(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="recipes",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='recipes',
    )

    ingredients = models.ManyToManyField(
        Ingredient,
        related_name='recipes'
    )

    # ingredients = models.ManyToManyField(
    #     Ingredient, 
    #     related_name='ingredients',
    # )
    title = models.CharField(max_length=30,)
    prepTime = models.IntegerField(blank=True, null= True,)
    cookTime = models.IntegerField(blank=True, null= True,)
    servings = models.IntegerField(blank=True, null= True,)
    method = models.TextField(blank=True, null= True,)
    image = models.ImageField(upload_to='images/recipes', blank=True,)

    def __str__(self) :
        return self.title



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