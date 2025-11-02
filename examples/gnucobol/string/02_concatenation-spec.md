# 02_CONCATENATION Specification

## Overview
A COBOL program demonstrating string concatenation using the STRING verb with delimiter control, pointer tracking, and overflow handling.

## Program Identification
- **Program ID**: 02_CONCATENATION
- **Original File**: 02_concatenation.cbl
- **Author**: Not specified
- **Date Written**: Not specified
- **Last Modified**: Available via file system

## Business Logic
### Purpose
This program demonstrates:
- STRING verb for concatenation
- DELIMITED BY SIZE (use entire field)
- DELIMITED BY space (stop at first space)
- POINTER clause for tracking position
- ON OVERFLOW condition handling
- String length calculation

### Process Flow
1. Prompt for name and accept into var-str1
2. Prompt for surname and accept into var-str2
3. Concatenate strings using STRING:
   - Append var-str2 (entire field)
   - Append var-str1 (up to first space)
   - Track position with var-count
4. Display concatenated result
5. Display final length/position
6. Handle overflow if strings too long

## Data Structures

### Input Files
None (user input from console)

### Output Files
None (output to standard output/console)

### Working Storage Variables

| Variable Name | Type | Size | Purpose |
|--------------|------|------|---------|
| var-str1 | Alphanumeric | 10 chars | First input (name) |
| var-str2 | Alphanumeric | 10 chars | Second input (surname) |
| var-str-out | Alphanumeric | 20 chars | Output concatenated string |
| var-count | Numeric | 2 digits | Pointer tracking current position |

## File Operations
None

## Calculations and Transformations

### STRING Operation
```cobol
STRING var-str2 DELIMITED BY SIZE
       var-str1 DELIMITED BY space
       INTO var-str-out
       WITH POINTER var-count
       ON OVERFLOW DISPLAY 'String overflow!'
END-STRING
```

**Components:**
1. **var-str2 DELIMITED BY SIZE**: Uses entire var-str2 (all 10 characters)
2. **var-str1 DELIMITED BY space**: Uses var-str1 up to first space
3. **INTO var-str-out**: Target for concatenation
4. **WITH POINTER var-count**: Tracks current write position
5. **ON OVERFLOW**: Triggered if output exceeds 20 characters

**Delimiter Behavior:**
- DELIMITED BY SIZE: Uses entire field regardless of content
- DELIMITED BY space: Stops at first space character
- No delimiter between concatenated strings

## Error Handling
- ON OVERFLOW clause catches buffer overflow
- Displays "String overflow!" if result too long
- No other validation

## Dependencies
### Called Programs
None

### External Resources
- Standard input (keyboard)
- Standard output (console/terminal)

## Migration Considerations

### Recommended Target Architecture
- String utility library
- Name formatting component
- Text processing application

### Python Implementation Notes
```python
def demonstrate_concatenation():
    """Demonstrate string concatenation with delimiters."""
    
    print("Type your name:")
    name = input()[:10]  # Limit to 10 characters
    
    print("Type your surname:")
    surname = input()[:10]  # Limit to 10 characters
    
    # Concatenate: surname (full) + name (up to space)
    name_part = name.split()[0] if ' ' in name else name
    str_out = surname + name_part
    
    # Check overflow
    if len(str_out) > 20:
        print("String overflow!")
        str_out = str_out[:20]
    
    print(f"str: {str_out}")
    print(f"length: {len(str_out) + 1}")  # +1 for COBOL pointer (1-based)

if __name__ == "__main__":
    demonstrate_concatenation()
```

**Python Equivalents:**
- `string1 + string2` for concatenation
- `string.split()[0]` for delimiter-based extraction
- `string[:n]` for length limiting
- `len(string)` for length

### Node.js Implementation Notes
```javascript
const readline = require('readline/promises');

async function demonstrateConcatenation() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    try {
        let name = (await rl.question("Type your name:\n")).substring(0, 10);
        let surname = (await rl.question("Type your surname:\n")).substring(0, 10);
        
        // Concatenate: surname (full) + name (up to space)
        const namePart = name.split(' ')[0];
        let strOut = surname + namePart;
        
        // Check overflow
        if (strOut.length > 20) {
            console.log("String overflow!");
            strOut = strOut.substring(0, 20);
        }
        
        console.log(`str: ${strOut}`);
        console.log(`length: ${strOut.length + 1}`);  // +1 for COBOL pointer
        
    } finally {
        rl.close();
    }
}

demonstrateConcatenation();
```

### Data Migration
No persistent data.

## Testing Scenarios
### Unit Tests
- **Test 1**: name="John", surname="Doe"
  - Expected: "DoeJohn", length=8
- **Test 2**: name="John Smith", surname="Doe"
  - Expected: "DoeJohn", length=8 (space delimiter stops at first space)
- **Test 3**: name="VeryLongName", surname="VeryLongSurname"
  - Expected: Overflow message, truncated to 20 chars
- **Test 4**: name="A", surname="B"
  - Expected: "BA", length=3

### Integration Tests
- **Test 1**: Complete flow with normal inputs
- **Test 2**: Overflow condition testing
- **Test 3**: Delimiter behavior verification

## Performance Considerations
- STRING operation is efficient
- Single-pass concatenation
- Minimal memory overhead
- Execution time: negligible

## Security Considerations
- **Buffer Overflow**: Protected by ON OVERFLOW clause
- **Input Validation**: Limited to 10 characters per field
- **Output Limit**: 20-character maximum enforced
- No injection risks with string concatenation
- No authentication/authorization required
- No encryption needed
