from django.contrib import admin
from recipes.models import Category, Recipe, Ingredient

admin.site.register([Category, Recipe, Ingredient])