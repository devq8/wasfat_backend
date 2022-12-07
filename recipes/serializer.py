from rest_framework import serializers
from recipes.models import Category, Recipe, Ingredient, Quantity

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

    class Meta:
        model = Recipe
        fields = ['id', 'profile', 'category', 'title', 'prepTime', 'cookTime', 'servings', 'method', 'image',]

class QuantityListSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Quantity
        fields = ['ingredient', 'recipe', 'qty', 'unit', ]

# class RecipeUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Recipe
#         fields = ['id', 'title', 'category', ]