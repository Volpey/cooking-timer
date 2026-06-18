import flet as ft

from helpers import get_recipe_emoji


def create_recipes_page(recipes, select_recipe, show_timer_page):
    recipe_items = []

    for recipe_key, recipe in recipes.items():
        emoji = get_recipe_emoji(recipe_key)

        if recipe.temperature is not None:
            details = f"{recipe.cooking_time} min • {recipe.temperature} °C"
        else:
            details = f"{recipe.cooking_time} min • No oven"

        recipe_items.append(
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Text(emoji, size=28),
                        ft.Column(
                            controls=[
                                ft.Text(recipe.name, size=18, weight=ft.FontWeight.BOLD),
                                ft.Text(details, size=13, color="#9CA3AF"),
                            ],
                            spacing=4,
                        ),
                    ],
                    spacing=16,
                ),
                padding=18,
                border_radius=18,
                bgcolor="#111827",
                border=ft.border.all(1, "#1F2937"),
                on_click=lambda e, key=recipe_key: (
                    select_recipe(key),
                    show_timer_page()
                ),
            )
        )

    return ft.Container(
        expand=True,
        padding=40,
        content=ft.Column(
            controls=[
                ft.Text("Recipes", size=34, weight=ft.FontWeight.BOLD),
                ft.Text("Choose a recipe from your collection.", size=16, color="#9CA3AF"),
                ft.Column(
                    controls=recipe_items,
                    spacing=12,
                    scroll=ft.ScrollMode.AUTO,
                    expand=True,
                ),
            ],
            spacing=24,
        ),
    )