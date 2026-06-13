class PlantError(Exception):
    def __init__(self, message: str = "Unknown plant error"):
        self.message = message
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print()
    print("Testing valid plants...")

    try:
        print("Opening watering system")
        valid_inputs = ['Tomato', 'Lettuce', 'Carrots']
        for plant in valid_inputs:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")

    print()
    print("Testing invalid plants...")

    try:
        print("Opening watering system")
        invalid_inputs = ['Tomato', 'lettuce', 'Carrots']
        for plant in invalid_inputs:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    test_watering_system()

    print()
    print("Cleanup always happens, even with errors!")
