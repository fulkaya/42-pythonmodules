import sys


def main() -> None:
    print("=== Command Quest ===")
    program_name = sys.argv[0].split("/")[-1]
    print(f"Program name: {program_name}")

    argc_count = len(sys.argv) - 1

    if argc_count == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {argc_count}")
        for i in range(1, len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")
        print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
