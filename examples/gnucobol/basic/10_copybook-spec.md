# 10_COPYBOOK Specification

## Overview
A COBOL program demonstrating the COPY statement, which includes external copybook files during compilation. This is similar to #include in C or import in modern languages, promoting code reuse.

## Program Identification
- **Program ID**: 10_COPYBOOK
- **Original File**: 10_copybook.cbl
- **Author**: Not specified
- **Date Written**: Not specified
- **Last Modified**: Available via file system

## Business Logic
### Purpose
This program demonstrates:
- COPY statement for including external code
- Code reusability through copybooks
- Shared data structures across programs
- Separation of concerns (data definitions in copybooks)

### Process Flow
1. Program starts at PROCEDURE DIVISION
2. Displays table headers (struct-headers)
3. Displays separator line (var-line with dashes)
4. Assigns values to variables:
   - Sets var-lp to 01
   - Sets var-number to 3721
5. Displays formatted row (struct-row) from copybook
6. Terminates with STOP RUN

## Data Structures

### Input Files
None (user input from console)

### Output Files
None (output to standard output/console)

### Working Storage Variables

**Defined in Program:**
| Variable Name | Type | Size | Purpose |
|--------------|------|------|---------|
| struct-headers | Group | 38 chars | Table header structure |
| var-line | Alphanumeric | 80 chars | Separator line filled with dashes |

**Defined in Copybook (SampleDataRow.cpy):**
| Variable Name | Type | Size | Purpose |
|--------------|------|------|---------|
| struct-row | Group | ~40 chars | Data row structure from copybook |
| var-lp | Numeric | 2 digits | Line/position number |
| var-number | Numeric (formatted) | 10 chars | Integer with zero suppression |
| var-decimal | Numeric (formatted) | 10 chars | Signed decimal |
| var-currency | Numeric (formatted) | 10 chars | Currency format |

### Copybook Details
- **Copybook Name**: SampleDataRow
- **Location**: CopyBooks/SampleDataRow.cpy
- **Purpose**: Defines struct-row and its sub-fields
- **Usage**: `COPY SampleDataRow.`
- **Benefit**: Reusable data structure definition across multiple programs

## File Operations
None

## Calculations and Transformations
- Data initialization with VALUE clauses
- MOVE statements for data assignment
- Automatic formatting via PICTURE clauses

## Error Handling
No explicit error handling. Potential issues:
- Copybook file not found (compile-time error)
- DISPLAY operations assumed to succeed

## Dependencies
### Called Programs
None

### External Resources
- **Copybook**: CopyBooks/SampleDataRow.cpy (compile-time dependency)
- Standard output (console/terminal)

### Compiler Configuration
- Compiler must know copybook search path
- Typically configured via COBCPY environment variable or compiler flag
- Example: `export COBCPY="./CopyBooks"`

## Migration Considerations

### Recommended Target Architecture
- Modular application with shared data models
- Separate files for data structures/models
- Configuration management for shared components

### Python Implementation Notes
```python
# SampleDataRow.py - Shared data model (copybook equivalent)
from dataclasses import dataclass

@dataclass
class DataRow:
    """Shared data structure equivalent to copybook."""
    lp: int = 0
    number: int = 0
    decimal: float = -317.21
    currency: float = 317.21
    
    def __str__(self):
        return (f"{self.lp:02d}|"
                f"{self.number:>10}|"
                f"{self.decimal:>+10.2f}|"
                f"${self.currency:>9.2f}")

# main program
from SampleDataRow import DataRow

def main():
    """Main program using shared data structure."""
    # Headers
    print("lp|    number|   decimal|  currency")
    print("-" * 80)
    
    # Create and populate data row
    row = DataRow()
    row.lp = 1
    row.number = 3721
    
    print(row)

if __name__ == "__main__":
    main()
```

**Python Equivalent Concepts:**
- Separate module files for shared structures
- `from module import Class` equivalent to COPY
- Dataclasses for data structures
- Type hints for field definitions

### Node.js Implementation Notes
```javascript
// SampleDataRow.js - Shared data model (copybook equivalent)
class DataRow {
    constructor() {
        this.lp = 0;
        this.number = 0;
        this.decimal = -317.21;
        this.currency = 317.21;
    }
    
    toString() {
        return `${this.lp.toString().padStart(2, '0')}|` +
               `${this.number.toString().padStart(10)}|` +
               `${(this.decimal >= 0 ? '+' : '')}${this.decimal.toFixed(2).padStart(10)}|` +
               `$${this.currency.toFixed(2).padStart(9)}`;
    }
}

module.exports = DataRow;

// main program
const DataRow = require('./SampleDataRow');

function main() {
    // Headers
    console.log("lp|    number|   decimal|  currency");
    console.log("-".repeat(80));
    
    // Create and populate data row
    const row = new DataRow();
    row.lp = 1;
    row.number = 3721;
    
    console.log(row.toString());
}

main();
```

**JavaScript Equivalent Concepts:**
- CommonJS modules (`require`) or ES6 modules (`import`)
- Separate files for shared classes
- Export/import mechanism
- Class definitions for data structures

### Data Migration
No persistent data. Demonstrates code organization and reusability pattern.

**Migration Strategy for Copybooks:**
1. Identify all copybooks in the COBOL system
2. Create equivalent model/class files in target language
3. Document data structures and their relationships
4. Ensure consistent field names and types
5. Implement validation logic from copybooks
6. Use dependency injection for flexibility

## Testing Scenarios
### Unit Tests
- **Test 1: Copybook Loading**: Verify copybook compiles correctly
- **Test 2: Data Structure**: Verify struct-row fields accessible
- **Test 3: Output Format**: Verify formatted output matches expected
  - Expected: Headers, separator, data row with values 01, 3721, etc.

### Integration Tests
- **Test 1**: Complete program execution
  - Verify copybook data structure works correctly
- **Test 2**: Multiple programs using same copybook
  - Verify consistency across programs

## Performance Considerations
- COPY is compile-time operation (no runtime cost)
- No performance overhead from using copybooks
- Same as if code were written inline
- Execution time: negligible

## Security Considerations
- **Copybook Security**: Ensure copybook files are read-only in production
- **Source Control**: Version control copybooks with programs
- **Access Control**: Restrict who can modify shared copybooks
- **Impact Analysis**: Changes to copybooks affect all using programs
- No authentication/authorization required for demo
- No encryption needed
- **Production Recommendations**:
  - Implement copybook versioning
  - Use change management for copybook modifications
  - Test all dependent programs when copybooks change
  - Document copybook dependencies
