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


class Ingredient(models.Model):
    
    title = models.CharField(max_length=30, blank=False, unique=True,)

    def __str__(self) :
        return f'ID: {self.id} - {self.title}'
 

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
        related_name='recipes',
        blank=True,
    )
    
    title = models.CharField(max_length=30,)
    prepTime = models.IntegerField(blank=True, null= True,)
    cookTime = models.IntegerField(blank=True, null= True,)
    servings = models.IntegerField(blank=True, null= True,)
    method = models.TextField(blank=True, null= True,)
    image = models.ImageField(upload_to='images/recipes', blank=True,)

    def __str__(self) :
        return self.title




# class Likes(models.Model):
#     profile = models.ForeignKey(
#         Profile,
#         on_delete=models.CASCADE,
#         related_name='likes',
#     )
#     recipe = models.ForeignKey(
#         Recipe,
#         on_delete=models.CASCADE,
#         related_name='likes'
#     )
#     liked_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.profile} liked {self.recipe} on {self.liked_at}'

#     class Meta:
#             verbose_name_plural = 'Likes'

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