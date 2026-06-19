import random
import flet as ft

from recipe_card import recipe_card
from helpers import get_recipe_image


def create_suggestions(select_recipe, recipes):
    suggestions_title = ft.Text(
        "SUGGESTIONS",
        size=13,
        weight=ft.FontWeight.BOLD,
        color="#A78BFA",
    )

    recipe_items = list(recipes.items())
    random_suggestions = random.sample(
        recipe_items,
        min(12, len(recipe_items))
    )

    cards = []

    for recipe_key, recipe in random_suggestions:
        if recipe.temperature is not None:
            details = f"{recipe.cooking_time} min • {recipe.temperature} °C"
        else:
            details = f"{recipe.cooking_time} min • No oven"

        cards.append(
            recipe_card(
                recipe.name,
                details,
                get_recipe_image(recipe_key),
                lambda e, key=recipe_key: select_recipe(key),
            )
        )

    suggestion_cards = ft.Row(
        controls=cards,
        spacing=18,
        wrap=True,
    )

    return suggestions_title, suggestion_cards