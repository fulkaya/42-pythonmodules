import sys
import typing


def main() -> None:
    program_name = sys.argv[0]

    if len(sys.argv) == 1:
        print(f"Usage: {program_name} <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{sys.argv[1]}'")

    try:
        file: typing.IO[str] = open(sys.argv[1], "r")
        content = file.read()
        file.close()
        print("---", end="\n\n")
        print(content, end="\n\n")
        print("---")
        print(f"File '{sys.argv[1]}' closed.", end="\n\n")

        print("Transform data:")
        print("---", end="\n\n")
        lines = content.splitlines()
        transformed_lines = (f"{line}#" for line in lines if line.strip())
        new_content = "\n".join(transformed_lines)
        print(new_content, end="\n\n")
        print("---")

        new_name = input("Enter new file name (or empty): ")
        if new_name.strip() == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_name}")
            new_file: typing.IO[str] = open(new_name, "w")
            new_file.write(new_content)
            new_file.close()
            print(f"Data saved in file '{new_name}'.")

    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")


if __name__ == "__main__":
    main()
