from ex0 import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1 import HealCapability, TransformCapability

healing_factory = HealingCreatureFactory()
transform_factory = TransformCreatureFactory()


def test_factory(factory: CreatureFactory) -> None:
    creature = factory.create_base()
    evolved = factory.create_evolved()

    print("base:")
    print(creature.describe())
    print(creature.attack())

    if isinstance(creature, HealCapability):
        print(creature.heal())

    if isinstance(creature, TransformCapability):
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())

    print("evolved:")
    print(evolved.describe())
    print(evolved.attack())

    if isinstance(evolved, HealCapability):
        print(evolved.heal())

    if isinstance(evolved, TransformCapability):
        print(evolved.transform())
        print(evolved.attack())
        print(evolved.revert())


if __name__ == "__main__":
    print("Testing Creature with healing capability")
    test_factory(healing_factory)
    print()
    print("Testing Creature with transform capability")
    test_factory(transform_factory)
