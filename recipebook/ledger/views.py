from django.shortcuts import render

recipes_data = [
    {
        "id": 1,
        "name": "Recipe 1",
        "ingredients":
        [
            {
                "name": "tomato",
                "quantity": "3pcs"
            },
            {
                "name": "onion",
                "quantity": "1pc"
            },
            {
                "name": "pork",
                "quantity": "1kg"
            },
            {
                "name": "water",
                "quantity": "1L"
            },
            {
                "name": "sinigang mix",
                "quantity": "1 packet"
            },
        ]
    },
    {
        "id": 2,
        "name": "Recipe 2",
        "ingredients":
        [
            {
                "name": "garlic",
                "quantity": "1 head"
            },
            {
                "name": "onion",
                "quantity": "1pc"
            },
            {
                "name": "vinegar",
                "quantity": "1/2cup"
            },
            {
                "name": "water",
                "quantity": "1 cup"
            },
            {
                "name": "salt",
                "quantity": "1 tablespoon"
            },
            {
                "name": "whole black peppers",
                "quantity": "1 tablespoon"
            },
            {
                "name": "pork",
                "quantity": "1 kilo"
            },
        ]
    }
]


def recipe_list(request):
    """Displays recipe list page."""
    return render(request, 'recipe_list.html', {"recipes": recipes_data})


def recipe_ingredients(request, recipe_id):
    """Displays the corresponding ingredients of each recipe."""
    recipe = next((r for r in recipes_data if r["id"] == recipe_id), None)
    return render(request, 'recipe_ingredients.html', {"recipe": recipe})
