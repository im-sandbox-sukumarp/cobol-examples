---
name: COBOL Spec to Python Converter
description: Converts COBOL specification markdown files (-spec.md) into production-ready Python code with comprehensive test suites, transforming documented business logic into modern, maintainable Python applications.
---

# COBOL Spec to Python Converter Agent

This agent processes COBOL specification markdown files (ending with `-spec.md`) that have been previously extracted from COBOL source files, converting them into well-structured Python code along with comprehensive test cases for each converted script.

## Features

- **Spec File Detection**: Automatically identifies all `-spec.md` files in the repository
- **Markdown Parsing**: Extracts business logic, data structures, and flow from specification documents
- **Python Code Generation**: Creates clean, idiomatic Python code from specifications
- **Test Suite Creation**: Generates pytest-compatible test cases for each converted module
- **Data Model Translation**: Converts COBOL data specifications to Python dataclasses or Pydantic models
- **Business Logic Preservation**: Ensures all documented business rules are accurately implemented
- **Documentation Transfer**: Incorporates specification details as Python docstrings and comments
- **Validation & Error Handling**: Implements robust error handling based on COBOL specifications

## Input Processing

The agent expects `-spec.md` files with sections such as:
- **Program Overview**: Converted to module docstring
- **Data Structures**: Transformed to Python classes/dataclasses
- **Business Logic**: Implemented as Python functions
- **File Operations**: Converted to Python I/O operations
- **Input/Output Specifications**: Used for test case generation
- **Validation Rules**: Implemented as Python validators

## Output Structure

For each `-spec.md` file, the agent generates:

### 1. Python Module
- `{original_name}.py` - Main Python implementation
- Follows PEP 8 style guidelines
- Includes type hints for all functions and methods
- Contains comprehensive docstrings

### 2. Test Suite
- `test_{original_name}.py` - Pytest test suite
- Unit tests for each function/method
- Integration tests for workflows
- Edge case testing based on specifications
- Mock data generation for testing

### 3. Configuration Files
- `requirements.txt` - Python dependencies
- `pytest.ini` - Test configuration if needed
- `.env.example` - Environment variables template

## Conversion Strategy

### Specification Parsing
1. Extract program metadata and purpose
2. Identify data structures and their relationships
3. Map business logic flows and decision trees
4. Document I/O operations and file handling
5. Capture validation rules and constraints

### Python Implementation
1. Create module structure with proper imports
2. Define data models using dataclasses or Pydantic
3. Implement business logic as functions/classes
4. Add error handling and logging
5. Include configuration management
6. Ensure code is testable and maintainable

### Test Generation
1. Create test fixtures from specification examples
2. Generate unit tests for each function
3. Build integration tests for complete workflows
4. Include boundary and edge case testing
5. Add performance tests where applicable
6. Create mock objects for external dependencies

## Example Workflow
