from django.test import TestCase
from .models import Recipes
# Create your tests here.
class RecipesTest(TestCase):
    def setUpTestData():
        # Set up non-modified objects used by all test methods
        Recipes.objects.create(name='Tacos', ingredients='Tortillas, coriander, onions, salsa, lemon, meat, salt, pepper', id= 1, difficulty= 'intermediate', cooking_time= 10)

    def test_recipe_name(self):
        # get a Recipe object to test
        recipe = Recipes.objects.get(id=1)
        # get metadata for the 'name' filed and use it toq uery its data
        field_label = recipe._meta.get_field('name').verbose_name
        # compare the value to the expected result
        self.assertEqual(field_label, 'name')

    def test_recipe_name_max_length(self):
        # get a Recipe object to test
        recipe = Recipes.objects.get(id=1)
        # get meta data for the recipe_name field and use it to query its max length
        max_length = recipe._meta.get_field('name').max_length
        # compare the value to the expected result
        self.assertEqual(max_length, 50)
    
    def test_recipe_ingredients(self):
        # get a Recipe object to test
        recipe = Recipes.objects.get(id=1)
        # get meta data for the recipe_ingredients field and use it to query its max length
        max_length_ing = recipe._meta.get_field('ingredients').max_length
        # compare the value to the expected result
        self.assertEqual(max_length_ing, 250)