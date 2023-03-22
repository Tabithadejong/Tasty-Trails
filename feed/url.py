from . import views
from django.urls import path
from .views import RecipeDetailView

urlpatterns= [ 
    path('', views.RecipeList.as_view(), name='home'), 
    path('post/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail') 
]