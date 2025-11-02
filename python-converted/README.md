# COBOL to Python Converted Programs

This directory contains Python implementations of COBOL programs, automatically converted from COBOL specification markdown files.

## Structure

- `basic/` - Basic COBOL programs (hello world, variables, arithmetic operations)
- `control/` - Control flow programs (if statements, loops, goto)
- `string/` - String manipulation programs (inspect, concatenation, split)
- `file/` - File operation programs (read, write, rewrite, delete)
- `database/` - Database operation programs (select, insert, update, delete, DDL)
- `sorting/` - Sorting programs
- `subroutines/` - Subroutine call examples
- `mainframe/` - Mainframe-specific programs
- `tests/` - Test suites for all converted programs

## Requirements

- Python 3.8+
- pytest (for running tests)

## Installation

```bash
pip install -r requirements.txt
```

## Running Programs

Each Python file can be executed directly:

```bash
python3 basic/01_hello_world.py
python3 basic/03_add.py
```

## Running Tests

Run all tests:
```bash
pytest
```

Run specific test file:
```bash
pytest tests/test_01_hello_world.py
```

Run with coverage:
```bash
pytest --cov=. --cov-report=html
```

## Conversion Notes

All programs were converted from COBOL specification markdown files that document:
- Program overview and business logic
- Data structures and variable definitions
- Process flows and algorithms
- Error handling requirements
- Testing scenarios

The Python implementations preserve the business logic and behavior of the original COBOL programs while using idiomatic Python patterns.
