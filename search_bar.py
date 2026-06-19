import flet as ft


def create_search_controls(search_recipe):
    search_input = ft.TextField(
        hint_text="Search for a recipe...",
        width=620,
        height=54,
        border_radius=18,
        bgcolor="#0F172A",
        border_color="#334155",
        focused_border_color="#8B5CF6",
        color="#FFFFFF",
        cursor_color="#A855F7",
        content_padding=ft.padding.symmetric(
            horizontal=16,
            vertical=12,
        ),
    )

    search_input.on_submit = search_recipe

    search_button = ft.Container(
        width=54,
        height=54,
        border_radius=18,
        bgcolor="#7C3AED",
        alignment=ft.alignment.center,
        shadow=ft.BoxShadow(
            blur_radius=22,
            spread_radius=1,
            color="#607C3AED",
            offset=ft.Offset(0, 8),
        ),
        content=ft.Icon(
            ft.Icons.ARROW_FORWARD,
            size=24,
            color="#FFFFFF",
        ),
        on_click=search_recipe,
    )

    search_bar = ft.Container(
        height=76,
        padding=ft.padding.symmetric(horizontal=18),
        border_radius=24,
        bgcolor="#111827",
        border=ft.border.all(1, "#263244"),
        content=ft.Row(
            controls=[
                ft.Icon(
                    ft.Icons.SEARCH,
                    size=24,
                    color="#94A3B8",
                ),
                search_input,
                search_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=14,
        ),
    )

    return search_input, search_bar