from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeForm, RecipeImageForm

@login_required
def recipe_list(request):
    """Displays recipe list page."""
    recipes = Recipe.objects.all()
    return render(request, "recipe_list.html", {"recipes": recipes})


def recipe_ingredients(request, recipe_id):
    """Displays the corresponding ingredients of each recipe."""
    recipe = Recipe.objects.filter(id=recipe_id).first()
    return render(request, "recipe_ingredients.html", {"recipe": recipe})


def recipe_form(request):
    """Displays the page to create recipes."""
    if (request.method == "POST"):
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("recipe_list")
    form = RecipeForm()
    return render(request, "recipe_form.html", {"recipe_form": form})


def recipe_add_image(request, recipe_id):
    """Displays the page to upload picture of each recipe."""
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if (request.method == "POST"):
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.recipe = recipe
            image.save()
        return redirect("recipe_ingredients", recipe_id=recipe_id)
    form = RecipeImageForm()
    return render(request, "recipe_image.html", {"image_form": form, "recipe": recipe})

def base_template(request):
    """Displays the base template."""
    return render(request,"base_template.html")
