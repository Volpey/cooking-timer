import flet as ft


def create_search_controls(search_recipe):
    search_input = ft.TextField(
        hint_text="Search for a recipe...",
        width=500,
        height=54,
        border_radius=18,
        bgcolor="#111827",
        border_color="#1F2937",
        focused_border_color="#7C3AED",
        color="#FFFFFF",
    )

    search_input.on_submit = search_recipe

    search_button = ft.Container(
        content=ft.Text("→", size=26),
        width=52,
        height=52,
        alignment=ft.alignment.center,
        border_radius=16,
        bgcolor="#7C3AED",
        on_click=search_recipe,
    )

    search_bar = ft.Container(
        height=64,
        padding=ft.padding.symmetric(horizontal=22),
        border_radius=20,
        bgcolor="#111827",
        border=ft.border.all(1, "#1F2937"),
        content=ft.Row(
            controls=[
                ft.Text("⌕", size=26, color="#9CA3AF"),
                search_input,
                ft.Container(expand=True),
                search_button,
            ]
        ),
    )

    return search_input, search_bar