import sys


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory = {}

    for i in range(1, len(sys.argv)):
        arg = sys.argv[i]

        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        parts = arg.split(":")
        key = parts[0].strip()
        value_str = parts[1].strip()

        if key in inventory:
            print(f"Redundant item '{key}' - discarding")
            continue

        try:
            value = int(value_str)
            inventory[key] = value
        except ValueError as e:
            print(f"Quantity error for '{key}': {e}")

    if len(inventory) == 0:
        return

    print(f"Got inventory: {inventory}")

    key_list = list(inventory.keys())
    print(f"Item list: {key_list}")

    total_quantity = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_quantity}")

    for key, value in inventory.items():
        percentage = (value / total_quantity) * 100
        print(f"Item {key} represents {percentage:.1f}%")

    most_abundant_key = None
    least_abundant_key = None

    for key in key_list:
        value = inventory[key]

        if most_abundant_key is None or value > inventory[most_abundant_key]:
            most_abundant_key = key

        if least_abundant_key is None or value < inventory[least_abundant_key]:
            least_abundant_key = key

    assert most_abundant_key is not None
    assert least_abundant_key is not None

    print(f"Item most abundant: {most_abundant_key} with quantity "
          f"{inventory[most_abundant_key]}")

    print(f"Item least abundant: {least_abundant_key} with quantity "
          f"{inventory[least_abundant_key]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
