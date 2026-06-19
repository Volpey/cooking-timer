import flet as ft

from recipes import RECIPES
from helpers import (
    get_recipe_emoji,
    get_recipe_image,
)

from sidebar import create_sidebar
from timer import TimerManager
from hero_card import (
    create_hero_card,
    TimerRing,
)

from buttons import (
    create_start_button,
    create_stop_button,
)

from search_bar import create_search_controls
from suggestions import create_suggestions
from recipes_page import create_recipes_page


def main(page: ft.Page):
    page.title = "CookFlow"
    page.window.width = 1600
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
        no_wrap=False,
        max_lines=2,
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

    timer_ring = TimerRing(timer_text, timer_status)

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

    autocomplete_list = ft.Column(
        spacing=6,
    )

    autocomplete_box = ft.Container(
        width=620,
        padding=10,
        border_radius=18,
        bgcolor="#111827",
        border=ft.border.all(1, "#1F2937"),
        visible=False,
        content=autocomplete_list,
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
        timer_ring,
    )

    def hide_autocomplete():
        autocomplete_list.controls.clear()
        autocomplete_box.visible = False

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
        timer_ring.set_idle()

        hide_autocomplete()
        page.update()

    def select_autocomplete_recipe(recipe_key):
        search_input.value = RECIPES[recipe_key].name
        select_recipe(recipe_key)

    def update_autocomplete(e):
        user_input = search_input.value.strip().lower()

        autocomplete_list.controls.clear()

        if not user_input:
            hide_autocomplete()
            page.update()
            return

        matches = [
            recipe_key
            for recipe_key, recipe in RECIPES.items()
            if user_input in recipe_key.lower()
            or user_input in recipe.name.lower()
        ]

        if not matches:
            hide_autocomplete()
            page.update()
            return

        for recipe_key in matches[:6]:
            recipe = RECIPES[recipe_key]
            emoji = get_recipe_emoji(recipe_key)

            if recipe.temperature is not None:
                details = f"{recipe.cooking_time} min • {recipe.temperature} °C"
            else:
                details = f"{recipe.cooking_time} min • No oven"

            autocomplete_list.controls.append(
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(emoji, size=22),
                            ft.Column(
                                controls=[
                                    ft.Text(
                                        recipe.name,
                                        size=15,
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                    ft.Text(
                                        details,
                                        size=12,
                                        color="#9CA3AF",
                                    ),
                                ],
                                spacing=2,
                            ),
                        ],
                        spacing=12,
                    ),
                    padding=12,
                    border_radius=14,
                    bgcolor="#0F172A",
                    on_click=lambda e, key=recipe_key: select_autocomplete_recipe(key),
                )
            )

        autocomplete_box.visible = True
        page.update()

    def search_recipe(e):
        user_input = search_input.value.strip().lower()
        select_recipe(user_input)

    search_input, search_bar = create_search_controls(search_recipe)
    search_input.on_change = update_autocomplete

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
        timer_ring,
    )

    suggestions_title, suggestion_cards = create_suggestions(select_recipe)

    timer_page_content = ft.Column(
        controls=[
            headline,
            subtitle,
            search_bar,
            hero_card,
            suggestions_title,
            suggestion_cards,
        ],
        spacing=16,
    )

    timer_page = ft.Container(
        expand=True,
        padding=40,
        content=ft.Stack(
            controls=[
                timer_page_content,
                ft.Container(
                    content=autocomplete_box,
                    top=146,
                    left=0,
                ),
            ],
        ),
    )

    content_area = ft.Container(expand=True)

    def show_timer_page():
        content_area.content = timer_page
        page.update()

    def show_recipes_page():
        hide_autocomplete()

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