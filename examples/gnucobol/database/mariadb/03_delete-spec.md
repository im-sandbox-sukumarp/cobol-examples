# 03_delete Specification

## Overview
A COBOL program demonstrating SQL DELETE operations using embedded SQL with MariaDB. It deletes king records matching specific criteria.

## Program Identification
- **Program ID**: 03_delete
- **Original File**: 03_delete.cbl
- **Database**: MariaDB (via ODBC)

## Business Logic
### Purpose
Demonstrates:
- SQL DELETE statement
- WHERE clause for conditional deletion
- Row counting for verification
- Transaction validation

### Process Flow
1. Connect to database
2. Count rows before deletion (cnt-old)
3. Set king-name to 'Rudolf'
4. DELETE records WHERE name = 'Rudolf'
5. Count rows after deletion (cnt-new)
6. Verify success (cnt-new < cnt-old)
7. Display result
8. Disconnect

## Data Structures
### Database Operations
**DELETE**: Removes records matching WHERE condition
**SELECT COUNT(*)**: Verifies deletion success

## Migration Considerations
### Python Implementation
```python
import pyodbc

conn = pyodbc.connect('...')
cursor = conn.cursor()

# Count before
cursor.execute('SELECT COUNT(*) FROM kings_of_poland')
cnt_old = cursor.fetchone()[0]
print(f"Rows before deletion: {cnt_old}")

# Delete
cursor.execute(
    'DELETE FROM kings_of_poland WHERE name = ?',
    ('Rudolf',)
)

# Count after
cursor.execute('SELECT COUNT(*) FROM kings_of_poland')
cnt_new = cursor.fetchone()[0]
print(f"Rows after deletion: {cnt_new}")

if cnt_new <= cnt_old:
    print("SUCCESS!")

conn.commit()
conn.close()
```

## Security Considerations
- **Data Loss**: Permanent deletion - backup recommended
- **Hardcoded Credentials**: Critical security issue
- **Production**: Implement soft deletes, audit logging, confirmation prompts
