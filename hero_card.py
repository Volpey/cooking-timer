import flet as ft


class TimerRing:
    def __init__(self, timer_text, timer_status):
        self.progress = ft.ProgressRing(
            width=250,
            height=250,
            stroke_width=7,
            value=1.0,
            color="#B56CFF",
            bgcolor="#232A3A",
        )

        self.outer_glow = ft.Container(
            width=292,
            height=292,
            border_radius=999,
            bgcolor="#102A1A5E",
        )

        self.soft_glow = ft.Container(
            width=270,
            height=270,
            border_radius=999,
            bgcolor="#183B1E72",
        )

        self.inner_circle = ft.Container(
            width=218,
            height=218,
            border_radius=999,
            bgcolor="#0A1020",
            alignment=ft.alignment.center,
            shadow=ft.BoxShadow(
                blur_radius=28,
                spread_radius=1,
                color="#90000000",
                offset=ft.Offset(0, 14),
            ),
            content=ft.Column(
                controls=[
                    ft.Text("🔥", size=24, color="#FF6B4A"),
                    timer_text,
                    timer_status,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=8,
            ),
        )

        self.control = ft.Container(
            width=320,
            height=320,
            alignment=ft.alignment.center,
            content=ft.Stack(
                controls=[
                    self.outer_glow,
                    self.soft_glow,
                    ft.Container(
                        width=260,
                        height=260,
                        border_radius=999,
                        bgcolor="#111827",
                    ),
                    self.progress,
                    self.inner_circle,
                ],
                alignment=ft.alignment.center,
            ),
        )

    def set_idle(self):
        self.progress.value = 1.0
        self.progress.color = "#B56CFF"
        self.progress.bgcolor = "#232A3A"
        self.outer_glow.bgcolor = "#102A1A5E"
        self.soft_glow.bgcolor = "#183B1E72"

    def set_running(self, progress):
        self.progress.value = progress
        self.progress.color = "#C084FC"
        self.progress.bgcolor = "#232A3A"
        self.outer_glow.bgcolor = "#143B1E72"
        self.soft_glow.bgcolor = "#208B5CF6"

    def set_done(self):
        self.progress.value = 0.0
        self.progress.color = "#22C55E"
        self.outer_glow.bgcolor = "#1622C55E"
        self.soft_glow.bgcolor = "#2022C55E"

    def set_stopped(self):
        self.progress.color = "#94A3B8"
        self.outer_glow.bgcolor = "#1094A3B8"
        self.soft_glow.bgcolor = "#1494A3B8"


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
        bgcolor="#0F172A",
        border=ft.border.all(1, "#243044"),
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
                    bgcolor="#3B1E72",
                    border=ft.border.all(1, "#6D28D9"),
                ),
                ft.Container(
                    width=260,
                    content=recipe_title,
                ),
                ft.Container(height=8),
                ft.Divider(color="#334155"),
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
            blur_radius=45,
            spread_radius=1,
            color="#80000000",
            offset=ft.Offset(0, 20),
        ),
    )

    timer_section = ft.Column(
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
        spacing=10,
    )

    return ft.Container(
        height=470,
        padding=40,
        border_radius=30,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[
                "#172033",
                "#111827",
                "#0B1020",
            ],
        ),
        border=ft.border.all(1, "#334155"),
        shadow=ft.BoxShadow(
            blur_radius=60,
            spread_radius=2,
            color="#60000000",
            offset=ft.Offset(0, 25),
        ),
        content=ft.Row(
            controls=[
                recipe_info,
                ft.Container(expand=True),
                timer_section,
                ft.Container(expand=True),
                image_container,
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )