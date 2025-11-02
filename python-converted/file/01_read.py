#!/usr/bin/env python3
"""
01_READ_FILE - Python Implementation

A program demonstrating sequential file reading.
Reads person records from a text file and displays them.

Original COBOL Program: 01_read.cbl
Converted from specification: 01_read-spec.md
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class Person:
    """
    Person record structure.
    
    Attributes:
        person_id: Person ID number (3 digits)
        name: Person first name (16 chars)
        surname: Person last name (25 chars)
    """
    person_id: int
    name: str
    surname: str
    
    @classmethod
    def from_line(cls, line: str) -> Optional['Person']:
        """
        Parse a person record from a fixed-width text line.
        
        COBOL format:
        - ID: positions 0-2 (3 digits)
        - Name: positions 3-18 (16 chars)
        - Surname: positions 19-43 (25 chars)
        
        Args:
            line: Fixed-width text line
            
        Returns:
            Person object or None if parsing fails
        """
        try:
            if len(line) < 44:
                # Pad line if too short
                line = line.ljust(44)
            
            person_id = int(line[0:3].strip())
            name = line[3:19].strip()
            surname = line[19:44].strip()
            
            return cls(person_id, name, surname)
        except (ValueError, IndexError):
            return None
    
    def __str__(self) -> str:
        """Format person record for display."""
        return f"{self.person_id:03d} {self.name:16s} {self.surname:25s}"


def read_person_file(filename: str) -> None:
    """
    Read and display person records from file.
    
    Process:
    1. Open file for reading
    2. Loop through records
    3. Display each record
    4. Close file
    
    Args:
        filename: Path to person records file
        
    Raises:
        FileNotFoundError: If file doesn't exist
        IOError: If file cannot be read
    """
    try:
        file_path = Path(filename)
        
        # Check if file exists
        if not file_path.exists():
            print(f"Error: File '{filename}' not found")
            return
        
        # Open file for reading
        with open(file_path, 'r', encoding='utf-8') as f:
            # Read and display each record
            for line in f:
                # Remove trailing newline
                line = line.rstrip('\n\r')
                
                # Parse person record
                person = Person.from_line(line)
                
                if person:
                    print(person)
                else:
                    print(f"Warning: Could not parse line: {line}")
        
        print("File reading completed successfully")
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except IOError as e:
        print(f"Error reading file: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def main() -> None:
    """Main entry point for the file reading program."""
    # Default file location (matching COBOL)
    default_file = "../SampleData/persons.txt"
    
    # For testing, allow command line argument
    import sys
    filename = sys.argv[1] if len(sys.argv) > 1 else default_file
    
    read_person_file(filename)


if __name__ == "__main__":
    main()
