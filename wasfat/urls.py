"""wasfat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts.views import UserLoginAPIView, UserCreateAPIView
from recipes.views import RecipeListView, CategoryListView, CategoryCreateView, CategoryUpdateView, DeleteView
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers



urlpatterns = [
    path('admin/', admin.site.urls),


    # ----- Authentications URLs -----
    path('auth/signup/', UserCreateAPIView.as_view() , name="signup"),
    path('auth/signin/', UserLoginAPIView.as_view() , name="signin"),


    # ----- Recipes URLs -----
    path('recipes/', RecipeListView.as_view() , name="recipes-list"),
    # path('recipes/add/', users_views.register , name="recipe-add"),
    # path('recipes/<int:recipe_id>/', users_views.register , name="recipe-details"),
    # path('recipes/<int:recipe_id>/edit/', users_views.register , name="recipe-edit"),
    # path('recipes/<int:recipe_id>/delete/', users_views.register , name="recipe-delete"),
    
    
    # ----- Categories URLs -----
    path('categories/', CategoryListView.as_view() , name="categories-list"),
    path('categories/add/', CategoryCreateView.as_view() , name="category-add"),
    path('categories/<int:category_id>/edit/', CategoryUpdateView.as_view() , name="category-edit"),
    path('categories/<int:category_id>/delete/', DeleteView.as_view() , name="category-delete"),
    # path('categories/<int:category_id>/', users_views.register , name="category-details"),
    
    
    # ----- Ingredients URLs -----
    # path('ingredients/', users_views.register , name="ingredients-list"),``
    # path('ingredients/add/', users_views.register , name="ingredient-add"),
    # path('ingredients/<int:ingredient_id>/', users_views.register , name="ingredient-details"),
    # path('ingredients/<int:ingredient_id>/edit/', users_views.register , name="ingredient-edit"),
    # path('ingredients/<int:ingredient_id>/delete/', users_views.register , name="ingredient-delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
