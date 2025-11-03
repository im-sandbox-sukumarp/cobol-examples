#!/usr/bin/env python3
"""
07_COMPUTE - Python Implementation

A program that demonstrates complex mathematical calculations.
Evaluates a quadratic function y = ax² + bx + c with user-provided
coefficients and x value.

Original COBOL Program: 07_compute.cbl
Converted from specification: 07_compute-spec.md
"""


def compute_quadratic() -> None:
    """
    Calculate the result of quadratic formula y = ax² + bx + c.
    
    Process:
    1. Display instruction
    2. Prompt for coefficient 'a'
    3. Prompt for coefficient 'b'
    4. Prompt for coefficient 'c'
    5. Prompt for value 'x'
    6. Compute: y = a×x² + b×x + c
    7. Display result with 2 decimal places
    
    Raises:
        ValueError: If non-numeric input is provided
        OverflowError: If result is too large
    """
    try:
        # Display instruction
        print("Calc result of quadratic formula y = ax^2 + bx + c")
        
        # Prompt and accept coefficients
        print("a = ", end="")
        a = float(input())
        
        print("b = ", end="")
        b = float(input())
        
        print("c = ", end="")
        c = float(input())
        
        print("x = ", end="")
        x = float(input())
        
        # Compute quadratic function: y = ax² + bx + c
        # Order of operations: exponentiation, then multiplication, then addition
        result = a * (x ** 2) + b * x + c
        
        # Display result with 2 decimal places
        print(f"y = {result:.2f}")
        
    except ValueError:
        print("Error: Please enter valid numbers")
    except OverflowError:
        print("Error: Result too large")
    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    """Main entry point for the compute program."""
    compute_quadratic()


if __name__ == "__main__":
    main()
