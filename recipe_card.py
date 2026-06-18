import flet as ft


def recipe_card(name, details, emoji, on_click):
    return ft.Container(
        width=190,
        height=86,
        padding=14,
        border_radius=18,
        bgcolor="#111827",
        border=ft.border.all(1, "#1F2937"),
        on_click=on_click,
        content=ft.Row(
            controls=[
                ft.Container(
                    width=52,
                    height=52,
                    border_radius=14,
                    bgcolor="#1F2937",
                    alignment=ft.alignment.center,
                    content=ft.Text(emoji, size=26),
                ),
                ft.Column(
                    controls=[
                        ft.Text(name, size=16, weight=ft.FontWeight.BOLD),
                        ft.Text(details, size=12, color="#9CA3AF"),
                    ],
                    spacing=4,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            spacing=12,
        ),
    )