# main.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def main():
    # Retrieve environment variables
    my_env_var = os.getenv(
        "MYENVVAR", "default_value"
    )  # default_value used if MYENVVAR is not set
    another_var = os.getenv("ANOTHER_VAR")

    # Sample code using environment variables
    print(f"Environment Variable MYENVVAR: {my_env_var}")

    if another_var:
        print(f"Another environment variable: {another_var}")
    else:
        print("ANOTHER_VAR is not set in .env")

    # Placeholder for additional logic
    print("Starting main application...")


if __name__ == "__main__":
    main()
