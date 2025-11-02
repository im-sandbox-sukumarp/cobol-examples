#!/usr/bin/env python3
"""
06_DIVIDE - Python Implementation

A program that demonstrates division operations with both integer and decimal results.
Shows how to handle division with remainder calculation for both integer and decimal divisions.

Original COBOL Program: 06_divide.cbl
Converted from specification: 06_divide-spec.md
"""


def divide_numbers() -> None:
    """
    Demonstrate integer and decimal division with remainder.
    
    Process:
    1. Prompt for dividend (num1)
    2. Prompt for divisor (num2)
    3. Perform integer division with remainder
    4. Perform decimal division with remainder
    5. Display both results
    
    Raises:
        ValueError: If non-numeric input is provided
        ZeroDivisionError: If divisor is zero
    """
    try:
        # Prompt and accept dividend
        print("Enter number 1: ", end="")
        num1 = int(input())
        
        # Prompt and accept divisor
        print("Enter number 2: ", end="")
        num2 = int(input())
        
        # Check for division by zero
        if num2 == 0:
            print("Error: Cannot divide by zero")
            return
        
        # Integer division
        result_int = num1 // num2
        remainder_int = num1 % num2
        
        print("Divide as integers:")
        print(f"Result : {result_int}")
        print(f"Reminder : {remainder_int}")
        print()
        
        # Decimal division
        result_dec = num1 / num2
        # Remainder after considering decimal result
        remainder_dec = num1 - (int(result_dec) * num2)
        
        print("Divide as decimals:")
        print(f"Result : {result_dec:.2f}")
        print(f"Reminder : {remainder_dec:.2f}")
        print()
        
    except ValueError:
        print("Error: Please enter valid numbers")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    """Main entry point for the division program."""
    divide_numbers()


if __name__ == "__main__":
    main()
