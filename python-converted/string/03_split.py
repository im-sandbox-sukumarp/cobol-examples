#!/usr/bin/env python3
"""
03_SPLIT - Python Implementation

A program demonstrating string splitting using delimiter-based parsing
to extract name and surname from combined input.

Original COBOL Program: 03_split.cbl
Converted from specification: 03_split-spec.md
"""


def demonstrate_split() -> None:
    """
    Demonstrate string splitting by space delimiter.
    
    Process:
    1. Accept combined input (name and surname)
    2. Split by space delimiter
    3. Extract first token as name
    4. Extract second token as surname
    5. Display extracted fields
    
    COBOL behavior:
    - UNSTRING splits by space
    - First token → var-name
    - Second token → var-surname
    - Additional tokens → var-rest (captured but not displayed)
    """
    MAX_INPUT_LEN = 20
    
    try:
        # Display prompt
        print("Type your name and surname (use space as delimiter)")
        
        # Accept input (limit to 20 chars like COBOL)
        input_str = input()[:MAX_INPUT_LEN]
        
        # Split by space delimiter
        tokens = input_str.split()
        
        # Extract fields (pad with spaces to match COBOL field behavior)
        name = tokens[0] if len(tokens) > 0 else ""
        surname = tokens[1] if len(tokens) > 1 else ""
        rest = " ".join(tokens[2:]) if len(tokens) > 2 else ""
        
        # Display extracted fields
        print(f"Name: {name}")
        print(f"Surname: {surname}")
        
        # Note: var-rest is not displayed in original COBOL program
        # but could be used for overflow detection
        
    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    """Main entry point for the split program."""
    demonstrate_split()


if __name__ == "__main__":
    main()
