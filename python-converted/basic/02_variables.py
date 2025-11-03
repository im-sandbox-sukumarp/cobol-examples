#!/usr/bin/env python3
"""
02_VARIABLES - Python Implementation

A program that demonstrates variable declaration and data formatting.
Displays a formatted table showing different number formats including integers,
decimals, and currency values.

Original COBOL Program: 02_variables.cbl
Converted from specification: 02_variables-spec.md
"""


class VariablesDemo:
    """
    Demonstrates data formatting with different numeric types.
    
    Attributes:
        lp: Line/position number (2 digits)
        number: Integer value with formatting
        decimal: Signed decimal with 2 decimal places
        currency: Currency format with dollar sign
    """
    
    def __init__(self):
        """Initialize variables with default values."""
        self.lp: int = 0
        self.number: int = 0
        self.decimal: float = -317.21
        self.currency: float = 317.21
    
    def display_table(self) -> None:
        """
        Display a formatted table with headers and data row.
        
        Shows various numeric formats:
        - Integer with zero suppression
        - Signed decimal
        - Currency with dollar sign
        """
        # Display headers
        print("lp|    number|   decimal|  currency")
        
        # Display separator line (80 dashes)
        print("-" * 80)
        
        # Update values
        self.lp = 1
        self.number = 3721
        
        # Display formatted data row
        # Format: lp (2 digits), number (10 chars right-aligned), 
        #         decimal (10 chars with sign), currency ($ + 9 chars)
        print(f"{self.lp:02d}|{self.number:>10}|{self.decimal:>+10.2f}|${self.currency:>9.2f}")


def main() -> None:
    """Main entry point for the variables demonstration program."""
    demo = VariablesDemo()
    demo.display_table()


if __name__ == "__main__":
    main()
