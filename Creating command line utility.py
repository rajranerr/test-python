# Creating command line utility: To create a command-line interface (CLI) utility in Python, you can either use the built-in argparse module (requires no installations) or third-party libraries like Click and Typer for advanced features.

# 1. Choose Your Tooling

#  argparse: Included in Python's standard library. Best for simple scripts with no dependencies.
#  Click: Great for complex applications with subcommands, deep nesting, and automatic help pages.
#  Typer: Built on top of Click. It uses Python type hints to generate clean CLI interfaces with minimal boilerplate. 

# 2. Example:
import argparse

def main():
    # Initialize the argument parser
    parser = argparse.ArgumentParser(
        description="A simple CLI tool to greet users."
    )

    # Add a positional argument (required by default)
    parser.add_argument(
        "name", 
        type=str, 
        help="The name of the person to greet."
    )

    # Add an optional flag/switch (-c or --count)
    parser.add_argument(
        "-c", "--count", 
        type=int, 
        default=1, 
        help="Number of times to print the greeting."
    )

    # Parse inputs from the command line
    args = parser.parse_args()

    # Execute business logic
    for _ in range(args.count):
        print(f"Hello, {args.name}!")

if __name__ == "__main__":
    main()

# 3. Make Your Utility Globally Executable: To make your utility run using a custom system command (e.g., typing mytool Alice instead of python tool.py Alice), you must package it using setuptools.

# Step A: Arrange your files

# Create the following directory layout:
# my_cli_project/
# ├── pyproject.toml
# └── src/
#     └── my_tool/
#         ├── __init__.py
#         └── main.py

# Step B: Create a pyproject.toml file: Define your project metadata and tell Python to turn your script into an executable command:

# [build-system]
# requires = ["setuptools>=61.0.0"]
# build-backend = "setuptools.build_meta"

# [project]
# name = "my_tool_pkg"
# version = "0.1.0"
# description = "A custom CLI tool"
# dependencies = [] # Add external packages like 'typer' or 'click' here if used

# [project.scripts]
# mytool = "my_tool.main:main"

# Install and Test Locally

# 1. Open your terminal in the root directory (my_cli_project/).
# 2. Run an editable installation using pip: 
# pip install -e
# 3. un your utility directly from anywhere in your terminal using the shortcut name:
# greet Bob -r 2

# Ex:
import sys

def main():
    # Defensive programming against index errors
    if len(sys.argv) < 3:
        print("Usage: python script.py <name> <age>")
        sys.exit(1)
        
    name = sys.argv[1]
    # Command line inputs always default to strings
    age = int(sys.argv[2]) 
    
    print(f"Hello {name}, you are {age} years old.")

if __name__ == "__main__":
    main()