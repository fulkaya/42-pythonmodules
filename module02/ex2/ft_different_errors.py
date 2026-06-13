def garden_operations(operation_number: int) -> None:

    if operation_number == 0:
        int('abc')
    elif operation_number == 1:
        5 / 0
    elif operation_number == 2:
        open('/non/existent/file', 'r')
    elif operation_number == 3:
        "Fulya" + 27  # type: ignore
    else:
        print("Operation completed successfully")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    test_inputs = [0, 1, 2, 3, 4]

    for current_input in test_inputs:
        print(f"Testing operation {current_input}...")

        try:
            garden_operations(current_input)
        except ValueError as e:
            print(f"Caught {e.__class__.__name__}: {e}")
        except ZeroDivisionError as e:
            print(f"Caught {e.__class__.__name__}: {e}")
        except FileNotFoundError as e:
            print(f"Caught {e.__class__.__name__}: {e}")
        except TypeError as e:
            print(f"Caught {e.__class__.__name__}: {e}")

    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
