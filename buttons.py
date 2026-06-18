import flet as ft


def create_start_button(on_click):
    return ft.Container(
        content=ft.Row(
            controls=[
                ft.Text("▶", size=18, color="#000000"),
                ft.Text(
                    "Start Cooking",
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color="#000000",
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        ),
        width=210,
        height=56,
        border_radius=16,
        bgcolor="#FFFFFF",
        alignment=ft.alignment.center,
        on_click=on_click,
    )


def create_stop_button(on_click):
    return ft.Container(
        content=ft.Row(
            controls=[
                ft.Text("■", size=18, color="#FFFFFF"),
                ft.Text(
                    "Stop Cooking",
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color="#FFFFFF",
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        ),
        width=210,
        height=56,
        border_radius=16,
        bgcolor="#374151",
        alignment=ft.alignment.center,
        on_click=on_click,
    )