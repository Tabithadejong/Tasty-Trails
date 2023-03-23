from django.shortcuts import render , get_object_or_404
from django.views import generic, View
from django.views.generic import DetailView
from .models import Recipe, Comment

class RecipeList(generic.ListView): 
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('category')
    template_name= 'index.html'
    paginate_by = 3
    
class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs): 
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)

        return render(
            request, 
            "show_recipe.html", 
            {'recipe': recipe, 
            })