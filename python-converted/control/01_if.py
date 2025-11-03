#!/usr/bin/env python3
"""
01_IF - Python Implementation

A program demonstrating conditional logic using if statements,
comparison operators, and various data type checks.

Original COBOL Program: 01_if.cbl
Converted from specification: 01_if-spec.md
"""


def is_numeric(s: str) -> bool:
    """Check if string represents a numeric value."""
    try:
        float(s)
        return True
    except ValueError:
        return False


def is_alphabetic(s: str) -> bool:
    """Check if string contains only alphabetic characters."""
    return s.isalpha()


def demonstrate_conditionals() -> None:
    """
    Demonstrate various conditional tests.
    
    Tests include:
    - Comparison operators (>, =, <)
    - Sign tests (positive, negative)
    - Type tests (numeric, alphabetic)
    - Range tests (level 88 condition names)
    - Compound conditions (AND, NOT)
    """
    try:
        # Accept inputs
        print("ENTER number 1: ", end="")
        num1 = int(input())
        
        print("ENTER number 2: ", end="")
        num2 = int(input())
        
        print("ENTER some data: ", end="")
        data = input()
        
        # Comparison tests
        if num1 > num2:
            print(f"num1 ({num1}) is greater than num2 ({num2})")
        elif num1 == num2:
            print(f"num1 ({num1}) is equal to num2 ({num2})")
        else:
            print(f"num1 ({num1}) is less than num2 ({num2})")
        
        # Sign tests
        if num1 > 0:
            print(f"num1 ({num1}) is positive")
        elif num1 < 0:
            print(f"num1 ({num1}) is negative")
        else:
            print(f"num1 ({num1}) is zero")
        
        # Type tests on data
        if is_numeric(data):
            print(f"data '{data}' is numeric")
        elif is_alphabetic(data):
            print(f"data '{data}' is alphabetic")
        else:
            print(f"data '{data}' is mixed or special characters")
        
        # Level 88 condition tests (range checks)
        # var-pass1: num1 in range 100-9999
        pass1 = 100 <= num1 <= 9999
        pass2 = 100 <= num2 <= 9999
        
        if pass1:
            print(f"num1 ({num1}) is in valid range [100-9999]")
        else:
            print(f"num1 ({num1}) is outside valid range [100-9999]")
        
        if pass2:
            print(f"num2 ({num2}) is in valid range [100-9999]")
        else:
            print(f"num2 ({num2}) is outside valid range [100-9999]")
        
        # Compound condition test (AND)
        if pass1 and pass2:
            print("Both numbers are in valid range")
        else:
            print("At least one number is outside valid range")
        
    except ValueError:
        print("Error: Please enter valid numbers for num1 and num2")
    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    """Main entry point for the conditional logic program."""
    demonstrate_conditionals()


if __name__ == "__main__":
    main()
