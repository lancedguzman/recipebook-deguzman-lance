from django import forms
from .models import Recipe, RecipeImage, Ingredient

class RecipeForm(forms.ModelForm):
    """Creates form to add recipes."""
    ingredient = forms.ModelChoiceField(
        queryset = Ingredient.objects.all(),
        empty_label ="Select an ingredient",
        widget = forms.Select(attrs={"class": "form-control"}),
        required = True
    )

    quantity = forms.CharField(max_length=100, required=True)

    class Meta:
        model = Recipe
        fields = ["recipe_name", "recipe_author"]


class IngredientForm(forms.ModelForm):
    """Creates form to add ingredients."""
    class Meta:
        model = Ingredient
        fields = ["ingredient_name"]


class RecipeImageForm(forms.ModelForm):
    """Creates form to add recipe images."""
    class Meta:
        model = RecipeImage
        fields = ["image","description"]
