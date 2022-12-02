from django.contrib import admin
from recipes.models import Category, Recipe, Ingredient, Quantity

# Register your models here.
admin.site.register([Category, Recipe, Ingredient, Quantity,])