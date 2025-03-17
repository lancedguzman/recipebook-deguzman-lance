from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_template, name='home'),
    path('recipes/list/', views.recipe_list, name='recipe_list'),
    path('recipe/<int:recipe_id>/', views.recipe_ingredients,
         name='recipe_ingredients'),
]
