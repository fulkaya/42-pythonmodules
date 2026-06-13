class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error"):
        self.message = message
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        self.message = message
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error"):
        self.message = message
        super().__init__(message)


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
    print()
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
    print()
    print("Testing catching all garden errors...")

    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught {GardenError.__name__}: {e}")

    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught {GardenError.__name__}: {e}")
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
