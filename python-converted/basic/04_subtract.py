#!/usr/bin/env python3
"""
04_SUBSTRACT - Python Implementation

A program that demonstrates basic arithmetic subtraction.
Prompts the user to enter two numbers, subtracts the first from the second,
and displays the result.

Original COBOL Program: 04_subtract.cbl
Converted from specification: 04_subtract-spec.md
"""


def subtract_numbers() -> None:
    """
    Subtract two numbers provided by user input.
    
    Process:
    1. Prompt for first number (subtrahend)
    2. Prompt for second number (minuend)
    3. Calculate difference: num2 - num1
    4. Display result
    
    Note: Order matters - subtracts num1 FROM num2 (not num1 - num2)
    
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
        
        # Perform subtraction: num2 - num1
        result = num2 - num1
        
        # Display result
        print(f"Result : {result}")
        
    except ValueError:
        print("Error: Please enter valid numbers")
    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    """Main entry point for the subtraction program."""
    subtract_numbers()


if __name__ == "__main__":
    main()
