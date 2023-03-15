from django.shortcuts import render
from djano.views import generic 
from .models import Recipe

class RecipeList(generic.Listview): 
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('category')
    template_name= 'index.html'
    paginate_by = 4 
    