import elements
from alchemy.elements import create_air
from alchemy.potions import strength_potion


def lead_to_gold() -> str:
    x = (
        f"Recipe transmuting Lead to Gold: brew '{create_air()}' "
        f"and '{strength_potion()}' mixed with '{elements.create_fire()}'"
    )
    return x
