from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView ,UpdateAPIView ,DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from recipes.serializer import RecipeListSerializer, CategoryListSerializer


from recipes.models import Category, Recipe



# Create your views here.

class RecipeListView(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeListSerializer



class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

class CategoryCreateView(CreateAPIView):
    serializer_class = CategoryListSerializer

    def perform_create(self, serializer):
        serializer.save()

class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'category_id'

class DeleteView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'category_id'

