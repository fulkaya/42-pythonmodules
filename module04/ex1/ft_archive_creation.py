import sys
import typing


def read_file_content(filename: str) -> str:
    file_object: typing.IO[str] = open(filename, "r")
    content = file_object.read()
    file_object.close()
    return content


def transform_data(content: str) -> str:
    lines: list[str] = content.splitlines()
    transformed_lines = (f"{line}#" for line in lines if line.strip())
    new_content = "\n".join(transformed_lines)
    return new_content


def save_to_file(filename: str, content: str) -> None:
    new_file: typing.IO[str] = open(filename, "w")
    new_file.write(content)
    new_file.close()


def main() -> None:
    program_name = sys.argv[0]

    if len(sys.argv) == 1:
        print(f"Usage: {program_name} <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{sys.argv[1]}'")

    try:
        content: str = read_file_content(sys.argv[1])
        print("---", end="\n\n")
        print(content, end="\n\n")
        print("---")
        print(f"File '{sys.argv[1]}' closed.", end="\n\n")

        print("Transform data:")
        print("---", end="\n\n")
        new_content: str = transform_data(content)
        print(new_content, end="\n\n")
        print("---")

        new_name = input("Enter new file name (or empty): ")
        if new_name.strip() == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_name}'")
            save_to_file(new_name, new_content)
            print(f"Data saved in file '{new_name}'.")

    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    except BaseException:
        print("\nInput error")


if __name__ == "__main__":
    main()
