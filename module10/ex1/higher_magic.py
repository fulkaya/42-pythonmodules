from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda target, power: (spell1(target, power), spell2(target, power))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda target, power: base_spell(target, power * multiplier)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return lambda target, power: (
        spell(target, power) if condition(target, power) else "Spell fizzled")


def spell_sequence(spells: list[Callable]) -> Callable:
    return lambda target, power: [s(target, power) for s in spells]


if __name__ == "__main__":
    print("Testing spell combiner...")
    combo = spell_combiner(heal, fireball)
    spell1, spell2 = combo("Dragon", 20)
    print(f"{spell1}, {spell2}")

    print()
    print("Testing power amplifier...")
    multiplier = power_amplifier(heal, 15)
    spell = multiplier("Dragon", 20)
    print(f"{spell}")

    print()
    print("Testing conditional caster...")
    conditional_spell = conditional_caster(
        lambda target, power: power >= 50, fireball)
    spell_ = conditional_spell("Dragon", 20)
    print(f"{spell_}")

    print()
    print("Testing spell sequence...")
    spells = spell_sequence([heal, fireball])
    spell_list = spells("Dragon", 20)
    for item in spell_list:
        print(f"{item}")
