def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()

    test_inputs = ['25', 'abc']

    for current_input in test_inputs:
        print(f"Input data is '{current_input}'")

        try:
            valid_value = input_temperature(current_input)
            print(f"Temperature is now {valid_value}°C")
            print()
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
            print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
