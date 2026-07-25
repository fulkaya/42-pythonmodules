import os
import site
import sys


def is_in_venv() -> bool:
    return sys.prefix != sys.base_prefix


def main() -> None:
    current_python = sys.executable
    if not is_in_venv():
        print("MATRIX STATUS: You're still plugged in")
        print()
        print(f"Current Python: {current_python}")
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print()
        print("Then run this program again.")
    else:
        env_path = sys.prefix
        env_name = os.path.basename(env_path)

        site_packages = site.getsitepackages()
        pkg_path = site_packages[0] if site_packages else "Unknown"

        print("MATRIX STATUS: Welcome to the construct")
        print()
        print(f"Current Python: {current_python}")
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {env_path}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print()
        print("Package installation path:")
        print(f"{pkg_path}")


if __name__ == "__main__":
    main()
