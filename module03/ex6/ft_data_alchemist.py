import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    initial_players: list[str] = [
        "Alice", "bob", "Charlie", "dylan", "Emma",
        "Gregory", "john", "kevin", "Liam"
    ]
    print(f"Initial list of players: {initial_players}")

    all_capitalized: list[str] = [
        name.capitalize() for name in initial_players
    ]
    print(f"New list with all names capitalized: {all_capitalized}")

    only_originally_capitalized: list[str] = [
        name for name in initial_players if name[0].isupper()
    ]
    print(f"New list of capitalized names only: {only_originally_capitalized}")

    score_dict: dict[str, int] = {
        name: random.randint(50, 1000) for name in all_capitalized
    }
    print(f"Score dict: {score_dict}")

    total_score: int = sum(score_dict.values())
    player_count: int = len(score_dict)
    average_score: float = round(total_score / player_count, 2)
    print(f"Score average is {average_score}")

    high_scores: dict[str, int] = {
        name: score for name, score in score_dict.items()
        if score > average_score
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
