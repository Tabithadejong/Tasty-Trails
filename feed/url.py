from . import views
from django.urls import path
from .views import RecipeDetail

urlpatterns= [ 
    path('', views.RecipeList.as_view(), name='home'),  
     path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),  
]