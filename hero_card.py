import flet as ft


class TimerRing:
    def __init__(self, timer_text, timer_status):
        self.progress = ft.ProgressRing(
            width=250,
            height=250,
            stroke_width=9,
            value=1.0,
            color="#A855F7",
            bgcolor="#243044",
        )

        self.glow = ft.Container(
            width=270,
            height=270,
            border_radius=999,
            bgcolor="#168B5CF6",
        )

        self.control = ft.Container(
            width=300,
            height=300,
            alignment=ft.alignment.center,
            content=ft.Stack(
                controls=[
                    self.glow,
                    self.progress,
                    ft.Container(
                        width=215,
                        height=215,
                        border_radius=999,
                        bgcolor="#0B1020",
                        alignment=ft.alignment.center,
                        content=ft.Column(
                            controls=[
                                ft.Text("🔥", size=24, color="#F87171"),
                                timer_text,
                                timer_status,
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=6,
                        ),
                    ),
                ],
                alignment=ft.alignment.center,
            ),
        )

    def set_idle(self):
        self.progress.value = 1.0
        self.progress.color = "#A855F7"
        self.glow.bgcolor = "#168B5CF6"

    def set_running(self, progress):
        self.progress.value = progress
        self.progress.color = "#A855F7"
        self.glow.bgcolor = "#168B5CF6"

    def set_done(self):
        self.progress.value = 0.0
        self.progress.color = "#22C55E"
        self.glow.bgcolor = "#1622C55E"

    def set_stopped(self):
        self.progress.color = "#94A3B8"
        self.glow.bgcolor = "#1094A3B8"


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


def create_hero_card(
    recipe_title,
    time_info,
    temp_info,
    timer_text,
    timer_status,
    start_button,
    stop_button,
    recipe_image,
    timer_ring,
):
    recipe_info = ft.Container(
        width=260,
        content=ft.Column(
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
                ft.Container(
                    width=260,
                    content=recipe_title,
                ),
                ft.Container(height=8),
                ft.Divider(color="#243044"),
                info_box("⏱", time_info, "Cooking time"),
                info_box("🌡", temp_info, "Temperature"),
            ],
            spacing=14,
        ),
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
                        timer_ring.control,
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