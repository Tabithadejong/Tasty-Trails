from . import views
from django.urls import path
from .views import RecipeDetail, AddRecipe

urlpatterns= [ 
    path('', views.RecipeList.as_view(), name='home'),  
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),  
    path('starter_recipe', views.starter_recipe, name='starter_recipe'),  
    path('dinner_recipe', views.dinner_recipe, name='dinner_recipe'),  
    path('dessert_recipe', views.dessert_recipe, name='dessert_recipe'),  
    path('add_recipe/', views.AddRecipe, name='add_recipe'), 

]