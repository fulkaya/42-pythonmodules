import math


def get_player_pos() -> tuple:
    while True:
        user_input = input("Enter new coordinates as "
                           "floats in format 'x,y,z': ")

        parts = user_input.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue

        try:
            x = float(parts[0].strip())
            y = float(parts[1].strip())
            z = float(parts[2].strip())

            return (x, y, z)

        except ValueError as e:
            error_message = str(e)
            bad_part = error_message.split(":")[-1].strip()
            print(f"Error on parameter {bad_part}: {error_message}")


def main() -> None:
    print("=== Game Coordinate System ===")
    print()

    print("Get a first set of coordinates")
    p1 = get_player_pos()

    print(f"Got a first tuple: {p1}")
    print(f"It includes: X={p1[0]}, Y={p1[1]}, Z={p1[2]}")

    dist_to_center = math.sqrt(p1[0]**2 + p1[1]**2 + p1[2]**2)
    print(f"Distance to center: {round(dist_to_center, 4)}")

    print()
    print("Get a second set of coordinates")
    p2 = get_player_pos()

    dist_between = math.sqrt(
            (p2[0] - p1[0])**2 +
            (p2[1] - p1[1])**2 +
            (p2[2] - p1[2])**2
    )
    print(f"Distance between the 2 sets of coordinates: "
          f"{round(dist_between, 4)}")


if __name__ == "__main__":
    main()
