# 01_INSPECT Specification

## Overview
A COBOL program demonstrating the INSPECT verb for string analysis and manipulation, including character counting and character replacement.

## Program Identification
- **Program ID**: 01_INSPECT
- **Original File**: 01_insepct.cbl (note: filename has typo "insepct")
- **Author**: Not specified
- **Date Written**: Not specified
- **Last Modified**: Available via file system

## Business Logic
### Purpose
This program demonstrates:
- INSPECT TALLYING for counting characters
- INSPECT TALLYING FOR ALL for counting specific characters
- INSPECT REPLACING ALL for character substitution
- String length calculation
- Space counting in strings

### Process Flow
1. Display prompt: "Enter some string:"
2. Accept user input into var-str (max 10 characters)
3. Count total characters using INSPECT TALLYING
4. Display string length
5. Count spaces using INSPECT TALLYING FOR ALL space
6. Display space count
7. Replace all 'a' characters with 'z' using INSPECT REPLACING
8. Display modified string
9. Terminate with STOP RUN

## Data Structures

### Input Files
None (user input from console)

### Output Files
None (output to standard output/console)

### Working Storage Variables

| Variable Name | Type | Size | Purpose |
|--------------|------|------|---------|
| var-str | Alphanumeric | 10 chars | Input string for manipulation |
| var-length | Numeric | 5 digits | Counter for tallying operations |

## File Operations
None

## Calculations and Transformations

### INSPECT Operations

1. **Count All Characters**:
   ```cobol
   INSPECT var-str TALLYING var-length FOR CHARACTERS
   ```
   - Counts total number of characters in string
   - Includes spaces and all printable characters

2. **Count Specific Characters**:
   ```cobol
   INSPECT var-str TALLYING var-length FOR ALL space
   ```
   - Counts occurrences of specific character (space)
   - Can be used with any character or pattern

3. **Replace Characters**:
   ```cobol
   INSPECT var-str REPLACING ALL 'a' BY 'z'
   ```
   - Replaces all occurrences of 'a' with 'z'
   - Modifies string in-place
   - Case-sensitive replacement

## Error Handling
No explicit error handling. Considerations:
- Input longer than 10 characters will be truncated
- No validation of input

## Dependencies
### Called Programs
None

### External Resources
- Standard input (keyboard)
- Standard output (console/terminal)

## Migration Considerations

### Recommended Target Architecture
- String utility library
- Text processing application
- Input validation component

### Python Implementation Notes
```python
def demonstrate_inspect():
    """Demonstrate INSPECT operations using Python string methods."""
    
    print("Enter some string:")
    var_str = input()[:10]  # Limit to 10 characters
    
    # Tallying - count all characters
    var_length = len(var_str)
    print(f"Length: {var_length}")
    
    # Tallying - count spaces
    var_length = var_str.count(' ')
    print(f"Spaces: {var_length}")
    
    # Replacing - replace all 'a' with 'z'
    var_str = var_str.replace('a', 'z')
    print(f"Str: {var_str}")

if __name__ == "__main__":
    demonstrate_inspect()
```

**Python Equivalent Methods:**
- `len(string)` for character counting
- `string.count(char)` for counting specific characters
- `string.replace(old, new)` for character replacement
- `string.count(' ')` for counting spaces

### Node.js Implementation Notes
```javascript
const readline = require('readline/promises');

async function demonstrateInspect() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    try {
        let varStr = await rl.question("Enter some string:\n");
        varStr = varStr.substring(0, 10);  // Limit to 10 characters
        
        // Tallying - count all characters
        let varLength = varStr.length;
        console.log(`Length: ${varLength}`);
        
        // Tallying - count spaces
        varLength = (varStr.match(/ /g) || []).length;
        console.log(`Spaces: ${varLength}`);
        
        // Replacing - replace all 'a' with 'z'
        varStr = varStr.replace(/a/g, 'z');
        console.log(`Str: ${varStr}`);
        
    } finally {
        rl.close();
    }
}

demonstrateInspect();
```

**JavaScript Equivalent Methods:**
- `string.length` for character counting
- `string.match(/char/g).length` for counting specific characters
- `string.replace(/a/g, 'z')` for global character replacement
- Regular expressions for pattern matching

### Data Migration
No persistent data. Demonstrates string manipulation patterns.

## Testing Scenarios
### Unit Tests
- **Test 1**: Input "hello world"
  - Length: 10 (truncated)
  - Spaces: 1
  - After replace: "hello world" (no 'a')
- **Test 2**: Input "banana"
  - Length: 6
  - Spaces: 0
  - After replace: "bznznz"
- **Test 3**: Input "a b c d"
  - Length: 7
  - Spaces: 3
  - After replace: "z b c d"
- **Test 4**: Input "HELLO" (no 'a')
  - Length: 5
  - Spaces: 0
  - After replace: "HELLO" (unchanged)

### Integration Tests
- **Test 1**: Complete flow with various inputs
- **Test 2**: Boundary testing with 10-character strings
- **Test 3**: Empty string handling

## Performance Considerations
- INSPECT is efficient for character operations
- In-place modification for REPLACING
- Single-pass operations
- Execution time: negligible for short strings
- Modern alternatives may use regex (slightly slower but more flexible)

## Security Considerations
- **Input Validation**: 10-character limit prevents buffer overflow
- **No Injection Risk**: Character replacement is safe
- No authentication/authorization required
- No encryption needed
- No audit trail required
- **Production Recommendations**:
  - Add input length validation
  - Consider sanitizing special characters
  - Document character encoding (ASCII vs UTF-8)
