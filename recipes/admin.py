from django.contrib import admin
from recipes.models import Category, Recipe, Ingredient

# Register your models here.
admin.site.register([Category, Recipe, Ingredient,])