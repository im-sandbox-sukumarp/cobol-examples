#!/usr/bin/env python3
"""
02_CONCATENATION - Python Implementation

A program demonstrating string concatenation with delimiter control
and overflow handling.

Original COBOL Program: 02_concatenation.cbl
Converted from specification: 02_concatenation-spec.md
"""


def demonstrate_concatenation() -> None:
    """
    Demonstrate string concatenation with delimiter control.
    
    Process:
    1. Accept name (first input)
    2. Accept surname (second input)
    3. Concatenate: surname (entire) + name (up to first space)
    4. Display result and length
    5. Handle overflow if combined string too long
    
    COBOL behavior:
    - var-str2 DELIMITED BY SIZE: uses entire field
    - var-str1 DELIMITED BY space: stops at first space
    """
    MAX_OUTPUT_LEN = 20
    
    try:
        # Prompt and accept first string (name)
        print("Enter name: ", end="")
        name = input()[:10]  # Limit to 10 chars like COBOL
        
        # Prompt and accept second string (surname)
        print("Enter surname: ", end="")
        surname = input()[:10]  # Limit to 10 chars like COBOL
        
        # Concatenate:
        # - surname: entire field (all 10 chars in COBOL, we use actual input)
        # - name: up to first space
        name_part = name.split()[0] if name.strip() else name
        result = surname + name_part
        
        # Check for overflow (max 20 chars)
        if len(result) > MAX_OUTPUT_LEN:
            print("String overflow!")
            result = result[:MAX_OUTPUT_LEN]
        
        # Display result
        print(f"Result: {result}")
        
        # Display length/position
        position = len(result) + 1  # POINTER is 1-based in COBOL
        print(f"Position: {position}")
        
    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    """Main entry point for the concatenation program."""
    demonstrate_concatenation()


if __name__ == "__main__":
    main()
