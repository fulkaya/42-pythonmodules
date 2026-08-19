from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    count = 0

    def inner_counter() -> int:
        nonlocal count
        count += 1
        return count
    return inner_counter


def spell_accumulator(initial_power: int) -> Callable:
    def inner_accumulator(power: int) -> int:
        nonlocal initial_power
        initial_power += power
        return initial_power
    return inner_accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def inner_factory(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return inner_factory


def memory_vault() -> dict[str, Callable]:
    vault: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        return vault.get(key, "Memory not found")
    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_a call 3: {counter_a()}")

    counter_b = mage_counter()
    print(f"counter_b call 1: {counter_b()}")

    print()
    print("Testing spell accumulator...")
    accumulator = spell_accumulator(100)
    print(f"Base 100, add 20: {accumulator(20)}")
    print(f"Base 100, add 30: {accumulator(30)}")

    print()
    print("Testing enchantment factory...")
    enchantment = enchantment_factory("Flaming")
    print(enchantment("Sword"))
    enchantment2 = enchantment_factory("Frozen")
    print(enchantment2("Shield"))

    print()
    print("Testing memory vault...")
    vault = memory_vault()
    store_function = vault["store"]
    store_function("secret", 42)
    recall_function = vault["recall"]
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {recall_function('secret')}")
    print(f"Recall 'unknown': {recall_function('unknown')}")
