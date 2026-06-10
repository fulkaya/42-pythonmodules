#!/usr/bin/env python3

class Plant:

    def __init__(self, name: str, height: float, age: int) -> None:

        self.name = name

        if height < 0:
            print(f"{self.name.capitalize()}: Error, height "
                  f"can't be negative")
            self._height = 0.0
        else:
            self._height = height

        if age < 0:
            print(f"{self.name.capitalize()}: Error, age can't "
                  f"be negative")
            self._age = 0
        else:
            self._age = age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name.capitalize()}: Error, height "
                  f"can't be negative\nHeight update rejected")
        else:
            self._height = height
            print(f"Height updated: {round(self._height)}cm")

    def get_height(self) -> float:
        return self._height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name.capitalize()}: Error, age can't "
                  f"be negative\nAge update rejected\n")
        else:
            self._age = age
            print(f"Age updated: {self._age} days\n")

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"Plant created: {self.name.capitalize()}: "
              f"{self._height}cm, {self._age} days old\n")

    def show_last(self) -> None:
        print(f"Current state: {self.name.capitalize()}: "
              f"{self._height}cm, {self._age} days old\n")


def main() -> None:

    print("=== Garden Security System ===")
    rose = Plant("rose", 15.0, 10)
    rose.show()
    rose.set_height(25.0)
    rose.get_height()
    rose.set_age(30)
    rose.get_age()

    rose.set_height(-25.0)
    rose.set_age(-30)

    rose.show_last()


if __name__ == "__main__":
    main()
