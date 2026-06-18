import flet as ft

from recipes import RECIPES
from helpers import (
    get_recipe_emoji,
    get_recipe_image,
)

from sidebar import create_sidebar
from timer import TimerManager
from hero_card import create_hero_card

from buttons import (
    create_start_button,
    create_stop_button,
)

from search_bar import create_search_controls
from suggestions import create_suggestions
from recipes_page import create_recipes_page


def main(page: ft.Page):
    page.title = "CookFlow"
    page.window.width = 1400
    page.window.height = 1000
    page.window.resizable = True
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.bgcolor = "#070A12"

    selected_recipe = None
    search_input = None

    recipe_title = ft.Text(
        "Pizza 🍕",
        size=36,
        weight=ft.FontWeight.BOLD,
    )

    timer_text = ft.Text(
        "15:00",
        size=58,
        weight=ft.FontWeight.BOLD,
    )

    timer_status = ft.Text(
        "Ready to start",
        size=15,
        color="#9CA3AF",
    )

    time_info = ft.Text(
        "15 minutes",
        size=16,
        weight=ft.FontWeight.BOLD,
    )

    temp_info = ft.Text(
        "220 °C",
        size=16,
        weight=ft.FontWeight.BOLD,
    )

    recipe_image = ft.Image(
        src="assets/pizza.png",
        width=300,
        height=300,
        fit=ft.ImageFit.COVER,
    )

    def start_timer(e):
        timer_manager.start(selected_recipe)

    def stop_timer(e):
        if selected_recipe is not None:
            timer_manager.stop()

    start_button = create_start_button(start_timer)
    stop_button = create_stop_button(stop_timer)

    timer_manager = TimerManager(
        page,
        timer_text,
        timer_status,
        start_button,
        stop_button,
    )

    def select_recipe(recipe_key):
        nonlocal selected_recipe

        if recipe_key not in RECIPES:
            return

        if selected_recipe is not None:
            timer_manager.stop()

        selected_recipe = RECIPES[recipe_key]
        emoji = get_recipe_emoji(recipe_key)

        recipe_title.value = f"{selected_recipe.name} {emoji}"
        timer_text.value = f"{int(selected_recipe.cooking_time):02d}:00"
        timer_status.value = "Ready to start"
        time_info.value = f"{selected_recipe.cooking_time} minutes"

        if selected_recipe.temperature is not None:
            temp_info.value = f"{selected_recipe.temperature} °C"
        else:
            temp_info.value = "No oven"

        recipe_image.src = get_recipe_image(recipe_key)

        start_button.bgcolor = "#FFFFFF"
        stop_button.bgcolor = "#374151"

        page.update()

    def search_recipe(e):
        user_input = search_input.value.strip().lower()
        select_recipe(user_input)

    search_input, search_bar = create_search_controls(
        search_recipe
    )

    headline = ft.Text(
        "What are we cooking today?",
        size=34,
        weight=ft.FontWeight.BOLD,
    )

    subtitle = ft.Text(
        "Search a recipe or choose one of the suggestions.",
        size=16,
        color="#9CA3AF",
    )

    hero_card = create_hero_card(
        recipe_title,
        time_info,
        temp_info,
        timer_text,
        timer_status,
        start_button,
        stop_button,
        recipe_image,
    )

    suggestions_title, suggestion_cards = (
        create_suggestions(select_recipe)
    )

    timer_page = ft.Container(
        expand=True,
        padding=40,
        content=ft.Column(
            controls=[
                headline,
                subtitle,
                search_bar,
                hero_card,
                suggestions_title,
                suggestion_cards,
            ],
            spacing=22,
        ),
    )

    content_area = ft.Container(expand=True)

    def show_timer_page():
        content_area.content = timer_page
        page.update()

    def show_recipes_page():
        content_area.content = create_recipes_page(
            RECIPES,
            select_recipe,
            show_timer_page,
        )
        page.update()

    sidebar = create_sidebar(
        show_timer_page,
        show_recipes_page,
    )

    select_recipe("pizza")
    content_area.content = timer_page

    page.add(
        ft.Row(
            controls=[
                sidebar,
                content_area,
            ],
            expand=True,
            spacing=0,
        )
    )


ft.app(target=main)