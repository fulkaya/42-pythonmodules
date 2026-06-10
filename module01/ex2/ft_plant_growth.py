#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float) -> None:
        self.name = name
        self.height = height
        self.agenow = age
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {round(self.height, 1)}cm, "
              f"{self.agenow} days old")

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self.agenow += 1


def main() -> None:
    rose = Plant("rose", 25.0, 30, 0.8)
    start_height = rose.height
    print("=== Garden Plant Growth ===")
    rose.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow()
        rose.age()
        rose.show()
    total_growth = rose.height - start_height
    print(f"Growth this week: {round(total_growth, 1)}cm")


if __name__ == "__main__":
    main()
