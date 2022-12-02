from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from recipes.serializer import RecipeListSerializer, CategoryListSerializer


from recipes.models import Category, Recipe


class CategorySerializer(serializers.ModelSerializer):


    class Meta:
        model = Category
        fields = "__all__"

# Create your views here.
class CategoriesView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def destroy(self, req, pk):

        # extra logic 
    
        super.destroy(req, pk)

    authentication_classes = []


class RecipeListView(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeListSerializer

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer