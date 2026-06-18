import flet as ft
from recipe_card import recipe_card


def create_suggestions(select_recipe):
    suggestions_title = ft.Text(
        "SUGGESTIONS",
        size=13,
        weight=ft.FontWeight.BOLD,
        color="#A78BFA",
    )

    suggestion_cards = ft.Row(
        controls=[
            recipe_card(
                "Pizza",
                "15 min • 220 °C",
                "🍕",
                lambda e: select_recipe("pizza"),
            ),
            recipe_card(
                "Lasagne",
                "30 min • 180 °C",
                "🍝",
                lambda e: select_recipe("lasagne"),
            ),
            recipe_card(
                "Kekse",
                "12 min • 160 °C",
                "🍪",
                lambda e: select_recipe("kekse"),
            ),
            recipe_card(
                "Pommes",
                "25 min • 200 °C",
                "🍟",
                lambda e: select_recipe("pommes"),
            ),
                recipe_card(
                "Käsekuchen",
                "60 min • 170 °C",
                "🍰",
                lambda e: select_recipe("käsekuchen"),
            ),
        ],
        spacing=18,
    )

    return suggestions_title, suggestion_cards