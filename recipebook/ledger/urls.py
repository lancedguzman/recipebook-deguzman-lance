from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.base_template, name='home'),
    path('recipes/list/', views.recipe_list, name='recipe_list'),
    path('recipe/<int:recipe_id>/', views.recipe_ingredients,
         name='recipe_ingredients'),
    path('recipe/add/', views.recipe_form, name='recipe_form'),
    path('recipe/<int:recipe_id>/add_image', views.recipe_add_image,
         name='add_image'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
