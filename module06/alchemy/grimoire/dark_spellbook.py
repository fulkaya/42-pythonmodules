from alchemy.grimoire.dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    magic_list = ["bats", "frogs", "arsenic", "eyeball"]
    return magic_list


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validator_result: str = validate_ingredients(ingredients)
    if "INVALID" in validator_result:
        return f"Spell rejected: {spell_name} ({validator_result})"
    return f"Spell recorded: {spell_name} ({validator_result})"
