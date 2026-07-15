from elements import create_water, create_fire
from alchemy.elements import create_air, create_earth


def healing_potion() -> str:
    x = f"Healing potion brewed with '{create_earth()}' and '{create_air()}'"
    return x


def strength_potion() -> str:
    x = f"Strength potion brewed with '{create_fire()}' and '{create_water()}'"
    return x
