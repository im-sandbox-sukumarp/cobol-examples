# 01_MAIN Specification

## Overview
A COBOL program demonstrating subroutine calls with different parameter passing modes: BY REFERENCE (default) and BY CONTENT. It calls 01_call_subroutine with parameters and shows how they are affected.

## Program Identification
- **Program ID**: 01_MAIN
- **Original File**: 01_call_main.cbl
- **Author**: Not specified
- **Date Written**: Not specified
- **Last Modified**: Available via file system
- **Note**: This is the MAIN FILE to execute

## Business Logic
### Purpose
This program demonstrates:
- CALL statement for invoking subroutines
- BY REFERENCE parameter passing (default) - allows modification
- BY CONTENT parameter passing - passes copy, no modification
- Parameter passing differences
- Inter-program communication

### Process Flow
1. Initialize variables (WS-NUMBER=1234, WS-STRING='Some string')
2. Display "Before CALL BY"
3. Call subroutine BY REFERENCE (default):
   - Pass WS-NUMBER and WS-STRING
   - Subroutine CAN modify these values
4. Display "After CALL BY REFERENCE" - shows modifications
5. Reset WS-NUMBER to 1234
6. Call subroutine BY CONTENT:
   - Pass copies of WS-NUMBER and WS-STRING
   - Subroutine CANNOT modify original values
7. Display "After CALL BY CONTENT" - shows no modifications
8. Terminate with STOP RUN

## Data Structures

### Input Files
None

### Output Files
None (output to standard output/console)

### Working Storage Variables

| Variable Name | Type | Size | Purpose |
|--------------|------|------|---------|
| WS-NUMBER | Numeric | 4 digits | Test number (initially 1234) |
| WS-STRING | Alphabetic | 15 chars | Test string (initially 'Some string') |

## File Operations
None

## Calculations and Transformations
None - Demonstrates parameter passing, not calculations.

### Parameter Passing Modes

**BY REFERENCE (Default):**
- Passes address/pointer to original variable
- Subroutine can modify the original value
- Changes persist after CALL returns
- More memory efficient

**BY CONTENT:**
- Passes copy of the value
- Subroutine cannot modify original
- Changes do not persist after CALL returns
- Uses more memory (copy overhead)

## Error Handling
No explicit error handling.

## Dependencies
### Called Programs
- **01_call_subroutine**: External subroutine program
- Must be compiled and available for dynamic loading

### External Resources
- Standard output (console/terminal)
- Compiled subroutine module

## Migration Considerations

### Recommended Target Architecture
- Modular application with function/method calls
- Library or module system
- Object-oriented classes and methods

### Python Implementation Notes
```python
def main_program():
    """Main program demonstrating function calls."""
    ws_number = 1234
    ws_string = 'Some string'
    
    print("Before CALL BY:")
    print(f"Number: {ws_number}")
    print(f"String: {ws_string}")
    print()
    
    # BY REFERENCE equivalent - pass mutable object
    data = {'number': ws_number, 'string': ws_string}
    call_subroutine_by_ref(data)
    
    print()
    print("After CALL BY REFERENCE:")
    print(f"Number: {data['number']}")  # Modified to 3721
    print(f"String: {data['string']}")  # Modified
    
    # Reset and call by content
    data['number'] = 1234
    print()
    
    # BY CONTENT equivalent - pass immutable values
    result = call_subroutine_by_content(data['number'], data['string'])
    
    print()
    print("After CALL BY CONTENT:")
    print(f"Number: {data['number']}")  # Still 1234 (unchanged)
    print(f"String: {data['string']}")  # Unchanged

def call_subroutine_by_ref(data):
    """Subroutine with BY REFERENCE - modifies original."""
    print("Hello subroutine!")
    print(f"String data: {data['string']}")
    data['number'] = 3721  # Modifies original

def call_subroutine_by_content(number, string):
    """Subroutine with BY CONTENT - returns new values."""
    print("Hello subroutine!")
    print(f"String data: {string}")
    return 3721  # Returns new value, doesn't modify original

if __name__ == "__main__":
    main_program()
```

**Python Equivalents:**
- Pass mutable objects (dict, list) for BY REFERENCE
- Pass immutable values (int, str) for BY CONTENT
- Use return values for modified data

### Node.js Implementation Notes
```javascript
function mainProgram() {
    let wsNumber = 1234;
    let wsString = 'Some string';
    
    console.log("Before CALL BY:");
    console.log(`Number: ${wsNumber}`);
    console.log(`String: ${wsString}`);
    console.log();
    
    // BY REFERENCE equivalent - pass object
    const data = {number: wsNumber, string: wsString};
    callSubroutineByRef(data);
    
    console.log();
    console.log("After CALL BY REFERENCE:");
    console.log(`Number: ${data.number}`);  // Modified
    console.log(`String: ${data.string}`);
    
    // Reset
    data.number = 1234;
    console.log();
    
    // BY CONTENT equivalent - pass primitives
    callSubroutineByContent(data.number, data.string);
    
    console.log();
    console.log("After CALL BY CONTENT:");
    console.log(`Number: ${data.number}`);  // Unchanged
    console.log(`String: ${data.string}`);
}

function callSubroutineByRef(data) {
    console.log("Hello subroutine!");
    console.log(`String data: ${data.string}`);
    data.number = 3721;  // Modifies original
}

function callSubroutineByContent(number, string) {
    console.log("Hello subroutine!");
    console.log(`String data: ${string}`);
    return 3721;  // Can't modify primitives
}

mainProgram();
```

### Data Migration
No persistent data. Demonstrates program structure and calling conventions.

## Testing Scenarios
### Unit Tests
- **Test 1**: BY REFERENCE call
  - Expected: WS-NUMBER changed from 1234 to 3721
- **Test 2**: BY CONTENT call
  - Expected: WS-NUMBER remains 1234 after call
- **Test 3**: Subroutine execution
  - Expected: "Hello subroutine!" displayed twice

### Integration Tests
- **Test 1**: Complete call sequence
  - Verify both call modes work correctly
- **Test 2**: Parameter integrity
  - Verify BY CONTENT protection works

## Performance Considerations
- BY REFERENCE: More efficient (no copy)
- BY CONTENT: Overhead of copying data
- For large data structures, BY REFERENCE preferred
- Modern languages optimize parameter passing

## Security Considerations
- **Parameter Protection**: BY CONTENT prevents accidental modification
- **Data Integrity**: Use BY CONTENT for sensitive data
- **Best Practices**: Use BY CONTENT for read-only parameters
- No authentication/authorization needed for demo
- **Production Recommendations**:
  - Document parameter passing modes
  - Use BY CONTENT for immutable parameters
  - Validate parameters in called programs
  - Consider thread safety for concurrent calls
