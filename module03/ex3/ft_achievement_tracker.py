import random


def gen_player_achievements(master_list: list[str]) -> set[str]:
    num_to_pick = random.randint(5, 9)
    picked = random.sample(master_list, num_to_pick)
    return set(picked)


def main() -> None:
    print("=== Achievement Tracker System ===")
    print()

    master_achievement = [
        "Crafting Genius", "World Savior", "Master Explorer",
        "Collector Supreme", "Untouchable", "Boss Slayer",
        "Unstoppable", "Strategist", "Speed Runner", "Survivor",
        "Treasure Hunter", "First Steps", "Sharp Mind",
        "Hidden Path Finder"
    ]

    alice = gen_player_achievements(master_achievement)
    bob = gen_player_achievements(master_achievement)
    charlie = gen_player_achievements(master_achievement)
    dylan = gen_player_achievements(master_achievement)

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print()

    all_distinct = alice.union(bob, charlie, dylan)
    print(f"All distinct achievements: {all_distinct}")
    print()

    common = alice.intersection(bob, charlie, dylan)
    print(f"Common achievements: {common}")
    print()

    only_alice = alice.difference(bob.union(charlie, dylan))
    only_bob = bob.difference(alice.union(charlie, dylan))
    only_charlie = charlie.difference(alice.union(bob, dylan))
    only_dylan = dylan.difference(alice.union(bob, charlie))

    print(f"Only Alice has: {only_alice}")
    print(f"Only Bob has: {only_bob}")
    print(f"Only Charlie has: {only_charlie}")
    print(f"Only Dylan has: {only_dylan}")
    print()

    master_set = set(master_achievement)
    print(f"Alice is missing: {master_set.difference(alice)}")
    print(f"Bob is missing: {master_set.difference(bob)}")
    print(f"Charlie is missing: {master_set.difference(charlie)}")
    print(f"Dylan is missing: {master_set.difference(dylan)}")


if __name__ == "__main__":
    main()
