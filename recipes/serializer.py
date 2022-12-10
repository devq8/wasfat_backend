from rest_framework import serializers
from recipes.models import Category, Recipe, Ingredient

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'image',]

class IngredientListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ['id', 'title',]


class RecipeListSerializer(serializers.ModelSerializer):

    category = CategoryListSerializer()

    ingredients = IngredientListSerializer(many=True,)

    class Meta:
        model = Recipe
        fields = ['id', 'profile', 'category', 'title', 'prepTime', 'cookTime', 'servings', 'method', 'image', 'ingredients']

class CreateRecipeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Recipe
        fields = ['profile', 'category', 'title', 'prepTime', 'cookTime', 'servings', 'method', 'image', 'ingredients']
