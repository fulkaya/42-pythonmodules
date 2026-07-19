from ex0 import CreatureFactory, FlameFactory, AquaFactory


flame_factory = FlameFactory()
aqua_factory = AquaFactory()


def test_factory(factory: CreatureFactory) -> None:
    creature = factory.create_base()
    evolved = factory.create_evolved()
    print(creature.describe())
    print(creature.attack())
    print(evolved.describe())
    print(evolved.attack())


def fight_factory(factory: CreatureFactory, factory2: CreatureFactory) -> None:
    creature = factory.create_base()
    creature2 = factory2.create_base()
    print(creature.describe())
    print("vs.")
    print(creature2.describe())
    print("fight!")
    print(creature.attack())
    print(creature2.attack())


if __name__ == "__main__":
    print("Testing factory")
    test_factory(flame_factory)
    print()
    print("Testing factory")
    test_factory(aqua_factory)
    print()
    print("Testing battle")
    fight_factory(flame_factory, aqua_factory)
