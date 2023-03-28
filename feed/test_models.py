from django.test import TestCase
from .models import Recipe
from django.contrib.auth.models import User

class RecipeModelTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a User object for testing
        test_user = User.objects.create_user(username='testuser', password='testpass')
        test_user.save()

        # Create a Recipe object for testing
        test_recipe = Recipe.objects.create(
            recipe='Spaghetti Carbonara',
            slug='spaghetti-carbonara',
            author=test_user,
            cooking_time=Recipe.REGULAR,
            amount_of_people=Recipe.four,
            category=Recipe.MAIN,
            ingriedients='pasta, eggs, bacon',
            preperation='1. Cook pasta. 2. Fry bacon. 3. Whisk eggs. 4. Mix everything together.',
            
        )

    def test_recipe_model(self):
        recipe = Recipe.objects.get(recipe='Spaghetti Carbonara')
        self.assertEqual(recipe.slug, 'spaghetti-carbonara')
        self.assertEqual(recipe.author.username, 'testuser')
        self.assertEqual(recipe.cooking_time, Recipe.REGULAR)
        self.assertEqual(recipe.amount_of_people, Recipe.four)
        self.assertEqual(recipe.category, Recipe.MAIN)
        self.assertEqual(recipe.ingriedients, 'pasta, eggs, bacon')
        self.assertEqual(recipe.preperation, '1. Cook pasta. 2. Fry bacon. 3. Whisk eggs. 4. Mix everything together.')
        