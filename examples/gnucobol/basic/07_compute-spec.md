# 07_COMPUTE Specification

## Overview
A COBOL program that demonstrates the COMPUTE verb for complex mathematical calculations. It evaluates a quadratic function y = ax² + bx + c with user-provided coefficients and x value.

## Program Identification
- **Program ID**: 07_COMPUTE
- **Original File**: 07_compute.cbl
- **Author**: Not specified
- **Date Written**: Not specified
- **Last Modified**: Available via file system

## Business Logic
### Purpose
This program demonstrates:
- COMPUTE verb for complex arithmetic expressions
- Quadratic equation evaluation
- Exponentiation operator (**)
- Order of operations in mathematical expressions
- Formatted decimal output

### Process Flow
1. Program starts at PROCEDURE DIVISION
2. Displays instruction: "Calc result of quadratic formula y = ax^2 + bx + c"
3. Prompts and accepts coefficient 'a'
4. Prompts and accepts coefficient 'b'
5. Prompts and accepts coefficient 'c'
6. Prompts and accepts value 'x'
7. Computes result: y = a×x² + b×x + c
8. Displays result with label "y = "
9. Terminates with STOP RUN

## Data Structures

### Input Files
None (user input from console)

### Output Files
None (output to standard output/console)

### Working Storage Variables

| Variable Name | Type | Size | Purpose |
|--------------|------|------|---------|
| var-a | Numeric | 11 digits | Coefficient 'a' in quadratic equation |
| var-b | Numeric | 11 digits | Coefficient 'b' in quadratic equation |
| var-c | Numeric | 11 digits | Coefficient 'c' in quadratic equation |
| var-x | Numeric | 11 digits | Variable 'x' value to evaluate |
| var-result | Numeric (formatted) | 18 chars | Result with 2 decimal places and zero suppression |

**PICTURE Clause Details:**
- `PIC 9(10)9`: 11-digit numeric field
- `PIC z(15)9.99`: 16 digits with zero suppression + 1 always shown + 2 decimals

## File Operations
None

## Calculations and Transformations
### Quadratic Function Evaluation
- **Formula**: y = a×x² + b×x + c
- **COBOL Syntax**: `COMPUTE var-result = var-a * var-x**2 + var-b*var-x + var-c`
- **Operations**:
  - Exponentiation: x**2 (x squared)
  - Multiplication: a×x², b×x
  - Addition: sum of three terms
- **Order of Operations**:
  1. Exponentiation (**) - highest precedence
  2. Multiplication (*) - medium precedence
  3. Addition (+) - lowest precedence
- **Precision**: Result stored with 2 decimal places

### Mathematical Properties
- Quadratic function (parabola when plotted)
- Result range depends on input values
- Can produce very large or very small results

## Error Handling
No explicit error handling. Potential issues:
- Non-numeric input causes runtime error
- Overflow if result exceeds field capacity
- No validation of input values
- Large x values can cause exponential growth

## Dependencies
### Called Programs
None

### External Resources
- Standard input (keyboard)
- Standard output (console/terminal)

## Migration Considerations

### Recommended Target Architecture
- Console application or mathematical utility
- Consider web-based calculator interface
- Input validation essential for production use

### Python Implementation Notes
```python
def quadratic_calculator():
    """Calculate quadratic function y = ax² + bx + c."""
    try:
        print("Calc result of quadratic formula y = ax^2 + bx + c")
        print()
        
        print("Enter a:")
        a = float(input())
        
        print("Enter b:")
        b = float(input())
        
        print("Enter c:")
        c = float(input())
        
        print("Enter x:")
        x = float(input())
        
        # Calculate y = ax² + bx + c
        result = a * x**2 + b * x + c
        
        print(f"y = {result:.2f}")
        
    except ValueError:
        print("Error: Please enter valid numbers")
    except OverflowError:
        print("Error: Result too large")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    quadratic_calculator()
```

Suggested libraries:
- `numpy` for advanced mathematical operations (optional)
- Built-in arithmetic sufficient for basic implementation

### Node.js Implementation Notes
```javascript
const readline = require('readline/promises');

async function quadraticCalculator() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    try {
        console.log("Calc result of quadratic formula y = ax^2 + bx + c");
        console.log();
        
        const a = parseFloat(await rl.question("Enter a:\n"));
        const b = parseFloat(await rl.question("Enter b:\n"));
        const c = parseFloat(await rl.question("Enter c:\n"));
        const x = parseFloat(await rl.question("Enter x:\n"));
        
        // Calculate y = ax² + bx + c
        const result = a * Math.pow(x, 2) + b * x + c;
        
        console.log(`y = ${result.toFixed(2)}`);
        
    } catch (error) {
        console.error("Error:", error);
    } finally {
        rl.close();
    }
}

quadraticCalculator();
```

Alternative using Math.js library for more features:
```javascript
const math = require('mathjs');
const result = math.evaluate('a * x^2 + b * x + c', {a, b, c, x});
```

### Data Migration
No persistent data. All data is transient.

## Testing Scenarios
### Unit Tests
- **Test 1: Basic Quadratic**: a=1, b=0, c=0, x=5
  - Expected Result: 25.00 (y = 1×5² = 25)
- **Test 2: Full Equation**: a=2, b=3, c=1, x=4
  - Expected Result: 45.00 (y = 2×16 + 3×4 + 1 = 32 + 12 + 1)
- **Test 3: Negative Coefficients**: a=-1, b=2, c=3, x=2
  - Expected Result: 3.00 (y = -4 + 4 + 3)
- **Test 4: Zero Coefficients**: a=0, b=0, c=5, x=10
  - Expected Result: 5.00 (constant function)
- **Test 5: Decimal Values**: a=1.5, b=2.5, c=1, x=2
  - Expected Result: 12.00

### Integration Tests
- **Test 1: Complete Flow**
  - Input: a=1, b=-3, c=2, x=1
  - Expected Output: "y = 0.00"
- **Test 2: Large Values**
  - Input: a=1, b=0, c=0, x=100
  - Expected: Verify handling of large results

## Performance Considerations
- Minimal performance requirements
- Single computation with 3 arithmetic operations
- Execution time: negligible
- No optimization needed
- Exponentiation is O(1) for fixed power of 2

## Security Considerations
- **Input Validation**: Validate numeric input
- **Overflow Protection**: Check for result exceeding capacity
- **Range Checking**: Consider limits on input values
- No authentication/authorization required
- No encryption needed
- No audit trail required
- **Production Recommendations**:
  - Add input sanitization
  - Implement range validation
  - Add error messages for overflow
  - Consider scientific notation for large results
