# 03_MORE_LOOPS Specification

## Overview
A COBOL program demonstrating advanced loop structures including counted loops, UNTIL loops, TEST BEFORE loops, and VARYING loops (similar to for-loops).

## Program Identification
- **Program ID**: 03_MORE_LOOPS
- **Original File**: 03_more_loops.cbl
- **Author**: Not specified
- **Date Written**: Not specified
- **Last Modified**: Available via file system

## Business Logic
### Purpose
This program demonstrates:
- PERFORM N TIMES (counted loop)
- PERFORM UNTIL (do-while style, test after)
- PERFORM WITH TEST BEFORE UNTIL (while-do style)
- PERFORM VARYING (for-loop style)

### Process Flow
1. Loop #1: PERFORM 3 TIMES (counted loop)
2. Loop #2: PERFORM UNTIL (do-while, counter 0-2)
3. Loop #3: PERFORM WITH TEST BEFORE UNTIL (while-do, counter 0-2)
4. Loop #4: PERFORM VARYING (for-loop, counter 1-3)
5. Display spaces between each loop demonstration
6. Terminate with STOP RUN

## Data Structures

### Input Files
None

### Output Files
None (output to standard output/console)

### Working Storage Variables

| Variable Name | Type | Size | Purpose |
|--------------|------|------|---------|
| counter | Numeric | 2 digits | Loop counter for UNTIL and VARYING loops |

## File Operations
None

## Calculations and Transformations
None - Control flow demonstration.

### Loop Structures Explained

1. **Counted Loop (N TIMES)**:
   - Syntax: `PERFORM 3 TIMES`
   - Executes exactly 3 times
   - No counter variable needed

2. **UNTIL Loop (Do-While Style)**:
   - Syntax: `PERFORM UNTIL counter = 3`
   - Tests condition AFTER execution (always executes at least once)
   - Counter incremented inside loop

3. **TEST BEFORE UNTIL Loop (While-Do Style)**:
   - Syntax: `PERFORM WITH TEST BEFORE UNTIL counter = 3`
   - Tests condition BEFORE execution
   - May not execute if condition initially true

4. **VARYING Loop (For-Loop Style)**:
   - Syntax: `PERFORM VARYING counter FROM 1 BY 1 UNTIL counter=4`
   - Initializes counter
   - Increments by specified amount
   - Tests condition before each iteration

## Error Handling
No explicit error handling.

## Dependencies
### Called Programs
None

### External Resources
- Standard output (console/terminal)

## Migration Considerations

### Recommended Target Architecture
- Console application
- Educational tool for loop patterns
- Algorithm demonstration

### Python Implementation Notes
```python
def demonstrate_more_loops():
    """Demonstrate various advanced loop structures."""
    
    # Loop n times (counted loop)
    for _ in range(3):
        print("Hello world #1")
    
    print()
    
    # Do-while style (always executes at least once)
    # Python doesn't have do-while, but can simulate
    counter = 0
    while True:
        print("Hello World #2")
        counter += 1
        if counter == 3:
            break
    
    print()
    
    # While-do style (test before)
    counter = 0
    while counter != 3:
        print("Hello World #3")
        counter += 1
    
    print()
    
    # For-loop style
    counter = 0
    for counter in range(1, 4):  # 1 to 3 inclusive
        print("Hello World #4")
    
    print()

if __name__ == "__main__":
    demonstrate_more_loops()
```

### Node.js Implementation Notes
```javascript
function demonstrateMoreLoops() {
    // Loop n times (counted loop)
    for (let i = 0; i < 3; i++) {
        console.log("Hello world #1");
    }
    
    console.log();
    
    // Do-while style (test after)
    let counter = 0;
    do {
        console.log("Hello World #2");
        counter++;
    } while (counter !== 3);
    
    console.log();
    
    // While-do style (test before)
    counter = 0;
    while (counter !== 3) {
        console.log("Hello World #3");
        counter++;
    }
    
    console.log();
    
    // For-loop style
    for (counter = 1; counter !== 4; counter++) {
        console.log("Hello World #4");
    }
    
    console.log();
}

demonstrateMoreLoops();
```

### Data Migration
No persistent data.

## Testing Scenarios
### Unit Tests
- **Test 1**: Verify Loop #1 executes exactly 3 times
- **Test 2**: Verify Loop #2 executes 3 times (counter 0→1→2)
- **Test 3**: Verify Loop #3 executes 3 times with TEST BEFORE
- **Test 4**: Verify Loop #4 executes 3 times (counter 1→2→3)

### Integration Tests
- **Test 1**: Complete execution
  - Expected: 12 "Hello world" messages total (3 per loop)
  - Verify blank lines between sections

## Performance Considerations
- Minimal overhead
- Simple loop structures
- No intensive operations
- Execution time: negligible

## Security Considerations
- No security concerns for demonstration program
- No authentication/authorization required
- No encryption needed
