# 03_SPLIT Specification

## Overview
A COBOL program demonstrating string splitting using the UNSTRING verb to parse delimited input into separate fields.

## Program Identification
- **Program ID**: 03_SPLIT
- **Original File**: 03_split.cbl
- **Author**: Not specified
- **Date Written**: Not specified
- **Last Modified**: Available via file system

## Business Logic
### Purpose
This program demonstrates:
- UNSTRING verb for string parsing
- DELIMITED BY clause for field separation
- Multiple target fields
- Splitting space-delimited input
- Extracting name and surname from combined input

### Process Flow
1. Display prompt: "Type your name and surname (use space as delimiter)"
2. Accept user input into var-long-str (max 20 characters)
3. Split input using UNSTRING with space delimiter:
   - First token → var-name
   - Second token → var-surname
   - Remaining text → var-rest (if any)
4. Display extracted name
5. Display extracted surname
6. Terminate with STOP RUN

## Data Structures

### Input Files
None (user input from console)

### Output Files
None (output to standard output/console)

### Working Storage Variables

| Variable Name | Type | Size | Purpose |
|--------------|------|------|---------|
| var-long-str | Alphanumeric | 20 chars | Combined input string |
| var-name | Alphanumeric | 20 chars | First token (name) |
| var-surname | Alphanumeric | 20 chars | Second token (surname) |
| var-rest | Alphanumeric | 20 chars | Remaining tokens (unused but catches overflow) |

## File Operations
None

## Calculations and Transformations

### UNSTRING Operation
```cobol
UNSTRING var-long-str DELIMITED BY space
    INTO var-name, var-surname, var-rest
END-UNSTRING
```

**Behavior:**
- Splits input string by space delimiter
- First space-delimited token goes to var-name
- Second token goes to var-surname
- Additional tokens (if any) go to var-rest
- Each target field is left-justified and space-padded

**Commented Code:**
- ON OVERFLOW and NOT ON OVERFLOW clauses are commented out
- Could be used to detect if input has too many or too few fields

## Error Handling
No active error handling (overflow clauses commented out). Issues:
- Input with < 2 tokens leaves fields partially filled
- Input with > 3 tokens truncates after var-rest
- No validation of input format

## Dependencies
### Called Programs
None

### External Resources
- Standard input (keyboard)
- Standard output (console/terminal)

## Migration Considerations

### Recommended Target Architecture
- String parsing utility
- Name processing component
- Input validation module
- CSV/delimited data parser

### Python Implementation Notes
```python
def demonstrate_split():
    """Demonstrate string splitting by delimiter."""
    
    print("Type your name and surname (use space as delimiter)")
    var_long_str = input()[:20]  # Limit to 20 characters
    
    # Split by space
    tokens = var_long_str.split(' ')
    
    # Extract fields (pad with empty strings if not enough tokens)
    var_name = tokens[0] if len(tokens) > 0 else ""
    var_surname = tokens[1] if len(tokens) > 1 else ""
    var_rest = ' '.join(tokens[2:]) if len(tokens) > 2 else ""
    
    # Pad to 20 characters (COBOL behavior)
    var_name = var_name.ljust(20)
    var_surname = var_surname.ljust(20)
    
    print(f"Name: {var_name}")
    print(f"Surame: {var_surname}")  # Note: typo in original "Surame"

if __name__ == "__main__":
    demonstrate_split()
```

**Python Equivalents:**
- `string.split(delimiter)` for splitting
- List indexing with bounds checking
- `string.ljust(width)` for left-justification and padding
- `' '.join(list)` for rejoining tokens

### Node.js Implementation Notes
```javascript
const readline = require('readline/promises');

async function demonstrateSplit() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    try {
        const varLongStr = (await rl.question(
            "Type your name and surname (use space as delimiter)\n"
        )).substring(0, 20);
        
        // Split by space
        const tokens = varLongStr.split(' ');
        
        // Extract fields
        let varName = tokens[0] || "";
        let varSurname = tokens[1] || "";
        const varRest = tokens.slice(2).join(' ');
        
        // Pad to 20 characters (COBOL behavior)
        varName = varName.padEnd(20, ' ');
        varSurname = varSurname.padEnd(20, ' ');
        
        console.log(`Name: ${varName}`);
        console.log(`Surame: ${varSurname}`);
        
    } finally {
        rl.close();
    }
}

demonstrateSplit();
```

**JavaScript Equivalents:**
- `string.split(delimiter)` for splitting
- Array destructuring or indexing
- `string.padEnd(length, char)` for padding
- `array.slice(start)` for remaining elements

### Data Migration
No persistent data. Demonstrates parsing pattern for delimited data.

**Common Use Cases for Migration:**
- CSV parsing
- Name field extraction
- Address parsing
- Command-line argument processing

## Testing Scenarios
### Unit Tests
- **Test 1**: Input "John Doe"
  - Expected: Name="John", Surname="Doe"
- **Test 2**: Input "John"
  - Expected: Name="John", Surname="" (empty)
- **Test 3**: Input "John Paul Doe"
  - Expected: Name="John", Surname="Paul", Rest="Doe"
- **Test 4**: Input "Mary-Jane Smith-Jones"
  - Expected: Name="Mary-Jane", Surname="Smith-Jones"
- **Test 5**: Input with multiple spaces: "John  Doe"
  - Expected: May create empty token between spaces

### Integration Tests
- **Test 1**: Complete flow with normal input
- **Test 2**: Single token input
- **Test 3**: Many tokens input (> 3)
- **Test 4**: Empty input handling

## Performance Considerations
- UNSTRING is efficient single-pass operation
- Minimal memory overhead
- Execution time: negligible for short strings
- Modern alternatives (regex) may be more flexible but slightly slower

## Security Considerations
- **Input Length**: Limited to 20 characters
- **Buffer Safety**: UNSTRING with multiple targets prevents overflow
- **No Injection**: Simple string splitting is safe
- No authentication/authorization required
- No encryption needed
- **Production Recommendations**:
  - Add validation for minimum number of tokens
  - Handle empty tokens from multiple consecutive delimiters
  - Consider trimming whitespace
  - Validate name format (alphabetic characters)
