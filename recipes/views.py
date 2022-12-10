
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView
from recipes.serializer import RecipeListSerializer, CreateRecipeSerializer
from recipes.serializer import CategoryListSerializer, IngredientListSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from recipes.models import Category, Recipe, Ingredient

from recipes.permissions import IsCreator


# ------------- RECIPE VIEWS -------------

class RecipeListView(ListAPIView):
    serializer_class = RecipeListSerializer
    def get_queryset(self):
        queryset = Recipe.objects.all()
        
        return queryset
    permission_classes=[AllowAny]

class RecipeCreateView(CreateAPIView):
    serializer_class = CreateRecipeSerializer
    def perform_create(self, serializer):
        serializer.save()
    permission_classes=[IsAuthenticated]

class RecipeUpdateView(UpdateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'recipe_id'
    permission_classes = [IsCreator,IsAdminUser]

class RecipeDeleteView(DestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'recipe_id'
    permission_classes = [IsCreator,IsAdminUser]


# ------------- CATEGORY VIEWS -------------

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes=[AllowAny]

class CategoryCreateView(CreateAPIView):
    serializer_class = CategoryListSerializer
    def perform_create(self, serializer):
        serializer.save()
    permission_classes=[IsAuthenticated]

class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'category_id'
    permission_classes=[IsAuthenticated,IsAdminUser]

class CategoryDeleteView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'category_id'
    permission_classes=[IsAuthenticated,IsAdminUser]



# ------------- INGREDIENT VIEWS -------------

class IngredientListView(ListAPIView):
    serializer_class = IngredientListSerializer
    def get_queryset(self):
        recipes = Recipe.objects.all()
        category = self.request.query_params.get('category')
        if category is not None:
            recipes = Recipe.objects.filter(category__id = category)
        queryset = Ingredient.objects.filter(recipes__in=list(recipes)).distinct()
        return queryset
    permission_classes=[AllowAny]

class IngredientCreateView(CreateAPIView):
    serializer_class = IngredientListSerializer
    def perform_create(self, serializer):
        serializer.save()
    permission_classes=[IsAuthenticated]

class IngredientUpdateView(UpdateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'ingredient_id'
    permission_classes = [IsAuthenticated,IsAdminUser]

class IngredientDeleteView(DestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'ingredient_id'
    permission_classes=[IsAuthenticated,IsAdminUser]
