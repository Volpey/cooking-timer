import flet as ft


def recipe_card(name, details, image_src, on_click):
    recipe_image = ft.Image(
        src=image_src,
        width=58,
        height=58,
        fit=ft.ImageFit.COVER,
    )

    return ft.Container(
        width=210,
        height=92,
        padding=10,
        border_radius=18,
        bgcolor="#111827",
        border=ft.border.all(1, "#1F2937"),
        on_click=on_click,
        content=ft.Row(
            controls=[
                ft.Container(
                    width=58,
                    height=58,
                    border_radius=14,
                    clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                    bgcolor="#1F2937",
                    content=recipe_image,
                ),
                ft.Column(
                    controls=[
                        ft.Text(
                            name,
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            max_lines=1,
                            overflow=ft.TextOverflow.ELLIPSIS,
                        ),
                        ft.Text(
                            details,
                            size=12,
                            color="#9CA3AF",
                        ),
                    ],
                    spacing=4,
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True,
                ),
            ],
            spacing=12,
        ),
    )