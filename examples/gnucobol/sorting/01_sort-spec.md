# 01_SORT Specification

## Overview
A COBOL program demonstrating the SORT verb for sorting records in a file. It sorts person records by surname in ascending order using a work file.

## Program Identification
- **Program ID**: 01_SORT
- **Original File**: 01_sort.cbl
- **Author**: Not specified
- **Date Written**: Not specified
- **Last Modified**: Available via file system
- **Note**: Comment suggests executing files/02_write.cbl first, but program works independently with persons.txt

## Business Logic
### Purpose
This program demonstrates:
- SORT verb for file sorting
- Work file (SD - Sort Description) usage
- USING and GIVING clauses
- Sorting by ascending key
- Multi-field record sorting
- Reading sorted output

### Process Flow
1. Execute SORT operation:
   - Read from F-INPUT (persons.txt)
   - Sort by surname in ascending order
   - Write sorted results to F-OUTPUT (sortedOutput.dat)
   - Use F-WORK as temporary work file
2. Display "Finished!" message
3. Open sorted output file
4. Read and display all sorted records
5. Close output file
6. Terminate with STOP RUN

## Data Structures

### Input Files
| File Name | Record Format | Description |
|-----------|--------------|-------------|
| persons.txt | Fixed-width text | Unsorted person records |

**File Location**: `../SampleData/persons.txt`
**Organization**: LINE SEQUENTIAL

### Output Files
| File Name | Record Format | Description |
|-----------|--------------|-------------|
| sortedOutput.dat | Fixed-width text | Sorted person records |

**File Location**: `sortedOutput.dat` (current directory)
**Organization**: LINE SEQUENTIAL

### Work Files
| File Name | Record Format | Description |
|-----------|--------------|-------------|
| work.tmp | Temporary | Work file for sort operation |

**File Type**: SD (Sort Description)
**Usage**: Internal to SORT operation

### Working Storage Variables

| Variable Name | Type | Size | Purpose |
|--------------|------|------|---------|
| S-PERSON | Group | 44 chars | Display buffer for sorted records |
| B_EOF | Alphanumeric | 1 char | End-of-file flag |

## File Operations

### SORT Operation
```cobol
SORT F-WORK ON ASCENDING KEY OUT_PERSON-SURNAME
    USING F-INPUT GIVING F-OUTPUT
```

**Components:**
- **F-WORK**: Work file for sorting (SD type)
- **ON ASCENDING KEY OUT_PERSON-SURNAME**: Sort by surname field, ascending
- **USING F-INPUT**: Input file to sort
- **GIVING F-OUTPUT**: Output file for sorted results

**Process:**
1. SORT automatically opens input and output files
2. Reads all records from input
3. Sorts in memory/work file
4. Writes sorted records to output
5. Automatically closes files

## Calculations and Transformations

### Sorting Logic
- **Sort Key**: PERSON-SURNAME field
- **Sort Order**: Ascending (A-Z)
- **Algorithm**: Internal COBOL sort (typically quicksort or mergesort)
- **Stability**: May not preserve original order for equal keys

## Error Handling
Minimal error handling:
- No error handling for SORT operation failures
- No checking for input file existence
- No validation of sort success
- AT END for reading sorted output

## Dependencies
### Called Programs
None

### External Resources
- Input file: `../SampleData/persons.txt`
- Output file: `sortedOutput.dat`
- Work file: `work.tmp` (temporary)
- Standard output (console)

## Migration Considerations

### Recommended Target Architecture
- Data sorting utility
- ETL transformation component
- Report generation tool
- Batch processing application

### Python Implementation Notes
```python
from dataclasses import dataclass
from typing import List

@dataclass
class Person:
    id: str
    name: str
    surname: str
    
    def __str__(self):
        return f"{self.id}{self.name:16}{self.surname:25}"

def sort_person_file():
    """Sort person records by surname."""
    persons = []
    
    try:
        # Read input file
        with open('../SampleData/persons.txt', 'r') as file:
            for line in file:
                if len(line.strip()) >= 44:
                    person = Person(
                        id=line[0:3],
                        name=line[3:19].strip(),
                        surname=line[19:44].strip()
                    )
                    persons.append(person)
        
        # Sort by surname
        persons.sort(key=lambda p: p.surname)
        
        # Write sorted output
        with open('sortedOutput.dat', 'w') as file:
            for person in persons:
                file.write(str(person) + '\n')
        
        print("Finished!")
        
        # Display sorted records
        for person in persons:
            print(person)
    
    except FileNotFoundError:
        print("Error: Input file not found")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    sort_person_file()
```

**Python Equivalents:**
- `list.sort(key=...)` for in-memory sorting
- `sorted()` function for creating sorted copy
- Lambda functions for sort key
- File I/O for reading and writing

### Node.js Implementation Notes
```javascript
const fs = require('fs');
const readline = require('readline');

class Person {
    constructor(id, name, surname) {
        this.id = id;
        this.name = name;
        this.surname = surname;
    }
    
    toString() {
        return `${this.id}${this.name.padEnd(16)}${this.surname.padEnd(25)}`;
    }
}

async function sortPersonFile() {
    const persons = [];
    
    try {
        // Read input file
        const fileStream = fs.createReadStream('../SampleData/persons.txt');
        const rl = readline.createInterface({
            input: fileStream,
            crlfDelay: Infinity
        });
        
        for await (const line of rl) {
            if (line.length >= 44) {
                const person = new Person(
                    line.substring(0, 3),
                    line.substring(3, 19).trim(),
                    line.substring(19, 44).trim()
                );
                persons.push(person);
            }
        }
        
        // Sort by surname
        persons.sort((a, b) => a.surname.localeCompare(b.surname));
        
        // Write sorted output
        const output = persons.map(p => p.toString()).join('\n');
        fs.writeFileSync('sortedOutput.dat', output + '\n');
        
        console.log("Finished!");
        
        // Display sorted records
        persons.forEach(p => console.log(p.toString()));
        
    } catch (error) {
        console.error('Error:', error);
    }
}

sortPersonFile();
```

### Data Migration
**Operation**: File-based sorting
**Modern Alternatives:**
- Database ORDER BY clause
- In-memory sorting with libraries
- Stream processing for large files
- External sort for very large datasets

## Testing Scenarios
### Unit Tests
- **Test 1**: Sort 3 records
  - Input: Smith, Jones, Anderson
  - Expected: Anderson, Jones, Smith
- **Test 2**: Already sorted file
  - Expected: Same order maintained
- **Test 3**: Reverse sorted file
  - Expected: Complete reversal
- **Test 4**: Duplicate surnames
  - Expected: Any valid order for duplicates

### Integration Tests
- **Test 1**: Complete sort process
  - Verify all records in output
  - Verify correct sort order
- **Test 2**: Large file handling
  - Test with many records

## Performance Considerations
- COBOL SORT is optimized and efficient
- Work file allows external sorting for large datasets
- For very large files, may use disk-based sorting
- Memory usage depends on file size
- Modern alternatives:
  - Database sorting (usually faster)
  - Parallel sorting algorithms
  - Stream processing for memory efficiency

## Security Considerations
- **File Access**: Validate input/output paths
- **Work File**: Temporary file should be secured
- **Data Integrity**: Verify all records sorted
- **No Validation**: Input data not validated
- **Production Recommendations**:
  - Validate input file format
  - Check sort completion status
  - Clean up work files after sorting
  - Add error handling for SORT failures
  - Implement file locking for concurrent access
  - Consider data sanitization
