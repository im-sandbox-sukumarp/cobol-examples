# 04_START_AND_DELETE Specification

## Overview
A COBOL program demonstrating the START and DELETE operations for indexed files. It positions to records with ID > 10 and deletes all matching records.

## Program Identification
- **Program ID**: 04_START_AND_DELETE
- **Original File**: 04_start_and_delete.cbl
- **Author**: Not specified
- **Date Written**: Not specified
- **Last Modified**: Available via file system
- **Prerequisite**: Execute 02_write.cbl first to create output.dat

## Business Logic
### Purpose
This program demonstrates:
- START operation for positioning in indexed file
- KEY IS GREATER THAN clause
- DELETE RECORD operation
- Sequential processing from specific position
- Record removal from indexed file

### Process Flow
1. Open output.dat (indexed file) in I-O mode
2. Set FI_PERSON-ID to 10
3. Execute START to position at first record with ID > 10
4. Loop until end of file:
   - Read next record into S_PERSON
   - If not EOF:
     - Display "Removing" message with record data
     - Delete current record
5. Close file
6. Terminate with STOP RUN

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
Same file (output.dat) - modified with records deleted

### Working Storage Variables

| Variable Name | Type | Size | Purpose |
|--------------|------|------|---------|
| S_PERSON | Group | 44 chars | Working storage for display |
| B_EOF | Alphanumeric | 1 char | End-of-file flag |
| COUNTER | Numeric | 2 digits | Declared but unused |

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
2. **START PERSON-IN KEY IS GREATER THAN FI_PERSON-ID**:
   - Positions file pointer to first record where ID > 10
   - Subsequent READ operations start from this position
3. **READ PERSON-IN NEXT RECORD INTO S_PERSON**:
   - Reads from current position sequentially
   - INTO clause copies to working storage
4. **DELETE PERSON-IN RECORD**:
   - Deletes the current record (last record read)
   - Record removed from indexed file
5. **CLOSE PERSON-IN**: Closes file

## Calculations and Transformations
None - This is a record deletion program with no data transformation.

### Deletion Criteria
- Deletes all records with ID > 10
- START positions at first qualifying record
- Sequential reading and deletion continues until EOF

## Error Handling
Minimal error handling:
- AT END for file completion
- No error handling for:
  - START failure (no matching records)
  - DELETE errors
  - File not found
  - Concurrent access

## Dependencies
### Called Programs
None

### External Resources
- Indexed file: `output.dat`
- Standard output (console)
- **Prerequisite**: File created by 02_write.cbl

## Migration Considerations

### Recommended Target Architecture
- Data purge utility
- Archive cleanup tool
- Record retention manager
- Batch deletion processor

### Python Implementation Notes
```python
import sqlite3

def delete_records_greater_than(threshold_id):
    """Delete all records with ID greater than threshold."""
    try:
        # Open database
        conn = sqlite3.connect('output.db')
        cursor = conn.cursor()
        
        # Find records to delete
        cursor.execute(
            'SELECT id, name, surname FROM persons WHERE id > ? ORDER BY id',
            (threshold_id,)
        )
        
        records = cursor.fetchall()
        
        # Delete each record
        for record in records:
            print(f"Removing{record[0]:03d}{record[1]:16}{record[2]:25}")
            cursor.execute('DELETE FROM persons WHERE id = ?', (record[0],))
        
        conn.commit()
        print(f"Deleted {len(records)} records")
    
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    delete_records_greater_than(10)
```

**Python Equivalents:**
- SQL DELETE with WHERE clause
- SQL SELECT for preview before delete
- Transaction management with commit/rollback
- pandas DataFrame filtering and deletion

### Node.js Implementation Notes
```javascript
const sqlite3 = require('sqlite3').verbose();

function deleteRecordsGreaterThan(thresholdId) {
    const db = new sqlite3.Database('output.db');
    
    db.serialize(() => {
        // Find records to delete
        db.all(
            'SELECT id, name, surname FROM persons WHERE id > ? ORDER BY id',
            [thresholdId],
            (err, rows) => {
                if (err) {
                    console.error('Error:', err);
                    return;
                }
                
                // Delete each record
                const stmt = db.prepare('DELETE FROM persons WHERE id = ?');
                
                rows.forEach(row => {
                    console.log(
                        `Removing${row.id.toString().padStart(3, '0')}` +
                        `${row.name.padEnd(16)}${row.surname.padEnd(25)}`
                    );
                    stmt.run(row.id);
                });
                
                stmt.finalize();
                console.log(`Deleted ${rows.length} records`);
            }
        );
    });
    
    db.close();
}

deleteRecordsGreaterThan(10);
```

**JavaScript Equivalents:**
- SQL DELETE with WHERE condition
- Array.filter() for in-memory filtering
- Database transactions
- Async/await for cleaner code

### Data Migration
**Operation**: Conditional deletion (DELETE WHERE)
**Modern Equivalents:**
- SQL DELETE with WHERE clause
- Soft delete (mark as deleted, don't remove)
- Archive before delete (move to archive table)
- Logical deletion with timestamp

## Testing Scenarios
### Unit Tests
- **Test 1**: Delete records with ID > 10
  - Input: Records with IDs 1-15
  - Expected: Records 11-15 deleted, 1-10 remain
- **Test 2**: No matching records
  - Input: All IDs ≤ 10
  - Expected: No deletions, no errors
- **Test 3**: All records match
  - Input: All IDs > 10
  - Expected: All records deleted

### Integration Tests
- **Test 1**: Complete deletion process
  - Verify correct records deleted
  - Verify remaining records intact
- **Test 2**: File integrity after deletion
  - Verify indexed file still functional
  - Verify can still access remaining records by key

## Performance Considerations
- START operation is efficient with indexed file
- Sequential deletion vs batch DELETE
- For large files:
  - Consider batch deletion
  - Use transactions
  - Implement progress tracking
- Indexed file overhead for maintaining index
- Reindexing may occur after deletions

## Security Considerations
- **Data Loss**: Permanent deletion, no recovery
- **Backup**: Should backup before bulk deletion
- **Audit Trail**: Should log deletions
- **Confirmation**: Should prompt before delete
- **Transaction Safety**: No rollback capability
- **Production Recommendations**:
  - CRITICAL: Create backup before deletion
  - Implement "soft delete" flag instead
  - Log all deletions with timestamp and user
  - Add confirmation prompt
  - Implement transaction with rollback
  - Consider archiving instead of deleting
  - Add WHERE clause validation
  - Implement access controls and permissions
  - Test on copy of data first
