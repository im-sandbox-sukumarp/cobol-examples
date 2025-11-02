# 01_select Specification

## Overview
A COBOL program demonstrating database SELECT operations using embedded SQL (ESQL) with MariaDB. It connects to a database, executes a cursor-based SELECT, and displays results.

## Program Identification
- **Program ID**: 01_select
- **Original File**: 01_select.cbl
- **Database**: MariaDB (via ODBC)
- **SQL Dialect**: Embedded COBOL SQL (ESQL/COBOL)

## Business Logic
### Purpose
Demonstrates:
- Embedded SQL in COBOL (EXEC SQL blocks)
- Database connection via ODBC
- DECLARE CURSOR for result sets
- FETCH loop for row retrieval
- SQL error checking with SQLSTATE
- Disconnection and resource cleanup

### Process Flow
1. Build ODBC connection string
2. Connect to MariaDB database
3. Declare cursor CURR_KINGS for SELECT statement
4. Open cursor
5. Loop fetching rows until SQLCODE = 100 (no more data):
   - Fetch row into host variables
   - Check SQL state
   - Display king data if not end-of-data
6. Disconnect from database
7. Terminate

## Data Structures
### Database Tables
**Table**: kings_of_poland
**Columns**: id, name, year_of_birth, year_of_death, reign_year_start, reign_year_end

### Host Variables (COBOL ↔ SQL interface)
| Variable | Type | Purpose |
|----------|------|---------|
| BUFFER | X(1024) | ODBC connection string |
| king-id | 9(10) | King ID from database |
| king-name | X(50) | King name |
| king-year_of_birth | 9(4) | Birth year |
| king-year_of_death | 9(4) | Death year |
| king-reign_year_start | 9(4) | Reign start |
| king-reign_year_end | 9(4) | Reign end |

## Migration Considerations
### Python Implementation
```python
import pyodbc

conn = pyodbc.connect(
    'DRIVER={MariaDB ODBC 3.0 Driver};'
    'SERVER=10.0.1.2;PORT=3306;'
    'DATABASE=coboldb;USER=cobolusr;'
    'PASSWORD=cobolExamplePassword;'
)

cursor = conn.cursor()
cursor.execute(
    'SELECT id, name, year_of_birth, year_of_death, '
    'reign_year_start, reign_year_end FROM kings_of_poland'
)

for row in cursor.fetchall():
    print(f"{row.id} | {row.name} | {row.year_of_birth} | "
          f"{row.year_of_death} | {row.reign_year_start} | "
          f"{row.reign_year_end}")

conn.close()
```

### Node.js Implementation
```javascript
const mariadb = require('mariadb');

async function selectKings() {
    const conn = await mariadb.createConnection({
        host: '10.0.1.2',
        port: 3306,
        user: 'cobolusr',
        password: 'cobolExamplePassword',
        database: 'coboldb'
    });
    
    const rows = await conn.query(
        'SELECT id, name, year_of_birth, year_of_death, ' +
        'reign_year_start, reign_year_end FROM kings_of_poland'
    );
    
    rows.forEach(row => {
        console.log(`${row.id} | ${row.name} | ${row.year_of_birth} | ` +
                    `${row.year_of_death} | ${row.reign_year_start} | ` +
                    `${row.reign_year_end}`);
    });
    
    await conn.end();
}

selectKings();
```

## Security Considerations
- **Hardcoded Credentials**: Password in source code (CRITICAL security issue)
- **SQL Injection**: Protected by parameterized queries
- **Production Recommendations**:
  - Use environment variables for credentials
  - Implement connection pooling
  - Use SSL/TLS for database connections
  - Rotate passwords regularly
  - Implement proper error handling without exposing internals
