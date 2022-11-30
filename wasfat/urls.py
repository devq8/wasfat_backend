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
from django.urls import path
from accounts.views import UserLoginAPIView, UserCreateAPIView

urlpatterns = [
    path('admin/', admin.site.urls),


    # ----- Authentications URLs -----
    path('auth/signup/', UserCreateAPIView.as_view() , name="signup"),
    path('auth/login/', UserLoginAPIView.as_view() , name="login"),


    # ----- Recipes URLs -----
    # path('recipes/', users_views.register , name="recipes-list"),
    # path('recipes/add/', users_views.register , name="recipe-add"),
    # path('recipes/<int:recipe_id>/', users_views.register , name="recipe-details"),
    # path('recipes/<int:recipe_id>/edit/', users_views.register , name="recipe-edit"),
    # path('recipes/<int:recipe_id>/delete/', users_views.register , name="recipe-delete"),
    
    
    # ----- Categories URLs -----
    # path('categories/', users_views.register , name="categories-list"),
    # path('categories/add/', users_views.register , name="category-add"),
    # path('categories/<int:category_id>/', users_views.register , name="category-details"),
    # path('categories/<int:category_id>/edit/', users_views.register , name="category-edit"),
    # path('categories/<int:category_id>/delete/', users_views.register , name="category-delete"),
    
    
    # ----- Ingredients URLs -----
    # path('ingredients/', users_views.register , name="ingredients-list"),
    # path('ingredients/add/', users_views.register , name="ingredient-add"),
    # path('ingredients/<int:ingredient_id>/', users_views.register , name="ingredient-details"),
    # path('ingredients/<int:ingredient_id>/edit/', users_views.register , name="ingredient-edit"),
    # path('ingredients/<int:ingredient_id>/delete/', users_views.register , name="ingredient-delete"),
]
