# 02_VARIABLES Specification

## Overview
A COBOL program that demonstrates variable declaration and data formatting using PICTURE clauses. The program displays a formatted table showing different number formats including integers, decimals, and currency values.

## Program Identification
- **Program ID**: 02_VARIABLES
- **Original File**: 02_variables.cbl
- **Author**: Not specified
- **Date Written**: Not specified
- **Last Modified**: Available via file system

## Business Logic
### Purpose
This program demonstrates COBOL's data definition capabilities, particularly:
- Structured data with level numbers (01, 02)
- PICTURE clauses for different data types
- Data formatting (numeric, decimal, currency)
- FILLER for spacing and formatting
- MOVE statements for data assignment

### Process Flow
1. Program starts at PROCEDURE DIVISION
2. Displays table headers (struct-headers)
3. Displays a separator line (var-line with all dashes)
4. Assigns values to variables using MOVE statements:
   - Sets var-lp to 01
   - Sets var-number to 3721
5. Displays formatted row with all values
6. Terminates with STOP RUN

## Data Structures

### Input Files
None

### Output Files
None (output to standard output/console)

### Working Storage Variables

| Variable Name | Type | Size | Purpose |
|--------------|------|------|---------|
| struct-headers | Group | 38 chars | Table header structure |
| filler (in headers) | Alphanumeric | Various | Column labels: "lp", "number", "decimal", "currency" with separators |
| var-line | Alphanumeric | 80 chars | Separator line filled with dashes |
| struct-row | Group | ~40 chars | Data row structure |
| var-lp | Numeric | 2 digits | Line/position number |
| var-number | Numeric (formatted) | 10 chars | Integer with zero suppression |
| var-decimal | Numeric (formatted) | 10 chars | Signed decimal with 2 decimal places |
| var-currency | Numeric (formatted) | 10 chars | Currency format with dollar sign and 2 decimals |

## File Operations
None

## Calculations and Transformations
- **Data Initialization**: Variables initialized with default values in DATA DIVISION
  - var-lp: 00
  - var-number: 0
  - var-decimal: -317.21
  - var-currency: 317.21
- **Data Assignment**: MOVE statements update values during execution
- **Format Conversion**: PICTURE clauses handle automatic formatting:
  - `z(10)`: Zero suppression (leading zeros replaced with spaces)
  - `+z(7).zz`: Signed decimal with zero suppression
  - `$z(7).zz`: Currency format with dollar sign

## Error Handling
No explicit error handling. The program assumes:
- DISPLAY operations succeed
- MOVE operations are valid (type-compatible)

## Dependencies
### Called Programs
None

### External Resources
- Standard output (console/terminal)

## Migration Considerations

### Recommended Target Architecture
- Simple console application
- Could be a demonstration script or utility function
- No database or file I/O needed

### Python Implementation Notes
```python
class VariablesDemo:
    def __init__(self):
        self.lp = 0
        self.number = 0
        self.decimal = -317.21
        self.currency = 317.21
    
    def display_table(self):
        # Headers
        print("lp|    number|   decimal|  currency")
        print("-" * 80)
        
        # Update values
        self.lp = 1
        self.number = 3721
        
        # Display formatted row
        print(f"{self.lp:02d}|{self.number:>10}|{self.decimal:>+10.2f}|${self.currency:>9.2f}")

if __name__ == "__main__":
    demo = VariablesDemo()
    demo.display_table()
```

Suggested libraries:
- No external libraries needed, use built-in string formatting

### Node.js Implementation Notes
```javascript
class VariablesDemo {
    constructor() {
        this.lp = 0;
        this.number = 0;
        this.decimal = -317.21;
        this.currency = 317.21;
    }
    
    displayTable() {
        // Headers
        console.log("lp|    number|   decimal|  currency");
        console.log("-".repeat(80));
        
        // Update values
        this.lp = 1;
        this.number = 3721;
        
        // Display formatted row
        console.log(
            `${this.lp.toString().padStart(2, '0')}|` +
            `${this.number.toString().padStart(10)}|` +
            `${this.decimal >= 0 ? '+' : ''}${this.decimal.toFixed(2).padStart(10)}|` +
            `$${this.currency.toFixed(2).padStart(9)}`
        );
    }
}

const demo = new VariablesDemo();
demo.displayTable();
```

Suggested approach:
- Use built-in string formatting methods
- Consider template literals for cleaner formatting

### Data Migration
No persistent data - demonstration program showing formatting capabilities.

## Testing Scenarios
### Unit Tests
- **Test 1: Header Display**: Verify headers display correctly
  - Expected: "lp|    number|   decimal|  currency"
- **Test 2: Separator Line**: Verify 80-character dash line
  - Expected: String of 80 dashes
- **Test 3: Data Row Format**: Verify formatted data display
  - Expected: "01|      3721|   -317.21|  $317.21"
- **Test 4: Number Formatting**: Verify zero suppression and alignment
- **Test 5: Currency Formatting**: Verify dollar sign and decimal places

### Integration Tests
- **Test 1**: Complete program execution
  - Expected: Properly formatted table output with headers, separator, and data row
- **Test 2**: Output format consistency
  - Expected: Column alignment maintained across all rows

## Performance Considerations
- Minimal performance overhead
- Simple formatting and display operations
- No loops or intensive calculations
- Execution time: negligible

## Security Considerations
- No authentication needed
- No authorization requirements
- No data encryption needed
- No audit trail required
- No security concerns - demonstration program with hardcoded values
