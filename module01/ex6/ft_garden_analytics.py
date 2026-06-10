#!/usr/bin/env python3

class Plant:
    class Analytics:
        def __init__(self) -> None:
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self, name: str) -> None:
            print(f"[statistics for {name.capitalize()}]")
            print(f"Stats: {self.grow_calls} grow, {self.age_calls}"
                  f" age, {self.show_calls} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self._age = age
        self._stats = self.Analytics()

    def display_analytics(self) -> None:
        self._stats.display(self.name)

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> 'Plant':
        return cls("Unknown plant", 0.0, 0)

    def grow(self) -> None:
        self._stats.grow_calls += 1

    def get_age(self) -> int:
        self._stats.age_calls += 1
        return self._age

    def show(self) -> None:
        self._stats.show_calls += 1
        print(f"{self.name.capitalize()}: {self.height}cm, "
              f"{self._age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str,
                 growth_rate: float, age_rate: int) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.growth_rate = growth_rate
        self.age_rate = age_rate
        self.has_bloomed = False

    def grow(self) -> None:
        super().grow()
        self.height += self.growth_rate
        self.has_bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.has_bloomed:
            print(f"{self.name.capitalize()} is blooming beautifully!")
        else:
            print(f"{self.name.capitalize()} has not bloomed yet")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str,
                 growth_rate: float, age_rate: int, seeds: int) -> None:
        super().__init__(name, height, age, color, growth_rate, age_rate)
        self._max_seeds = seeds
        self.seeds = 0

    def grow(self) -> None:
        super().grow()
        if self.has_bloomed:
            self.seeds = self._max_seeds
        self.get_age()
        self._age += self.age_rate

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


class Tree(Plant):
    class TreeAnalytics(Plant.Analytics):
        def __init__(self) -> None:
            super().__init__()
            self.shade_calls = 0

        def display(self, name: str) -> None:
            super().display(name)
            print(f"{self.shade_calls} shade")

    _stats: 'Tree.TreeAnalytics'

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._stats = self.TreeAnalytics()

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name.capitalize()} now produces a shade"
              f" of {self.height}cm long and {self.trunk_diameter}cm wide.")
        self._stats.shade_calls += 1

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


def display_plant_statistics(plant_instance: Plant) -> None:
    plant_instance.display_analytics()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print()

    print("=== Flower")
    rose = Flower("rose", 15.0, 10, "red", 8.0, 0)
    rose.show()
    display_plant_statistics(rose)
    print(f"[asking the {rose.name} to grow and bloom]")
    rose.grow()
    rose.show()
    display_plant_statistics(rose)
    print()

    print("=== Tree")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_statistics(oak)
    oak.produce_shade()
    display_plant_statistics(oak)
    print()

    print("=== Seed")
    sunflower = Seed("sunflower", 80.0, 45, "yellow", 30, 20, 42)
    sunflower.show()
    print(f"[make {sunflower.name} grow, age and bloom]")
    sunflower.grow()
    sunflower.show()
    display_plant_statistics(sunflower)
    print()

    print("=== Anonymous")
    plant = Plant.create_anonymous()
    plant.show()
    display_plant_statistics(plant)
