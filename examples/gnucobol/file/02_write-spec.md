# 02_WRITE Specification

## Overview
A COBOL program that converts a sequential text file to an indexed file format. It reads from persons.txt and writes to output.dat as an indexed file with PERSON-ID as the key.

## Program Identification
- **Program ID**: 02_WRITE
- **Original File**: 02_write.cbl
- **Author**: Not specified
- **Date Written**: Not specified
- **Last Modified**: Available via file system

## Business Logic
### Purpose
This program demonstrates:
- Reading from sequential file
- Writing to indexed file
- File organization conversion
- Dynamic access mode for indexed files
- Record key definition
- File opening modes (INPUT, OUTPUT, I-O)

### Process Flow
1. Open PERSON-IN (sequential file) for INPUT
2. Open PERSON-OUT (indexed file) for OUTPUT, then close it
3. Reopen PERSON-OUT for I-O (read/write) mode
4. Loop until end of input file:
   - Read record from sequential file
   - Display record to console
   - Write record to indexed file (if not EOF)
5. Close both files
6. Terminate with STOP RUN

## Data Structures

### Input Files
| File Name | Record Format | Description |
|-----------|--------------|-------------|
| persons.txt | Fixed-width text | Sequential person records |

**File Location**: `../SampleData/persons.txt`
**Organization**: LINE SEQUENTIAL

### Output Files
| File Name | Record Format | Description |
|-----------|--------------|-------------|
| output.dat | Indexed | Indexed person records with ID as key |

**File Location**: `output.dat` (current directory)
**Organization**: INDEXED
**Access Mode**: DYNAMIC
**Record Key**: FO_PERSON-ID

### Working Storage Variables

| Variable Name | Type | Size | Purpose |
|--------------|------|------|---------|
| S_PERSON | Group | 44 chars | Working storage buffer |
| B_EOF | Alphanumeric | 1 char | End-of-file flag |

## File Operations

### Input File (PERSON-IN)
```cobol
SELECT PERSON-IN ASSIGN TO '../SampleData/persons.txt'
    ORGANIZATION IS LINE SEQUENTIAL
```
- **Mode**: INPUT
- **Operations**: READ

### Output File (PERSON-OUT)
```cobol
SELECT PERSON-OUT ASSIGN TO 'output.dat'
    ORGANIZATION IS INDEXED
    ACCESS IS DYNAMIC
    RECORD KEY IS FO_PERSON-ID
```
- **Mode**: OUTPUT (create), then I-O (read/write)
- **Operations**: WRITE
- **Key**: PERSON-ID for indexed access

### Open Sequence
1. OPEN OUTPUT - Creates new indexed file
2. CLOSE - Closes to finalize structure
3. OPEN I-O - Reopens for reading and writing

## Calculations and Transformations
None - Straight data copy from sequential to indexed format.

### Data Flow
Sequential File → Working Storage → Indexed File

## Error Handling
Minimal error handling:
- AT END for input file
- No duplicate key handling
- No write error handling
- No file not found handling

## Dependencies
### Called Programs
None

### External Resources
- Input file: `../SampleData/persons.txt`
- Output file: `output.dat`
- Standard output (console)

## Migration Considerations

### Recommended Target Architecture
- ETL (Extract, Transform, Load) component
- Data migration utility
- File format converter
- Database import tool

### Python Implementation Notes
```python
import sqlite3
from dataclasses import dataclass

@dataclass
class Person:
    id: int
    name: str
    surname: str

def convert_file_to_indexed():
    """Convert sequential file to indexed database."""
    # Create indexed file (SQLite database)
    conn = sqlite3.connect('output.db')
    cursor = conn.cursor()
    
    # Create table with indexed primary key
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS persons (
            id INTEGER PRIMARY KEY,
            name TEXT,
            surname TEXT
        )
    ''')
    
    try:
        # Read sequential file
        with open('../SampleData/persons.txt', 'r') as file:
            for line in file:
                if len(line.strip()) >= 44:
                    # Parse record
                    person = Person(
                        id=int(line[0:3].strip()),
                        name=line[3:19].strip(),
                        surname=line[19:44].strip()
                    )
                    
                    # Display
                    print(f"{person.id:03d}{person.name:16}{person.surname:25}")
                    
                    # Write to indexed file (database)
                    cursor.execute(
                        'INSERT OR REPLACE INTO persons VALUES (?, ?, ?)',
                        (person.id, person.name, person.surname)
                    )
        
        conn.commit()
    
    except FileNotFoundError:
        print("Error: Input file not found")
    finally:
        conn.close()

if __name__ == "__main__":
    convert_file_to_indexed()
```

**Python Alternatives:**
- SQLite for indexed storage
- pandas DataFrame with index
- shelve module for key-value storage
- HDF5 for large datasets

### Node.js Implementation Notes
```javascript
const fs = require('fs');
const readline = require('readline');
const sqlite3 = require('sqlite3').verbose();

async function convertFileToIndexed() {
    // Create indexed file (SQLite database)
    const db = new sqlite3.Database('output.db');
    
    // Create table with indexed primary key
    await new Promise((resolve, reject) => {
        db.run(`
            CREATE TABLE IF NOT EXISTS persons (
                id INTEGER PRIMARY KEY,
                name TEXT,
                surname TEXT
            )
        `, (err) => err ? reject(err) : resolve());
    });
    
    const fileStream = fs.createReadStream('../SampleData/persons.txt');
    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });
    
    const stmt = db.prepare('INSERT OR REPLACE INTO persons VALUES (?, ?, ?)');
    
    for await (const line of rl) {
        if (line.length >= 44) {
            const id = parseInt(line.substring(0, 3).trim());
            const name = line.substring(3, 19).trim();
            const surname = line.substring(19, 44).trim();
            
            console.log(`${id.toString().padStart(3, '0')}${name.padEnd(16)}${surname.padEnd(25)}`);
            
            stmt.run(id, name, surname);
        }
    }
    
    stmt.finalize();
    db.close();
}

convertFileToIndexed();
```

### Data Migration
**From**: Sequential text file
**To**: Indexed file (ISAM-style) or database

**Modern Equivalents:**
- SQLite database with PRIMARY KEY index
- MongoDB with indexed _id field
- Redis with key-value storage
- PostgreSQL with B-tree indexes

## Testing Scenarios
### Unit Tests
- **Test 1**: Convert file with 3 records
  - Expected: 3 records in indexed file
- **Test 2**: Verify indexed access
  - Expected: Can retrieve by key
- **Test 3**: Duplicate key handling
  - Expected: Proper error or replacement

### Integration Tests
- **Test 1**: Complete conversion process
  - Verify all records transferred
- **Test 2**: Verify output file structure
  - Check ISAM/indexed organization

## Performance Considerations
- Sequential read is efficient
- Indexed write may be slower than sequential
- Index building overhead during file creation
- For large files: Consider batch commits
- Trade-off: Slower writes for faster lookups

## Security Considerations
- **File Access**: Validate input/output paths
- **Data Integrity**: Ensure complete transfer
- **Key Uniqueness**: Handle duplicate keys
- **No Encryption**: Data in plain format
- **Production Recommendations**:
  - Add transaction support
  - Implement rollback on errors
  - Validate data before writing
  - Add audit logging
  - Consider data encryption
