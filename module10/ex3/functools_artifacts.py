from collections.abc import Callable
from typing import Any
from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    operations: dict[str, Callable] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")
    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": partial(base_enchantment, 50, "fire"),
        "ice": partial(base_enchantment, 50, "ice"),
        "lightning": partial(base_enchantment, 50, "lightning")}


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Fibonacci index cannot be negative")
    if n in (0, 1):
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register(int)
    def _(damage: int) -> str:
        return f"Damage spell: {damage} damage"

    @dispatch.register(str)
    def _(enchantment: str) -> str:
        return f"Enchantment: {enchantment}"

    @dispatch.register(list)
    def _(spells: list[Any]) -> str:
        return f"Multi-cast: {len(spells)} spells"

    return dispatch


if __name__ == "__main__":
    print("Testing spell reducer...")
    list_a: list[int] = [10, 20, 30, 40]
    sum_ = spell_reducer(list_a, "add")
    print(f"Sum: {sum_}")
    multiply_ = spell_reducer(list_a, "multiply")
    print(f"Product: {multiply_}")
    max_ = spell_reducer(list_a, "max")
    print(f"Max: {max_}")

    print()
    print("Testing partial enchanter...")

    def base_enchant(power: int, element: str, target: str) -> str:
        return f"{element.capitalize()} {target} with {power} power"

    enhanct_dict = partial_enchanter(base_enchant)
    fire_func = enhanct_dict["fire"]
    print(fire_func("Sword"))
    ice_func = enhanct_dict["ice"]
    print(ice_func("Staff"))
    lightning_func = enhanct_dict["lightning"]
    print(lightning_func("Shield"))

    print()
    print("Testing memoized fibonacci...")
    n0 = memoized_fibonacci(0)
    n1 = memoized_fibonacci(1)
    n10 = memoized_fibonacci(10)
    n15 = memoized_fibonacci(15)
    print(f"Fib(0): {n0}")
    print(f"Fib(1): {n1}")
    print(f"Fib(10): {n10}")
    print(f"Fib(15): {n15}")

    print()
    print("Testing spell dispatcher...")
    spell = spell_dispatcher()
    print(spell(42))
    print(spell("fireball"))
    spell_list = ["heal", "fireball", "freeze"]
    print(spell(spell_list))
    print(spell(10.0))
