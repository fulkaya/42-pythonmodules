def input_temperature(temp_str: str) -> int:
    value = int(temp_str)

    if value > 40:
        raise ValueError(f"{temp_str}°C is too hot for plants (max 40°C)")
    elif value < 0:
        raise ValueError(f"{temp_str}°C is too cold for plants (min 0°C)")
    else:
        return value


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    print()

    test_inputs = ['25', 'abc', '100', '-50']

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
