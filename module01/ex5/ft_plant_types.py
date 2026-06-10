#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.agenow = age

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}: "
            f"{self.height:.1f}cm, {self.agenow} days old"
        )

    def grow(self) -> None:
        self.height += 1.0

    def age(self) -> None:
        self.agenow += 1


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.has_bloomed = False

    def bloom(self) -> None:
        print(f"[asking the {self.name} to bloom]")
        self.has_bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.has_bloomed:
            print(f"{self.name.capitalize()} is blooming beautifully!")
        else:
            print(f"{self.name.capitalize()} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name.capitalize()} now produces a shade of "
              f"{self.height:.1f}cm long and {self.trunk_diameter:.1f}cm "
              f"wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self) -> None:
        super().grow()
        self.height += 1.1

    def age(self) -> None:
        super().age()
        self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


print("=== Garden Plant Types ===")

print("=== Flower")
rose = Flower("rose", 15.0, 10, "red")
rose.show()
rose.bloom()
rose.show()
print()

print("=== Tree")
tree = Tree("oak", 200.0, 365, 5.0)
tree.show()
tree.produce_shade()
print()

print("=== Vegetable")

vegetable = Vegetable("tomato", 5.0, 10, "April")
vegetable.show()
print(f"[make {vegetable.name} grow and age for 20 days]")
for _ in range(20):
    vegetable.grow()
    vegetable.age()
vegetable.show()
