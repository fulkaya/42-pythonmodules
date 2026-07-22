from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy, NormalStrategy,
    AggressiveStrategy, DefensiveStrategy,
    InvalidStrategyError)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    print()
    is_first_battle = True

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            c1 = factory1.create_base()
            c2 = factory2.create_base()

            if not is_first_battle:
                print()

            print("* Battle *")
            print(c1.describe())
            print("vs.")
            print(c2.describe())
            print("now fight!")

            try:
                actions1 = strategy1.act(c1)
                actions2 = strategy2.act(c2)

                for act in actions1:
                    print(act)
                for act in actions2:
                    print(act)
                is_first_battle = False
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([(flame_factory, normal), (healing_factory, defensive)])
    print()

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([(flame_factory, aggressive), (healing_factory, defensive)])
    print()

    print("Tournament 2 (multiple)")
    print("[ (Aquabob+Normal), (Healing+Defensive), (Transform+Agressive) ]")
    battle([(aqua_factory, normal), (healing_factory, defensive),
            (transform_factory, aggressive)])
