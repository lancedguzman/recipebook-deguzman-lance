from django import forms
from .models import Recipe, RecipeImage

class RecipeForm(forms.ModelForm):
    """Creates form to add recipes."""
    class Meta:
        model = Recipe
        fields = ['recipe_name', 'recipe_author',]


class RecipeImageForm(forms.ModelForm):
    """Creates form to add recipe images."""
    class Meta:
        model = RecipeImage
        fields = ['image','description',]
