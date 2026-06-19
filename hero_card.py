import flet as ft


class TimerRing:
    def __init__(self, timer_text, timer_status):
        self.glow_outer = ft.Container(
            width=290,
            height=290,
            border_radius=999,
            bgcolor="#148B5CF6",
        )

        self.glow_inner = ft.Container(
            width=260,
            height=260,
            border_radius=999,
            bgcolor="#18EC4899",
        )

        self.ring = ft.Container(
            width=235,
            height=235,
            border_radius=999,
            border=ft.border.all(8, "#A855F7"),
            shadow=ft.BoxShadow(
                blur_radius=65,
                spread_radius=3,
                color="#668B5CF6",
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
                        ft.Text("🔥", size=24, color="#F87171"),
                        timer_text,
                        timer_status,
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=6,
                ),
            ),
        )

        self.control = ft.Container(
            width=300,
            height=300,
            alignment=ft.alignment.center,
            content=ft.Stack(
                controls=[
                    self.glow_outer,
                    self.glow_inner,
                    self.ring,
                ],
                alignment=ft.alignment.center,
            ),
        )

    def set_idle(self):
        self.glow_outer.width = 290
        self.glow_outer.height = 290
        self.glow_outer.bgcolor = "#148B5CF6"

        self.glow_inner.width = 260
        self.glow_inner.height = 260
        self.glow_inner.bgcolor = "#18EC4899"

        self.ring.width = 235
        self.ring.height = 235
        self.ring.border = ft.border.all(8, "#A855F7")

    def set_pulse(self, active):
        if active:
            self.glow_outer.width = 305
            self.glow_outer.height = 305
            self.glow_outer.bgcolor = "#228B5CF6"

            self.glow_inner.width = 275
            self.glow_inner.height = 275
            self.glow_inner.bgcolor = "#28EC4899"

            self.ring.width = 242
            self.ring.height = 242
            self.ring.border = ft.border.all(9, "#EC4899")
        else:
            self.glow_outer.width = 290
            self.glow_outer.height = 290
            self.glow_outer.bgcolor = "#148B5CF6"

            self.glow_inner.width = 260
            self.glow_inner.height = 260
            self.glow_inner.bgcolor = "#18EC4899"

            self.ring.width = 235
            self.ring.height = 235
            self.ring.border = ft.border.all(8, "#A855F7")


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