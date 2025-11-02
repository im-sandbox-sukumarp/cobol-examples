#!/usr/bin/env python3
"""
03_ADDING - Python Implementation

A program that demonstrates basic arithmetic addition.
Prompts the user to enter two numbers, adds them together, and displays the result.

Original COBOL Program: 03_add.cbl
Converted from specification: 03_add-spec.md
"""


def add_numbers() -> None:
    """
    Add two numbers provided by user input.
    
    Process:
    1. Prompt for first number
    2. Prompt for second number
    3. Calculate sum
    4. Display result
    
    Raises:
        ValueError: If non-numeric input is provided
    """
    try:
        # Prompt and accept first number
        print("Enter number 1: ", end="")
        num1 = int(input())
        
        # Prompt and accept second number
        print("Enter number 2: ", end="")
        num2 = int(input())
        
        # Perform addition
        result = num1 + num2
        
        # Display result
        print(f"Result : {result}")
        
    except ValueError:
        print("Error: Please enter valid numbers")
    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    """Main entry point for the addition program."""
    add_numbers()


if __name__ == "__main__":
    main()
