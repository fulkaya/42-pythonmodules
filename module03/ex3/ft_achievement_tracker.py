import random


def gen_player_achievements(master_list: list[str]) -> set[str]:
    num = random.randint(5, 9)
    my_set = random.sample(master_list, num)
    return set(my_set)


def main() -> None:
    print("=== Achievement Tracker System ===")
    print()

    master_achievement: list[str] = [
        "Crafting Genius", "World Savior", "Master Explorer",
        "Collector Supreme", "Untouchable", "Boss Slayer",
        "Unstoppable", "Strategist", "Speed Runner", "Survivor",
        "Treasure Hunter", "First Steps", "Sharp Mind",
        "Hidden Path Finder"
    ]

    alice, bob, charlie, dylan = [
        gen_player_achievements(master_achievement)
        for _ in range(4)]

    player_names = ["alice", "bob", "charlie", "dylan"]
    players = [alice, bob, charlie, dylan]

    for i in range(len(players)):
        print(f"Player {player_names[i].capitalize()}: {players[i]}")
    print()

    all_distinct = alice.union(bob, charlie, dylan)
    print(f"All distinct achievements: {all_distinct}")
    print()

    common = alice.intersection(bob, charlie, dylan)
    print(f"Common achievements: {common}")
    print()

    for i in range(len(players)):
        others: set[str] = set()

        for j in range(len(players)):
            if i != j:
                others = others.union(players[j])

        just = players[i].difference(others)
        print(f"Only {player_names[i].capitalize()} has: {just}")
    print()

    master_set = set(master_achievement)
    for i in range(len(players)):
        print(f"{player_names[i].capitalize()} is missing: "
              f"{master_set.difference(players[i])}")


if __name__ == "__main__":
    main()
