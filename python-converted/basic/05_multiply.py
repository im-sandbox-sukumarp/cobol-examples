#!/usr/bin/env python3
"""
05_MULTIPLY - Python Implementation

A program that demonstrates basic arithmetic multiplication.
Prompts the user to enter two numbers, multiplies them together,
and displays the result.

Original COBOL Program: 05_multiply.cbl
Converted from specification: 05_multiply-spec.md
"""


def multiply_numbers() -> None:
    """
    Multiply two numbers provided by user input.
    
    Process:
    1. Prompt for first number (multiplicand)
    2. Prompt for second number (multiplicand)
    3. Calculate product
    4. Display result
    
    Raises:
        ValueError: If non-numeric input is provided
        OverflowError: If result is too large
    """
    try:
        # Prompt and accept first number
        print("Enter number 1: ", end="")
        num1 = int(input())
        
        # Prompt and accept second number
        print("Enter number 2: ", end="")
        num2 = int(input())
        
        # Perform multiplication
        result = num1 * num2
        
        # Display result
        print(f"Result : {result}")
        
    except ValueError:
        print("Error: Please enter valid numbers")
    except OverflowError:
        print("Error: Result too large")
    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    """Main entry point for the multiplication program."""
    multiply_numbers()


if __name__ == "__main__":
    main()
