import sys


def main() -> None:
    program_name = sys.argv[0]

    if len(sys.argv) == 1:
        print(f"Usage: {program_name} <file>")
        return

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{sys.argv[1]}'")

    try:
        file_stream = open(sys.argv[1], "r")
        content = file_stream.read()
        file_stream.close()
        print("---", end="\n\n")
        print(content, end="\n\n")
        print("---")
        print(f"File '{sys.argv[1]}' closed.")
    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")


if __name__ == "__main__":
    main()
