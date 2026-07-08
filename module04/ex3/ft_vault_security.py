def secure_archive(filename: str, action: str = "read",
                   content: str = "") -> tuple[bool, str]:

    if action == "read":
        try:
            with open(filename, "r") as file_object:
                content = file_object.read()
            return (True, content)
        except (FileNotFoundError, PermissionError) as e:
            return (False, str(e))

    elif action == "write":
        try:
            with open(filename, "w") as file_object:
                file_object.write(content)
            return (True, 'Content successfully written to file')
        except Exception as e:
            return (False, str(e))

    return (False, "Invalid action")


def main() -> None:
    print("=== Cyber Archives Security ===")
    print()

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "read"), end="\n\n")

    print("Using 'secure_archive' to read from an inaccessile file:")
    print(secure_archive("/etc/master.passwd", "read"), end="\n\n")

    print("Using 'secure_archive' to read from a regular file:")
    a = secure_archive("archive_vault.txt", "read")
    print(a, end="\n\n")

    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("text.txt", "write", a[1]))


if __name__ == "__main__":
    main()
