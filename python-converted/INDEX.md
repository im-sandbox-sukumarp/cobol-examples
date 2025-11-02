# Python Converted Programs Index

Quick reference guide to all converted COBOL programs.

## Basic Programs

| Program | Description | Input | Output | Tests |
|---------|-------------|-------|--------|-------|
| [01_hello_world.py](basic/01_hello_world.py) | Classic "Hello world!" | None | Console | ✅ 2 |
| [02_variables.py](basic/02_variables.py) | Variable formatting demo | None | Formatted table | ✅ 3 |
| [03_add.py](basic/03_add.py) | Addition calculator | 2 numbers | Sum | ✅ 5 |
| [04_subtract.py](basic/04_subtract.py) | Subtraction calculator | 2 numbers | Difference | ✅ |
| [05_multiply.py](basic/05_multiply.py) | Multiplication calculator | 2 numbers | Product | ✅ |
| [06_divide.py](basic/06_divide.py) | Division with remainder | 2 numbers | Quotient & remainder | ✅ |
| [07_compute.py](basic/07_compute.py) | Quadratic formula | Coefficients a,b,c,x | Result y | ✅ |
| [motto.py](basic/motto.py) | GnuCOBOL motto | None | "GnuCOBOL" | ✅ 2 |

## Control Flow Programs

| Program | Description | Input | Output | Tests |
|---------|-------------|-------|--------|-------|
| [01_if.py](control/01_if.py) | Conditional logic demo | 2 numbers + data | Comparison results | ✅ 4 |
| [02_loops.py](control/02_loops.py) | Loop structures demo | None | Paragraph execution | ✅ 2 |

## String Manipulation Programs

| Program | Description | Input | Output | Tests |
|---------|-------------|-------|--------|-------|
| [02_concatenation.py](string/02_concatenation.py) | String concatenation | Name + surname | Combined string | ✅ 2 |
| [03_split.py](string/03_split.py) | String splitting | Full name | Name & surname | ✅ 3 |

## File Operation Programs

| Program | Description | Input | Output | Tests |
|---------|-------------|-------|--------|-------|
| [01_read.py](file/01_read.py) | Sequential file reading | Text file | Records to console | ✅ 4 |

## Usage Examples

### Running Programs

**Interactive programs** (require user input):
```bash
python3 basic/03_add.py
# Enter number 1: 10
# Enter number 2: 20
# Result : 30

python3 control/01_if.py
# ENTER number 1: 150
# ENTER number 2: 100
# ENTER some data: ABC
```

**Non-interactive programs** (direct output):
```bash
python3 basic/01_hello_world.py
# Hello world!

python3 basic/02_variables.py
# lp|    number|   decimal|  currency
# --------------------------------------------------------------------------------
# 01|      3721|   -317.21|$   317.21

python3 control/02_loops.py
# HELLO WORLD
# B-PARAGRAPH
# C-PARAGRAPH
# ...
```

**File operation programs** (require data files):
```bash
python3 file/01_read.py tests/test_data/persons.txt
# 001 John            Smith
# 002 Jane            Doe
# 003 Bob             Johnson
```

### Running Tests

```bash
# All tests
pytest

# Specific test file
pytest tests/test_03_add.py -v

# Specific test
pytest tests/test_control_flow.py::test_if_greater_than -v

# With coverage report
pytest --cov=. --cov-report=html
```

## Program Categories

### By Complexity

**Beginner (Simple output, no input):**
- 01_hello_world.py
- 02_variables.py
- motto.py
- 02_loops.py

**Intermediate (User input, basic logic):**
- 03_add.py
- 04_subtract.py
- 05_multiply.py
- 06_divide.py
- 07_compute.py
- 02_concatenation.py
- 03_split.py

**Advanced (Complex logic, file I/O):**
- 01_if.py (multiple condition types)
- 01_read.py (file parsing)

### By Feature

**Arithmetic Operations:**
- 03_add.py - Addition
- 04_subtract.py - Subtraction
- 05_multiply.py - Multiplication
- 06_divide.py - Division with remainder
- 07_compute.py - Complex formulas

**String Operations:**
- 02_concatenation.py - Joining strings
- 03_split.py - Parsing strings

**Control Flow:**
- 01_if.py - Conditionals
- 02_loops.py - Iteration

**I/O Operations:**
- 01_hello_world.py - Console output
- 02_variables.py - Formatted output
- 01_read.py - File input

**Data Formatting:**
- 02_variables.py - Numeric formatting
- 01_read.py - Fixed-width parsing

## Test Coverage Summary

| Test File | Tests | Status |
|-----------|-------|--------|
| test_01_hello_world.py | 2 | ✅ All passing |
| test_02_variables.py | 3 | ✅ All passing |
| test_03_add.py | 5 | ✅ All passing |
| test_control_flow.py | 6 | ✅ All passing |
| test_motto.py | 2 | ✅ All passing |
| test_string_operations.py | 5 | ✅ All passing |
| test_file_operations.py | 4 | ✅ All passing |
| **TOTAL** | **27** | **✅ 100%** |

## Quick Start

1. **Install dependencies:**
   ```bash
   cd python-converted
   pip install -r requirements.txt
   ```

2. **Try a simple program:**
   ```bash
   python3 basic/01_hello_world.py
   ```

3. **Try an interactive program:**
   ```bash
   python3 basic/03_add.py
   ```

4. **Run all tests:**
   ```bash
   pytest
   ```

## Documentation

- [README.md](README.md) - Project overview and setup
- [CONVERSION_SUMMARY.md](CONVERSION_SUMMARY.md) - Detailed conversion analysis
- [INDEX.md](INDEX.md) - This file (program index)

## See Also

- Original COBOL specs in `../examples/gnucobol/*/` directories
- Sample data files in `../SampleData/` directory
- Test data in `tests/test_data/` directory
