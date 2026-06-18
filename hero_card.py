import flet as ft


def info_box(icon, main_text, sub_text):
    return ft.Container(
        content=ft.Row(
            controls=[
                ft.Text(icon, size=22),
                ft.Column(
                    controls=[
                        main_text,
                        ft.Text(sub_text, size=12, color="#9CA3AF"),
                    ],
                    spacing=4,
                ),
            ],
            spacing=12,
        ),
        padding=16,
        border_radius=16,
        bgcolor="#111827",
        width=210,
    )


def create_timer_ring(timer_text, timer_status):
    return ft.Container(
        width=280,
        height=280,
        alignment=ft.alignment.center,
        content=ft.Stack(
            controls=[
                ft.Container(
                    width=280,
                    height=280,
                    border_radius=999,
                    bgcolor="#108B5CF6",
                ),
                ft.Container(
                    width=255,
                    height=255,
                    border_radius=999,
                    bgcolor="#12EC4899",
                ),
                ft.Container(
                    width=235,
                    height=235,
                    border_radius=999,
                    border=ft.border.all(8, "#A855F7"),
                    shadow=ft.BoxShadow(
                        blur_radius=55,
                        spread_radius=2,
                        color="#558B5CF6",
                        offset=ft.Offset(0, 0),
                    ),
                    alignment=ft.alignment.center,
                    content=ft.Container(
                        width=200,
                        height=200,
                        border_radius=999,
                        bgcolor="#0B1020",
                        alignment=ft.alignment.center,
                        content=ft.Column(
                            controls=[
                                ft.Text("♨", size=24, color="#C084FC"),
                                timer_text,
                                timer_status,
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=6,
                        ),
                    ),
                ),
            ],
            alignment=ft.alignment.center,
        ),
    )


def create_hero_card(
    recipe_title,
    time_info,
    temp_info,
    timer_text,
    timer_status,
    start_button,
    stop_button,
    recipe_image,
):
    recipe_info = ft.Column(
        controls=[
            ft.Container(
                content=ft.Text(
                    "CURRENT RECIPE",
                    size=12,
                    color="#E9D5FF",
                    weight=ft.FontWeight.BOLD,
                ),
                padding=ft.padding.symmetric(horizontal=14, vertical=8),
                border_radius=999,
                bgcolor="#306D28D9",
            ),
            recipe_title,
            ft.Container(height=8),
            ft.Divider(color="#243044"),
            info_box("⏱", time_info, "Cooking time"),
            info_box("🌡", temp_info, "Temperature"),
        ],
        spacing=14,
    )

    image_container = ft.Container(
        width=300,
        height=300,
        border_radius=30,
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        alignment=ft.alignment.center,
        content=recipe_image,
        shadow=ft.BoxShadow(
            blur_radius=35,
            spread_radius=1,
            color="#80000000",
            offset=ft.Offset(0, 18),
        ),
    )

    return ft.Container(
        height=470,
        padding=40,
        border_radius=30,
        bgcolor="#111827",
        border=ft.border.all(1, "#2E3A52"),
        shadow=ft.BoxShadow(
            blur_radius=45,
            spread_radius=1,
            color="#90000000",
            offset=ft.Offset(0, 22),
        ),
        content=ft.Row(
            controls=[
                recipe_info,
                ft.Container(expand=True),
                ft.Column(
                    controls=[
                        create_timer_ring(timer_text, timer_status),
                        ft.Row(
                            controls=[
                                start_button,
                                stop_button,
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=16,
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=16,
                ),
                ft.Container(expand=True),
                image_container,
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )