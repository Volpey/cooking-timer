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
        "nudeln": "assets/nudeln.png",
        "reis": "assets/reis.png",
        "brot": "assets/brot.png",
        "brownies": "assets/brownies.png",
        "muffins": "assets/muffins.png",
        "lachs": "assets/lachs.png",
        "hähnchenbrust": "assets/haehnchenbrust.png",
        "hähnchenschenkel": "assets/haehnchenschenkel.png",
        "brötchen": "assets/broetchen.png",
        "baguette": "assets/baguette.png",
        "brezeln": "assets/brezeln.png",
        "croissant": "assets/croissant.png",
        "pizza brötchen": "assets/pizza_broetchen.png",
        "auflauf": "assets/auflauf.png",
        "cannelloni": "assets/cannelloni.png",
        "fischstäbchen": "assets/fischstaebchen.png",
        "franzbrötchen": "assets/franzbroetchen.png",
        "hot dogs": "assets/hot_dogs.png",
        "kartoffeln": "assets/kartoffeln.png",
        "ofenkartoffeln": "assets/ofenkartoffeln.png",
        "kartoffelgratin": "assets/kartoffelgratin.png",
        "blumenkohl": "assets/blumenkohl.png",
        "brokkoli": "assets/brokkoli.png",
        "spargel": "assets/spargel.png",
        "chicken nuggets": "assets/chicken_nuggets.png",
        "mac and cheese": "assets/mac_and_cheese.png",
        "mozzarella sticks": "assets/mozzarella_sticks.png",
        "onion rings": "assets/onion_rings.png",
        "nachos": "assets/nachos.png",
        "apfelkuchen": "assets/apfelkuchen.png",
        "quiche": "assets/quiche.png",
    }

    return images.get(recipe_key, "assets/pizza.png")