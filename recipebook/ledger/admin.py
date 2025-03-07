from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient

class IngredientAdmin(admin.ModelAdmin):
    """Creates Ingredient Admin Panel."""
    model = Ingredient

    list_display = ('ingredient_name',)
    list_filter = ('ingredient_name',)


class RecipeAdmin(admin.ModelAdmin):
    """Creates Recipe Admin Panel."""
    model = Recipe

    list_display = ('recipe_name',)
    list_filter = ('recipe_name',)


class RecipeIngredientAdmin(admin.ModelAdmin):
    """Creates RecipeIngredient Admin Panel."""
    model = RecipeIngredient

    list_display = ('quantity',)


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
