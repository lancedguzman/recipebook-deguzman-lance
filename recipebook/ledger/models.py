from django.db import models
from django.contrib.auth.models import User


class Ingredient(models.Model):
    """Creates the Ingredient Model."""
    ingredient_name = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.ingredient_name


class Recipe(models.Model):
    """Creates the Recipe Model."""
    recipe_name = models.CharField(max_length=255, default="")
    recipe_author = models.CharField(max_length=255, default="")
    CreatedOn = models.DateField(auto_now_add=True)
    UpdatedOn = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.recipe_name} by {self.recipe_author}"


class RecipeIngredient(models.Model):
    """Creates the RecipeIngredient Model."""
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE,
                                   related_name="ingredients")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name="recipe")
    quantity = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.quantity} of {self.ingredient.ingredient_name} in {self.recipe.recipe_name}"


class RecipeImage(models.Model):
    """Creates the RecipeImage Model."""
    image = models.ImageField(upload_to="images/", blank=False,
                              null=False)
    description = models.TextField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name="images")

    def __str__(self):
        return f"{self.recipe.recipe_name}: {self.description}"

    def add_image(self):
        return f"/recipe/{self.id}/add_image"


class Profile(models.Model):
    """Creates the Profile Model."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=50, default="")
    bio = models.CharField(max_length=255, default="")
