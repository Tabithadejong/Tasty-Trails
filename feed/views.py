from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Recipe
from .forms import MyModelForm


# view code for main feed recipes
class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('category')
    template_name = 'index.html'
    paginate_by = 3


# view code for displaying the individual recipes
class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "show_recipe.html",
            {'recipe': recipe, })


# view code for rendering new page with only Starter recipes
def starter_recipe(request):

    starter = Recipe.objects.filter(category='Starter')

    return render(request, 'starter_recipe.html', {'starter': starter, })


# view code for rendering new page with only Main Dishes
def dinner_recipe(request):

    dinner = Recipe.objects.filter(category='Main')

    return render(request, 'dinner_recipe.html', {'dinner': dinner, })


# view code for rendering new page with only Desserts recipes
def dessert_recipe(request):

    dessert = Recipe.objects.filter(category='Dessert')

    return render(request, 'dessert_recipe.html', {'dessert': dessert, })


# view code for displaying the form to add recipes
def AddRecipe(request):

        form = MyModelForm()
        context = {'form': form}

        return render(request, 'add_recipe.html', context)


# view code for handling the add recipes form
def recipe_submit(request):
    if request.method == 'POST':

        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe_submit')
    else:
        form = MyModelForm()
    return render(request, 'recipe_submit.html', {'form': form})       