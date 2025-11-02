# 01_IF Specification

## Overview
A COBOL program demonstrating conditional logic using IF statements, comparison operators, condition names (level 88), and class tests (NUMERIC, ALPHABETIC).

## Program Identification
- **Program ID**: 01_IF
- **Original File**: 01_if.cbl
- **Author**: Not specified
- **Date Written**: Not specified
- **Last Modified**: Available via file system

## Business Logic
### Purpose
This program demonstrates:
- IF-THEN-ELSE conditional statements
- Comparison operators (>, =, <)
- Class tests (IS POSITIVE, IS NEGATIVE, IS NUMERIC, IS ALPHABETIC)
- Level 88 condition names (boolean flags)
- Logical operators (AND, NOT)
- Nested IF statements

### Process Flow
1. Accept three inputs: var-num1, var-num2, var-data
2. Compare num1 and num2 (greater, equal, less than)
3. Test if num1 is positive or negative
4. Test if data is numeric or alphabetic
5. Test level 88 conditions (var-pass1, var-pass2) for values >= 100
6. Test compound conditions with AND operator
7. Display appropriate messages for each condition

## Data Structures

### Input Files
None (user input from console)

### Output Files
None (output to standard output/console)

### Working Storage Variables

| Variable Name | Type | Size | Purpose |
|--------------|------|------|---------|
| var-num1 | Signed Numeric | 9 digits | First number for comparison |
| var-pass1 | Level 88 | - | Condition: var-num1 in range 100-9999 |
| var-num2 | Signed Numeric | 9 digits | Second number for comparison |
| var-pass2 | Level 88 | - | Condition: var-num2 in range 100-9999 |
| var-data | Alphanumeric | 9 chars | String data for class testing |

**Level 88 Conditions:**
- `88 var-pass1 VALUES ARE 100 THRU 9999`: True when var-num1 is 100-9999
- `88 var-pass2 VALUES ARE 100 THRU 9999`: True when var-num2 is 100-9999

## File Operations
None

## Calculations and Transformations
None - This is a conditional logic demonstration program.

### Conditional Logic
1. **Comparison Tests**: >, =, <
2. **Sign Tests**: IS POSITIVE, IS NEGATIVE
3. **Class Tests**: IS NUMERIC, IS ALPHABETIC
4. **Condition Names**: Level 88 variables act as boolean flags
5. **Logical Operations**: AND, NOT

## Error Handling
No explicit error handling. The program accepts any input.

## Dependencies
### Called Programs
None

### External Resources
- Standard input (keyboard)
- Standard output (console/terminal)

## Migration Considerations

### Recommended Target Architecture
- Console application
- Input validation utility
- Educational tool for conditional logic

### Python Implementation Notes
```python
def demonstrate_conditionals():
    """Demonstrate various conditional tests."""
    try:
        print("ENTER number 1: ", end="")
        num1 = int(input())
        
        print("ENTER number 2: ", end="")
        num2 = int(input())
        
        print("ENTER some data: ", end="")
        data = input()
        
        # Comparison tests
        if num1 > num2:
            print("Number1 is greater than Number2")
        elif num1 == num2:
            print("Number1 equals Number2")
        else:
            print("Number1 is less than Number2")
        
        # Sign tests
        if num1 > 0:
            print("Number1 is positive")
        
        if num1 < 0:
            print("Number1 is negative")
        
        # Class tests
        if data.isdigit():
            print("Numeric data")
        
        if data.isalpha():
            print("Alphabetic data")
        
        # Range tests (level 88 equivalent)
        pass1 = 100 <= num1 <= 9999
        pass2 = 100 <= num2 <= 9999
        
        if pass1:
            print("Number1 is greater than 100")
        
        if not pass1:
            print("Number1 is less than 100")
        
        if pass2:
            print("Number2 is greater than 100")
        
        if not pass2:
            print("Number2 is less than 100")
        
        # Compound conditions
        if pass1 and pass2:
            print("Both of numbers are greater than 100")
    
    except ValueError:
        print("Error: Invalid number input")

if __name__ == "__main__":
    demonstrate_conditionals()
```

### Node.js Implementation Notes
```javascript
const readline = require('readline/promises');

async function demonstrateConditionals() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    try {
        const num1 = parseInt(await rl.question("ENTER number 1: \n"));
        const num2 = parseInt(await rl.question("ENTER number 2: \n"));
        const data = await rl.question("ENTER some data: \n");
        
        // Comparison tests
        if (num1 > num2) {
            console.log("Number1 is greater than Number2");
        } else if (num1 === num2) {
            console.log("Number1 equals Number2");
        } else {
            console.log("Number1 is less than Number2");
        }
        
        // Sign tests
        if (num1 > 0) {
            console.log("Number1 is positive");
        }
        
        if (num1 < 0) {
            console.log("Number1 is negative");
        }
        
        // Class tests
        if (/^\d+$/.test(data)) {
            console.log("Numeric data");
        }
        
        if (/^[a-zA-Z]+$/.test(data)) {
            console.log("Alphabetic data");
        }
        
        // Range tests (level 88 equivalent)
        const pass1 = num1 >= 100 && num1 <= 9999;
        const pass2 = num2 >= 100 && num2 <= 9999;
        
        if (pass1) {
            console.log("Number1 is greater than 100");
        }
        
        if (!pass1) {
            console.log("Number1 is less than 100");
        }
        
        if (pass2) {
            console.log("Number2 is greater than 100");
        }
        
        if (!pass2) {
            console.log("Number2 is less than 100");
        }
        
        // Compound conditions
        if (pass1 && pass2) {
            console.log("Both of numbers are greater than 100");
        }
        
    } finally {
        rl.close();
    }
}

demonstrateConditionals();
```

### Data Migration
No persistent data. Demonstrates conditional logic patterns.

## Testing Scenarios
### Unit Tests
- **Test 1**: num1=150, num2=50, data="abc"
  - Expected: "Number1 is greater", "positive", "alphabetic", both pass conditions
- **Test 2**: num1=50, num2=150, data="123"
  - Expected: "Number1 is less", "positive", "numeric", neither pass
- **Test 3**: num1=-10, num2=-10, data="a1b"
  - Expected: "equals", "negative", neither pass
- **Test 4**: num1=500, num2=600
  - Expected: Both pass conditions met

### Integration Tests
- **Test 1**: Complete flow with various inputs
- **Test 2**: Edge cases (0, boundary values 100, 9999)

## Performance Considerations
- Minimal overhead
- Sequential conditional checks
- No loops or intensive operations
- Execution time: negligible

## Security Considerations
- Input validation recommended
- No authentication/authorization required
- No encryption needed
- No audit trail required
