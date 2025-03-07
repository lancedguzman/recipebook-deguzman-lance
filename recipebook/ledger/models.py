from django.db import models

class Ingredient(models.Model):
    """Creates the Ingredient Model."""
    ingredient_name = models.CharField(max_length=255, default="")

    def __str__(self):
         return self.ingredient_name


class Recipe(models.Model):
    """Creates the Recipe Model."""
    recipe_name = models.CharField(max_length=255, default="")

    def __str__(self):
         return self.recipe_name


class RecipeIngredient(models.Model):
    """Creates the RecipeIngredient Model."""
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="ingredients")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe")
    quantity = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.quantity} of {self.ingredient.ingredient_name} in {self.recipe.recipe_name}"
