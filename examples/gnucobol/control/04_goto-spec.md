# 04_GOTO Specification

## Overview
A COBOL program demonstrating GO TO statements for unconditional jumps and GO TO DEPENDING ON for switch-like behavior (labeled "GO TO MONSTER").

## Program Identification
- **Program ID**: 04_GOTO
- **Original File**: 04_goto.cbl
- **Author**: Not specified
- **Date Written**: Not specified
- **Last Modified**: Available via file system

## Business Logic
### Purpose
This program demonstrates:
- Simple GO TO for unconditional jump
- GO TO DEPENDING ON for switch/case-like logic
- Paragraph labels as jump targets
- Control flow redirection

### Process Flow
1. Execute GO TO PARA-NEXT (skip PARA-TO-SKIP)
2. Display message in PARA-NEXT
3. Prompt user to enter number 1, 2, or 3
4. Execute GO TO DEPENDING ON var-switch:
   - If var-switch = 1, go to PARA-1
   - If var-switch = 2, go to PARA-2
   - If var-switch = 3, go to PARA-3
   - If var-switch > 3 or < 1, fall through
5. Execute selected paragraph and all following paragraphs (fall-through)
6. Terminate with STOP RUN

## Data Structures

### Input Files
None (user input from console)

### Output Files
None (output to standard output/console)

### Working Storage Variables

| Variable Name | Type | Size | Purpose |
|--------------|------|------|---------|
| var-switch | Numeric | 2 digits | Switch value to select paragraph (1, 2, or 3) |

## File Operations
None

## Calculations and Transformations
None - Control flow demonstration.

### GO TO Behavior

1. **Simple GO TO**:
   ```cobol
   GO TO PARA-NEXT
   ```
   - Unconditionally jumps to labeled paragraph
   - Skips intervening code

2. **GO TO DEPENDING ON** (Switch/Case):
   ```cobol
   GO TO PARA-1 PARA-2 PARA-3 DEPENDING ON var-switch
   ```
   - If var-switch = 1: jump to PARA-1
   - If var-switch = 2: jump to PARA-2
   - If var-switch = 3: jump to PARA-3
   - If var-switch < 1 or > 3: no jump (fall through)

3. **Fall-Through Behavior**:
   - After jumping to a paragraph, execution continues through subsequent paragraphs
   - No implicit break like in switch statements
   - Continues until STOP RUN

## Error Handling
No explicit error handling. Issues:
- Non-numeric input causes runtime error
- Out-of-range values (< 1 or > 3) fall through to all paragraphs

## Dependencies
### Called Programs
None

### External Resources
- Standard input (keyboard)
- Standard output (console/terminal)

## Migration Considerations

### Recommended Target Architecture
- Console application
- Menu-driven interface
- State machine implementation

**Important**: GO TO is generally discouraged in modern programming. Refactor to use structured control flow.

### Python Implementation Notes
```python
def demonstrate_goto():
    """Demonstrate GO TO patterns using structured code."""
    
    # Simple GO TO equivalent - just skip code with control flow
    # Skip para_to_skip
    para_next()
    
    # GO TO DEPENDING ON equivalent - use match/case (Python 3.10+)
    # or if-elif chain
    print("Enter number 1,2 or 3:")
    var_switch = int(input())
    
    # Python 3.10+ match statement
    match var_switch:
        case 1:
            para_1()
            # Note: Need explicit fall-through in Python
            para_2()
            para_3()
        case 2:
            para_2()
            para_3()
        case 3:
            para_3()
        case _:
            # Out of range - execute all
            para_1()
            para_2()
            para_3()

def para_to_skip():
    print("You never see that.")

def para_next():
    print("Hello in PARA-NEXT!")

def para_1():
    print("PARA-1")

def para_2():
    print("PARA-2")

def para_3():
    print("PARA-3")

if __name__ == "__main__":
    demonstrate_goto()
```

**Refactored Alternative (Structured Programming)**:
```python
def demonstrate_switch():
    """Better structured alternative without GO TO."""
    print("Hello in PARA-NEXT!")
    
    print("Enter number 1,2 or 3:")
    choice = int(input())
    
    # Dictionary dispatch pattern (more Pythonic)
    actions = {
        1: lambda: execute_from(1),
        2: lambda: execute_from(2),
        3: lambda: execute_from(3)
    }
    
    actions.get(choice, lambda: execute_from(1))()

def execute_from(start):
    """Execute paragraphs from start position."""
    paragraphs = [para_1, para_2, para_3]
    for para in paragraphs[start-1:]:
        para()
```

### Node.js Implementation Notes
```javascript
const readline = require('readline/promises');

async function demonstrateGoto() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    try {
        // Simple GO TO - just skip
        paraNext();
        
        // GO TO DEPENDING ON
        const varSwitch = parseInt(await rl.question("Enter number 1,2 or 3:\n"));
        
        switch (varSwitch) {
            case 1:
                para1();
                // Fall-through
            case 2:
                para2();
                // Fall-through
            case 3:
                para3();
                break;
            default:
                para1();
                para2();
                para3();
        }
    } finally {
        rl.close();
    }
}

function paraToSkip() {
    console.log("You never see that.");
}

function paraNext() {
    console.log("Hello in PARA-NEXT!");
}

function para1() {
    console.log("PARA-1");
}

function para2() {
    console.log("PARA-2");
}

function para3() {
    console.log("PARA-3");
}

demonstrateGoto();
```

### Data Migration
No persistent data.

## Testing Scenarios
### Unit Tests
- **Test 1**: var-switch = 1
  - Expected: PARA-1, PARA-2, PARA-3
- **Test 2**: var-switch = 2
  - Expected: PARA-2, PARA-3
- **Test 3**: var-switch = 3
  - Expected: PARA-3
- **Test 4**: var-switch = 0 or 4
  - Expected: All paragraphs or none (depending on implementation)

### Integration Tests
- **Test 1**: Verify PARA-TO-SKIP never executes
- **Test 2**: Verify fall-through behavior for each switch value

## Performance Considerations
- Minimal overhead
- GO TO is very fast (direct jump)
- No performance concerns

## Security Considerations
- **Input Validation**: Validate var-switch range
- No authentication/authorization required
- No encryption needed
- **Production Recommendations**:
  - Refactor GO TO to structured control flow
  - Add input range validation
  - Use switch/case or if-elif instead
