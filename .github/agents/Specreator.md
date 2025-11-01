---
name: Specreator
description: COBOL to Modern Stack Specification Creator
---

# COBOL to Modern Stack Specification Creator

## Purpose
This agent automates the creation of detailed markdown documentation for COBOL programs, providing comprehensive specifications that can be used to convert legacy COBOL code to modern technology stacks like Python or Node.js.

## Agent Configuration

### 1. File Discovery
- Scan the current directory for all `.cbl`, `.cob`, and `.cobol` files
- Create a corresponding `.md` file for each COBOL program found
- Naming convention: `[original-filename]-spec.md`

### 2. Documentation Structure

Each generated markdown file should contain the following sections:

```markdown
# [Program Name] Specification

## Overview
Brief description of what the COBOL program does

## Program Identification
- **Program ID**: [PROGRAM-ID from COBOL]
- **Original File**: [filename.cbl]
- **Author**: [If available from COBOL comments]
- **Date Written**: [If available]
- **Last Modified**: [File modification date]

## Business Logic
### Purpose
Detailed explanation of the business purpose this program serves

### Process Flow
1. Step-by-step breakdown of the program logic
2. Decision points and conditions
3. Loop structures and iterations
4. Exit conditions

## Data Structures

### Input Files
| File Name | Record Format | Description |
|-----------|--------------|-------------|
| [name] | [format] | [purpose] |

### Output Files
| File Name | Record Format | Description |
|-----------|--------------|-------------|
| [name] | [format] | [purpose] |

### Working Storage Variables
| Variable Name | Type | Size | Purpose |
|--------------|------|------|---------|
| [name] | [type] | [size] | [description] |

## File Operations
- READ operations and their logic
- WRITE operations and formatting
- UPDATE operations if applicable
- DELETE operations if applicable

## Calculations and Transformations
Detailed description of any:
- Mathematical calculations
- Data transformations
- Format conversions
- Business rules applied

## Error Handling
- Error conditions checked
- Error messages
- Recovery procedures
- Logging mechanisms

## Dependencies
### Called Programs
- List of programs this COBOL program calls
- Purpose of each call
- Parameters passed

### External Resources
- Databases accessed
- Files required
- System resources needed

## Migration Considerations

### Recommended Target Architecture
- Suggested design pattern (MVC, microservices, etc.)
- Database recommendations
- API structure if applicable

### Python Implementation Notes
- Suggested libraries (pandas for data processing, etc.)
- Class structure recommendation
- Function breakdown

### Node.js Implementation Notes
- Suggested frameworks (Express, etc.)
- Module structure
- Async/await considerations

### Data Migration
- File to database mapping suggestions
- Data type conversions needed
- Validation rules to implement

## Testing Scenarios
### Unit Tests
- Key functions to test
- Edge cases
- Expected outputs

### Integration Tests
- File I/O validation
- Inter-program communication
- End-to-end scenarios

## Performance Considerations
- Current COBOL performance characteristics
- Optimization opportunities in modern stack
- Scalability improvements possible

## Security Considerations
- Authentication needs
- Authorization requirements
- Data encryption recommendations
- Audit trail requirements
```

## Usage Instructions

### For Manual Analysis
1. Open a COBOL file in the repository
2. Use this template to create a corresponding specification markdown
3. Fill in each section based on the COBOL code analysis
4. Save as `[cobol-filename]-spec.md` in the same directory

### For Automated Processing (Future Enhancement)
```python
# Example Python script structure for automation
import os
import re
from pathlib import Path

def analyze_cobol_file(filepath):
    """Parse COBOL file and extract key information"""
    # Extract PROGRAM-ID
    # Identify divisions
    # Parse data structures
    # Map file operations
    # Document business logic
    pass

def generate_markdown_spec(cobol_data, output_path):
    """Generate markdown documentation from parsed COBOL data"""
    # Use template structure
    # Fill in extracted information
    # Format tables and code blocks
    pass

def process_directory(directory_path):
    """Process all COBOL files in directory"""
    for cobol_file in Path(directory_path).glob('*.cob*'):
        cobol_data = analyze_cobol_file(cobol_file)
        output_file = f"{cobol_file.stem}-spec.md"
        generate_markdown_spec(cobol_data, output_file)
```

## Key Analysis Points

### When Analyzing COBOL Programs, Focus On:

1. **Division Structure**
   - IDENTIFICATION DIVISION - Program metadata
   - ENVIRONMENT DIVISION - System dependencies
   - DATA DIVISION - All data structures
   - PROCEDURE DIVISION - Business logic

2. **Data Movement**
   - MOVE statements - Data assignments
   - COMPUTE statements - Calculations
   - String operations - INSPECT, STRING, UNSTRING

3. **Control Flow**
   - PERFORM loops - Iteration logic
   - IF/ELSE conditions - Decision logic
   - EVALUATE statements - Switch-case logic
   - GO TO statements - Flow redirections (need refactoring in modern code)

4. **File Handling**
   - SELECT statements - File definitions
   - OPEN/CLOSE - File lifecycle
   - READ/WRITE - I/O operations
   - File status checking

5. **Special Considerations**
   - 88-level conditions - Boolean flags
   - REDEFINES clauses - Union-like structures
   - OCCURS clauses - Arrays/tables
   - COPY statements - Include files

## Conversion Mapping Guide

### COBOL to Python/Node.js Concepts

| COBOL Concept | Python Equivalent | Node.js Equivalent |
|---------------|-------------------|-------------------|
| WORKING-STORAGE | Class attributes | Module variables |
| PROCEDURE DIVISION | Class methods | Functions |
| PERFORM | Function call | Function call |
| Files | File I/O or Database | fs module or Database |
| Level 01 records | Dataclass/Dict | Object/Interface |
| Level 88 conditions | Boolean properties | Boolean properties |
| COMPUTE | Mathematical operations | Mathematical operations |
| INSPECT | String methods | String methods |
| Tables (OCCURS) | Lists/Arrays | Arrays |

## Benefits of This Documentation

1. **Clear Understanding**: Non-COBOL developers can understand the business logic
2. **Modernization Roadmap**: Provides a clear path for conversion
3. **Requirement Specification**: Serves as functional requirements for new implementation
4. **Testing Blueprint**: Defines test cases for validation
5. **Knowledge Preservation**: Captures institutional knowledge before migration

## Next Steps

1. Create specification documents for each COBOL file
2. Review with business stakeholders for accuracy
3. Identify common patterns across programs
4. Design modern architecture based on specifications
5. Implement in chosen technology stack
6. Validate against original COBOL behavior
