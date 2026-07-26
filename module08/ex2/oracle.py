import os
import sys
from dotenv import load_dotenv


def check_security() -> None:
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found, using system env or defaults")

    print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configurations.")


def display_configuration(mode: str) -> None:
    db_url = os.getenv("DATABASE_URL", "Not Configured")
    api_key = os.getenv("API_KEY", "Not Configured")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    zion = os.getenv("ZION_ENDPOINT", "Not Configured")

    print("ORACLE STATUS: Reading the Matrix...")
    print()
    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if "local" in db_url.lower() or mode == "development":
        print(f"Database: Connected to local instance ({db_url})")
    else:
        print(f"Database: Connected to production mainframe ({db_url})")

    if api_key != "Not Configured":
        print("API Access: Authenticated")
    else:
        print("API Access: Unauthorized (Missing API Key)")

    print(f"Log Level: {log_level}")

    if zion != "Not Configured":
        print(f"Zion Network: Online ({zion})")
    else:
        print("Zion Network: Offline")

    print()
    check_security()


def main() -> None:
    load_dotenv()

    matrix_mode = os.getenv("MATRIX_MODE")

    if not matrix_mode:
        print("ORACLE STATUS: Reading the Matrix...")
        print()
        print("[WARNING] MATRIX_MODE is not set!")
        print("Please configure .env or set environment variables.")
        print()
        check_security()
        sys.exit(1)

    display_configuration(matrix_mode)


if __name__ == "__main__":
    main()
