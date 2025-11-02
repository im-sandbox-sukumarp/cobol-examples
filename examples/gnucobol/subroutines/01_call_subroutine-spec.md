# 01_call_subroutine Specification

## Overview
A COBOL subroutine program demonstrating parameter reception and modification. It is called by 01_call_main.cbl and modifies the passed parameters.

## Program Identification
- **Program ID**: 01_call_subroutine
- **Original File**: 01_call_subroutine.cbl
- **Author**: Not specified
- **Date Written**: Not specified
- **Last Modified**: Available via file system
- **Note**: DO NOT RUN THIS FILE DIRECTLY - Called by 01_call_main.cbl

## Business Logic
### Purpose
This program demonstrates:
- LINKAGE SECTION for parameter definition
- PROCEDURE DIVISION USING for parameter reception
- Parameter modification
- EXIT PROGRAM for returning to caller
- Subroutine structure

### Process Flow
1. Receive parameters via LINKAGE SECTION (LS-NUMBER, LS-STRING)
2. Display "Hello subroutine!"
3. Display received string data
4. Modify LS-NUMBER to 3721
5. Exit and return control to caller with EXIT PROGRAM

## Data Structures

### Input Files
None

### Output Files
None (output to standard output/console)

### Linkage Section Variables

| Variable Name | Type | Size | Purpose |
|--------------|------|------|---------|
| LS-NUMBER | Numeric | 4 digits | Received number parameter (modified to 3721) |
| LS-STRING | Alphabetic | 15 chars | Received string parameter (displayed) |

**Note**: LINKAGE SECTION variables do not allocate storage - they reference memory passed by caller.

## File Operations
None

## Calculations and Transformations
- **Modification**: LS-NUMBER set to 3721
- **Display**: Shows received string data
- **Effect**: Depends on how called (BY REFERENCE or BY CONTENT)

## Error Handling
No error handling implemented.

## Dependencies
### Called Programs
None - This is a leaf subroutine

### Called By
- **01_call_main.cbl**: Main program that invokes this subroutine

### External Resources
- Standard output (console/terminal)

## Migration Considerations

### Recommended Target Architecture
- Function or method in modern languages
- Library function
- Module export
- Class method

### Python Implementation Notes
```python
def call_subroutine(data):
    """Subroutine that modifies passed data.
    
    Args:
        data: Dictionary with 'number' and 'string' keys
    """
    print("Hello subroutine!")
    print(f"String data: {data['string']}")
    data['number'] = 3721  # Modifies if mutable object passed

# Alternative: Return new values
def call_subroutine_functional(number, string):
    """Functional style - returns new values."""
    print("Hello subroutine!")
    print(f"String data: {string}")
    return 3721, string  # Returns tuple of values
```

**Python Equivalents:**
- Regular function with parameters
- Modify mutable objects (dict, list) for BY REFERENCE
- Return new values for BY CONTENT
- Use decorators for metadata

### Node.js Implementation Notes
```javascript
function callSubroutine(data) {
    /**
     * Subroutine that modifies passed data
     * @param {Object} data - Object with number and string properties
     */
    console.log("Hello subroutine!");
    console.log(`String data: ${data.string}`);
    data.number = 3721;  // Modifies if object passed
}

// Alternative: Functional style
function callSubroutineFunctional(number, string) {
    console.log("Hello subroutine!");
    console.log(`String data: ${string}`);
    return {number: 3721, string: string};
}

module.exports = {
    callSubroutine,
    callSubroutineFunctional
};
```

### Data Migration
No persistent data. Demonstrates subroutine calling conventions.

## Testing Scenarios
### Unit Tests
- **Test 1**: Parameter reception
  - Verify subroutine receives correct values
- **Test 2**: Parameter modification
  - Verify LS-NUMBER changed to 3721
- **Test 3**: Display output
  - Verify messages display correctly

### Integration Tests
- **Test 1**: Called by main program
  - Verify integration with caller
- **Test 2**: BY REFERENCE behavior
  - Verify modifications persist
- **Test 3**: BY CONTENT behavior
  - Verify modifications don't persist

## Performance Considerations
- Minimal overhead
- Simple parameter access and modification
- No loops or intensive operations
- EXIT PROGRAM is efficient return mechanism

## Security Considerations
- **Parameter Validation**: Should validate received parameters
- **Data Integrity**: Ensure modifications are intentional
- **Access Control**: In production, control who can call subroutine
- **Production Recommendations**:
  - Validate parameter ranges and types
  - Document expected parameter values
  - Add error return codes
  - Log subroutine invocations
  - Consider parameter sanitization

## COBOL Subroutine Concepts

### LINKAGE SECTION
- Defines parameters passed from caller
- Does not allocate storage
- References memory from calling program
- Similar to function parameters in modern languages

### PROCEDURE DIVISION USING
- Specifies which LINKAGE items are parameters
- Order matches caller's USING clause
- Establishes parameter correspondence

### EXIT PROGRAM
- Returns control to caller
- Similar to `return` in functions
- Can be called multiple times (early exit)
- Last statement before natural program end

### Compilation
- Must be compiled separately from main program
- Creates object/module file
- Linked at runtime (dynamic) or compile-time (static)
- GnuCOBOL typically uses dynamic linking
