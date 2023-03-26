from django.shortcuts import render , get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Recipe
from .forms import MyModelForm




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


def starter_recipe(request): 

    starter = Recipe.objects.filter(category='Starter')

    return render(request, 'starter_recipe.html',
    {'starter': starter, 
     } )

def dinner_recipe(request): 

    dinner = Recipe.objects.filter(category='Main')

    return render(request, 'dinner_recipe.html',
    {'dinner': dinner, 
     } )


def dessert_recipe(request): 

    dessert = Recipe.objects.filter(category='Dessert')

    return render(request, 'dessert_recipe.html',
    {'dessert': dessert, 
     } )     



def AddRecipe(request):

        form = MyModelForm()
        context = {'form': form}

        return render(request, 'add_recipe.html',context)

