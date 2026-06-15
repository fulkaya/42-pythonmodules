import sys


def main() -> None:
    print("=== Player Score Analytics ===")

    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        return

    valid_scores = []

    for i in range(1, len(sys.argv)):
        current_input = sys.argv[i]
        try:
            score = int(current_input)
            valid_scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{current_input}'")

    if len(valid_scores) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        return

    total_players = len(valid_scores)
    total_score = sum(valid_scores)
    average_score = total_score / total_players
    high_score = max(valid_scores)
    low_score = min(valid_scores)
    score_range = high_score - low_score

    print(f"Scores processed: {valid_scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    main()
