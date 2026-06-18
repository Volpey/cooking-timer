def get_recipe_emoji(recipe_key):
    emojis = {
        "pizza": "🍕",
        "lasagne": "🍝",
        "kekse": "🍪",
        "pommes": "🍟",
        "nudeln": "🍜",
        "reis": "🍚",
        "brot": "🍞",
        "brownies": "🍫",
        "muffins": "🧁",
        "lachs": "🐟",
        "hähnchenbrust": "🍗",
        "brötchen": "🥐",
    }

    return emojis.get(recipe_key, "🍽")


def get_recipe_image(recipe_key):
    images = {
        "pizza": "assets/pizza.png",
        "lasagne": "assets/lasagne.png",
        "kekse": "assets/kekse.png",
        "pommes": "assets/pommes.png",
        "käsekuchen": "assets/kaesekuchen.png",
    }

    return images.get(
        recipe_key,
        "assets/pizza.png"
    )