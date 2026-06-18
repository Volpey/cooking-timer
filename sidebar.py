import flet as ft


def create_sidebar(show_timer_page, show_recipes_page):
    active_page = "timer"

    timer_button = ft.Container()
    recipes_button = ft.Container()

    def update_active_button():
        if active_page == "timer":
            timer_button.bgcolor = "#1F2937"
            recipes_button.bgcolor = None
        else:
            timer_button.bgcolor = None
            recipes_button.bgcolor = "#1F2937"

    def on_timer_click(e):
        nonlocal active_page
        active_page = "timer"
        update_active_button()
        show_timer_page()

    def on_recipes_click(e):
        nonlocal active_page
        active_page = "recipes"
        update_active_button()
        show_recipes_page()

    timer_button.content = ft.Row([
        ft.Text("⏱", size=20),
        ft.Text("Timer", size=16),
    ])
    timer_button.padding = 16
    timer_button.border_radius = 16
    timer_button.on_click = on_timer_click

    recipes_button.content = ft.Row([
        ft.Text("📖", size=20),
        ft.Text("Recipes", size=16),
    ])
    recipes_button.padding = 16
    recipes_button.border_radius = 16
    recipes_button.on_click = on_recipes_click

    update_active_button()

    return ft.Container(
        width=240,
        padding=30,
        bgcolor="#090D18",
        border=ft.border.only(right=ft.BorderSide(1, "#1F2937")),
        content=ft.Column(
            controls=[
                ft.Text("🍳 CookFlow", size=24, weight=ft.FontWeight.BOLD),
                ft.Container(height=30),
                timer_button,
                recipes_button,
                ft.Container(expand=True),
            ],
            spacing=18,
        ),
    )