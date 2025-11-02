# 03_REWRITE Specification

## Overview
A COBOL program demonstrating the REWRITE operation for updating records in an indexed file. It reads all records and anonymizes surnames by replacing them with "RODO anon."

## Program Identification
- **Program ID**: 03_REWRITE
- **Original File**: 03_rewrite.cbl
- **Author**: Not specified
- **Date Written**: Not specified
- **Last Modified**: Available via file system
- **Prerequisite**: Execute 02_write.cbl first to create output.dat

## Business Logic
### Purpose
This program demonstrates:
- REWRITE operation for updating records
- I-O mode for indexed files
- READ NEXT RECORD for sequential access
- In-place record modification
- Data anonymization/masking

### Process Flow
1. Open output.dat (indexed file) in I-O mode
2. Loop until end of file:
   - Read next record sequentially
   - If not EOF:
     - Modify surname field to "RODO anon."
     - Rewrite (update) the record in place
3. Close file
4. Terminate with STOP RUN

## Data Structures

### Input Files
| File Name | Record Format | Description |
|-----------|--------------|-------------|
| output.dat | Indexed | Indexed person records (from 02_write.cbl) |

**File Location**: `output.dat` (current directory)
**Organization**: INDEXED
**Access Mode**: DYNAMIC
**Record Key**: FI_PERSON-ID

### Output Files
Same file (output.dat) - modified in place

### Working Storage Variables

| Variable Name | Type | Size | Purpose |
|--------------|------|------|---------|
| B_EOF | Alphanumeric | 1 char | End-of-file flag |
| COUNTER | Numeric | 2 digits | Record counter (declared but unused) |

## File Operations

### File Definition
```cobol
SELECT PERSON-IN ASSIGN TO 'output.dat'
    ORGANIZATION IS INDEXED
    ACCESS IS DYNAMIC
    RECORD KEY IS FI_PERSON-ID
```

### Operations
1. **OPEN I-O PERSON-IN**: Opens file for read and write
2. **READ PERSON-IN NEXT RECORD**: Reads records sequentially
   - NEXT RECORD: Sequential access within indexed file
   - AT END: Triggered when no more records
3. **REWRITE FI_PERSON**: Updates current record in place
4. **CLOSE PERSON-IN**: Closes file

## Calculations and Transformations

### Data Modification
- **Original**: surname contains actual person's last name
- **Modified**: surname set to "RODO anon." (GDPR anonymization reference)
- **Operation**: `MOVE 'RODO anon.' TO FI_PERSON-SURNAME`

### RODO Note
"RODO" refers to GDPR (General Data Protection Regulation) in Polish. This demonstrates data anonymization for privacy compliance.

## Error Handling
Minimal error handling:
- AT END for file completion
- No error handling for:
  - File not found
  - Write errors
  - Concurrent access issues

## Dependencies
### Called Programs
None

### External Resources
- Indexed file: `output.dat`
- **Prerequisite**: File must be created by 02_write.cbl first

## Migration Considerations

### Recommended Target Architecture
- Data anonymization utility
- GDPR compliance tool
- Batch update processor
- ETL transformation component

### Python Implementation Notes
```python
import sqlite3

def anonymize_surnames():
    """Update all surnames to anonymize data."""
    try:
        # Open database (indexed file)
        conn = sqlite3.connect('output.db')
        cursor = conn.cursor()
        
        # Read all records
        cursor.execute('SELECT id FROM persons')
        records = cursor.fetchall()
        
        # Update each record
        for record in records:
            cursor.execute(
                'UPDATE persons SET surname = ? WHERE id = ?',
                ('RODO anon.', record[0])
            )
            print(f"Updated record ID: {record[0]}")
        
        conn.commit()
        print(f"Anonymized {len(records)} records")
    
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    anonymize_surnames()
```

**Python Equivalents:**
- SQL UPDATE statement for batch updates
- pandas DataFrame.loc for selective updates
- Dictionary update for in-memory modifications

### Node.js Implementation Notes
```javascript
const sqlite3 = require('sqlite3').verbose();

function anonymizeSurnames() {
    const db = new sqlite3.Database('output.db');
    
    db.serialize(() => {
        // Get all records
        db.all('SELECT id FROM persons', [], (err, rows) => {
            if (err) {
                console.error('Error:', err);
                return;
            }
            
            // Update each record
            const stmt = db.prepare('UPDATE persons SET surname = ? WHERE id = ?');
            
            rows.forEach(row => {
                stmt.run('RODO anon.', row.id);
                console.log(`Updated record ID: ${row.id}`);
            });
            
            stmt.finalize();
            console.log(`Anonymized ${rows.length} records`);
        });
    });
    
    db.close();
}

anonymizeSurnames();
```

### Data Migration
**Operation**: In-place update (UPDATE operation)
**Alternative Approaches:**
- Batch SQL UPDATE
- Stream processing for large files
- Create new file with anonymized data
- Use database transactions for safety

## Testing Scenarios
### Unit Tests
- **Test 1**: Rewrite single record
  - Expected: Surname changed to "RODO anon."
- **Test 2**: Rewrite all records
  - Expected: All surnames anonymized
- **Test 3**: Verify ID unchanged
  - Expected: Only surname field modified

### Integration Tests
- **Test 1**: Complete anonymization process
  - Verify all records updated
- **Test 2**: Data integrity check
  - Verify IDs and names unchanged
- **Test 3**: File still indexed after update
  - Verify can still access by key

## Performance Considerations
- Sequential READ for all records
- REWRITE for each record individually
- Could be optimized with batch updates
- For large files:
  - Consider batch processing
  - Use transactions
  - Implement progress tracking
- Indexed file overhead vs sequential file

## Security Considerations
- **Data Privacy**: Implements anonymization (GDPR compliance)
- **Backup**: Should backup before anonymizing
- **Audit Trail**: Should log anonymization operations
- **Reversibility**: Anonymization is irreversible
- **File Locking**: No concurrent access protection
- **Production Recommendations**:
  - Create backup before anonymization
  - Log all updates with timestamp
  - Implement transaction rollback capability
  - Add confirmation prompt
  - Consider selective anonymization
  - Verify file integrity after update
  - Implement access controls
