# 02_insert_update Specification

## Overview
A COBOL program demonstrating SQL INSERT and UPDATE operations using embedded SQL with MariaDB. It adds a new king record and then updates it.

## Program Identification
- **Program ID**: 02_insert_update
- **Original File**: 02_insert_update.cbl
- **Database**: MariaDB (via ODBC)

## Business Logic
### Purpose
Demonstrates:
- SQL INSERT statement
- SQL UPDATE statement
- Row counting with SELECT COUNT(*)
- Parameterized SQL with host variables
- Transaction verification

### Process Flow
1. Connect to database
2. Count existing rows (cnt-old)
3. Prepare king data: "rudolf xyz", years 1281-1307
4. INSERT new king record
5. Count rows after insertion (cnt-new)
6. Verify success (cnt-new > cnt-old)
7. UPDATE king name from "rudolf xyz" to "Rudolf"
8. Display success message
9. Disconnect

## Data Structures
### Database Operations
**INSERT**: Adds new king record with name, birth/death years, reign years
**UPDATE**: Changes name field based on WHERE clause

## Migration Considerations
### Python Implementation
```python
import pyodbc

conn = pyodbc.connect('...')  # Connection string
cursor = conn.cursor()

# Count before
cursor.execute('SELECT COUNT(*) FROM kings_of_poland')
cnt_old = cursor.fetchone()[0]

# Insert
cursor.execute(
    'INSERT INTO kings_of_poland (name, year_of_birth, year_of_death, '
    'reign_year_start, reign_year_end) VALUES (?, ?, ?, ?, ?)',
    ('rudolf xyz', 1281, 1307, 1306, 1307)
)

# Count after
cursor.execute('SELECT COUNT(*) FROM kings_of_poland')
cnt_new = cursor.fetchone()[0]

if cnt_new > cnt_old:
    print("SUCCESS!")

# Update
cursor.execute(
    'UPDATE kings_of_poland SET name = ? WHERE name = ?',
    ('Rudolf', 'rudolf xyz')
)

conn.commit()
conn.close()
```

## Security Considerations
- **Hardcoded Credentials**: Critical issue
- **SQL Injection**: Protected by parameterized queries
- **Transaction Management**: Consider explicit transactions
- **Production**: Use connection pooling, proper error handling, credentials management
