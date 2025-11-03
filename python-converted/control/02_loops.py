#!/usr/bin/env python3
"""
02_LOOPS - Python Implementation

A program demonstrating basic loop structures and function execution order.

Original COBOL Program: 02_loops.cbl
Converted from specification: 02_loops-spec.md
"""


def a_paragraph() -> None:
    """Execute A paragraph logic."""
    print("A-PARAGRAPH")


def b_paragraph() -> None:
    """Execute B paragraph logic."""
    print("B-PARAGRAPH")


def c_paragraph() -> None:
    """Execute C paragraph logic."""
    print("C-PARAGRAPH")


def d_paragraph() -> None:
    """Execute D paragraph logic."""
    print("D-PARAGRAPH")


def e_paragraph() -> None:
    """Execute E paragraph logic."""
    print("E-PARAGRAPH")


def demonstrate_loops() -> None:
    """
    Demonstrate various loop structures.
    
    COBOL behavior:
    1. Inline PERFORM (one-step loop)
    2. PERFORM paragraph range (B through D) 2 times
    3. Display separator
    4. Fall through to remaining paragraphs (A through E)
    """
    # One-step inline perform
    print("HELLO WORLD")
    
    # Perform paragraphs B through D, 2 times
    for _ in range(2):
        b_paragraph()
        c_paragraph()
        d_paragraph()
    
    # Separator line
    print("=======")
    
    # Fall through execution (all paragraphs in sequence)
    a_paragraph()
    b_paragraph()
    c_paragraph()
    d_paragraph()
    e_paragraph()


def main() -> None:
    """Main entry point for the loops demonstration program."""
    demonstrate_loops()


if __name__ == "__main__":
    main()
