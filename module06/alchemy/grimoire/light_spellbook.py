def light_spell_allowed_ingredients() -> list[str]:
    magic_list = ["earth", "air", "fire", "water"]
    return magic_list


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from alchemy.grimoire.light_validator import validate_ingredients

    validator_result: str = validate_ingredients(ingredients)
    if "VALID" in validator_result:
        return f"{spell_name} is RECORDED"
    return f"{spell_name} is REJECTED"
