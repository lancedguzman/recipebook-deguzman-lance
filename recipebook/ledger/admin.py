from django.contrib import admin
from django.contrib.auth.models import User
from .models import *


class IngredientAdmin(admin.ModelAdmin):
    """Creates Ingredient Admin Panel."""
    model = Ingredient
    list_display = ('ingredient_name',)
    list_filter = ('ingredient_name',)


class RecipeImageInline(admin.TabularInline):
    """Sets how Recipe Images are displayed in Admin Panel."""
    model = RecipeImage
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    """Creates Recipe Admin Panel."""
    model = Recipe
    list_display = ('recipe_name','recipe_author',
                    'CreatedOn', 'UpdatedOn',)
    list_filter = ('recipe_name',)
    inlines = [RecipeImageInline]


class RecipeIngredientAdmin(admin.ModelAdmin):
    """Creates RecipeIngredient Admin Panel."""
    model = RecipeIngredient
    list_display = ('quantity',)


class RecipeImageAdmin(admin.ModelAdmin):
    """Creates RecipeImage Admin Panel."""
    model = RecipeImage
    list_display = ('image','description',
                    'recipe',)


class ProfileInline(admin.StackedInline):
    """Creates the Profile Admin Panel."""
    model = Profile
    can_delete = False
    fields = ['author_name', 'bio']


class UserAdmin(admin.ModelAdmin):
    """Sets how Profiles are displayed in Admin Panel."""
    inlines = [ProfileInline]

admin.site.register(Ingredient, IngredientAdmin)

admin.site.register(Recipe, RecipeAdmin)

admin.site.register(RecipeIngredient, RecipeIngredientAdmin)

admin.site.register(RecipeImage, RecipeImageAdmin)

admin.site.unregister(User)

admin.site.register(User,UserAdmin)
