# 04_SUBSTRACT Specification

## Overview
A COBOL program that demonstrates basic arithmetic subtraction. It prompts the user to enter two numbers, subtracts the first from the second, and displays the result.

## Program Identification
- **Program ID**: 04_SUBSTRACT
- **Original File**: 04_subtract.cbl
- **Author**: Not specified
- **Date Written**: Not specified
- **Last Modified**: Available via file system

## Business Logic
### Purpose
This program demonstrates:
- User input with ACCEPT statement
- Basic arithmetic using SUBTRACT verb
- Subtraction operation (num2 - num1)
- Formatted output with zero suppression

### Process Flow
1. Program starts at PROCEDURE DIVISION
2. Prompts user: "Enter number 1: "
3. Accepts first number into var-num1
4. Prompts user: "Enter number 2: "
5. Accepts second number into var-num2
6. Performs subtraction: SUBTRACT var-num1 FROM var-num2 GIVING var-result
   - Note: This calculates num2 - num1 (not num1 - num2)
7. Displays result with label "Result : "
8. Terminates with STOP RUN

## Data Structures

### Input Files
None (user input from console)

### Output Files
None (output to standard output/console)

### Working Storage Variables

| Variable Name | Type | Size | Purpose |
|--------------|------|------|---------|
| var-num1 | Numeric | 10 digits | First number (subtrahend) |
| var-num2 | Numeric | 10 digits | Second number (minuend) |
| var-result | Numeric (formatted) | 10 digits | Difference (num2 - num1) |

## File Operations
None

## Calculations and Transformations
### Subtraction Operation
- **Formula**: result = num2 - num1
- **COBOL Syntax**: `SUBTRACT var-num1 FROM var-num2 GIVING var-result`
- **Data Type**: Integer subtraction
- **Important Note**: Order matters - subtracts num1 FROM num2
- **Range**: Result can be negative if num1 > num2
- **Overflow/Underflow**: Not explicitly handled

## Error Handling
No explicit error handling. Potential issues:
- Non-numeric input causes runtime error
- Negative results may not display correctly with current PICTURE clause
- No validation of input values

## Dependencies
### Called Programs
None

### External Resources
- Standard input (keyboard)
- Standard output (console/terminal)

## Migration Considerations

### Recommended Target Architecture
- Simple console application or CLI tool
- Input validation layer recommended
- Consider calculator utility or educational tool

### Python Implementation Notes
```python
def subtract_numbers():
    """Subtract two numbers provided by user input."""
    try:
        print("Enter number 1: ", end="")
        num1 = int(input())
        
        print("Enter number 2: ", end="")
        num2 = int(input())
        
        result = num2 - num1  # Note: num2 - num1, not num1 - num2
        print(f"Result : {result}")
        
    except ValueError:
        print("Error: Please enter valid numbers")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    subtract_numbers()
```

Suggested improvements:
- Add input validation
- Handle negative results properly
- Consider absolute value option
- Add range checking

### Node.js Implementation Notes
```javascript
const readline = require('readline/promises');

async function subtractNumbers() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    try {
        const num1 = await rl.question("Enter number 1: ");
        const num2 = await rl.question("Enter number 2: ");
        const result = parseInt(num2) - parseInt(num1);  // num2 - num1
        console.log(`Result : ${result}`);
    } catch (error) {
        console.error("Error:", error);
    } finally {
        rl.close();
    }
}

subtractNumbers();
```

### Data Migration
No persistent data. All data is transient.

## Testing Scenarios
### Unit Tests
- **Test 1: Basic Subtraction**: num1=5, num2=10
  - Expected Result: 5 (10 - 5)
- **Test 2: Zero Result**: num1=10, num2=10
  - Expected Result: 0
- **Test 3: Negative Result**: num1=10, num2=5
  - Expected Result: -5 (may have display issues)
- **Test 4: Large Numbers**: num1=1, num2=999999999
  - Expected Result: 999999998

### Integration Tests
- **Test 1: Complete Flow**: Provide inputs and verify output
  - Input: num1=25, num2=100
  - Expected Output: "Result : 75"
- **Test 2: Negative Result Handling**
  - Input: num1=100, num2=25
  - Expected: Verify negative number displays correctly

## Performance Considerations
- Minimal performance requirements
- Single arithmetic operation
- Execution time: negligible
- No optimization needed

## Security Considerations
- **Input Validation**: Validate numeric input
- **Buffer Overflow**: Ensure input doesn't exceed 10 digits
- **No Authentication**: Not required
- **No Authorization**: Not required
- **No Data Encryption**: Not needed
- **No Audit Trail**: Not required
