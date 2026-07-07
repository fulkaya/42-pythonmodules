def secure_archive(filename: str, action: str = "read", content: str = "") -> tuple[bool, str]:

    if action == "read":
        try:
            with open(filename, "r"):
                data = filename.read()
            return (True, data)
        except FileNotFoundError as e:
            return (False, str(e))
    
    elif action == "write":
        try:
            with open(filename, "w")
                filename.write(content)
            return(True, 'Content successfully written to file')
        except Exception as e:
            return (False, str(e))

def main() -> None:
    print("=== Cyber Archives Security ===")
    print()

    