from alchemy.grimoire.dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    ingredients_lower: str = ingredients.lower()
    for x in dark_spell_allowed_ingredients():
        if x in ingredients_lower:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
