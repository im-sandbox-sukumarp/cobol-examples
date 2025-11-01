# 04_ddl Specification

## Overview
A COBOL program demonstrating SQL DDL (Data Definition Language) operations using embedded SQL with MariaDB. It creates and drops a test table using dynamic SQL.

## Program Identification
- **Program ID**: 02_ddl (note: filename is 04_ddl.cbl)
- **Original File**: 04_ddl.cbl
- **Database**: MariaDB (via ODBC)

## Business Logic
### Purpose
Demonstrates:
- CREATE TABLE statement
- DROP TABLE statement
- EXECUTE IMMEDIATE for dynamic SQL
- SQL state checking (42S01 = table exists)
- DDL operations in COBOL

### Process Flow
1. Connect to database
2. Build CREATE TABLE SQL in BUFFER
3. Execute CREATE TABLE testtable:
   - Columns: id (INT AUTO_INCREMENT PRIMARY KEY), name (VARCHAR(100))
   - Check SQLSTATE='42S01' (table exists error)
4. Display creation result
5. Build DROP TABLE SQL
6. Execute DROP TABLE testtable
7. Display drop result
8. Disconnect

## Data Structures
### Table Schema
**Table**: testtable
**Columns**:
- id: INT NOT NULL AUTO_INCREMENT PRIMARY KEY
- name: VARCHAR(100) NOT NULL

## Migration Considerations
### Python Implementation
```python
import pyodbc

conn = pyodbc.connect('...')
cursor = conn.cursor()

# CREATE TABLE
try:
    cursor.execute(
        'CREATE TABLE testtable('
        'id INT NOT NULL AUTO_INCREMENT,'
        'name VARCHAR(100) NOT NULL,'
        'PRIMARY KEY (id))'
    )
    print("table testtable created")
except pyodbc.Error as e:
    if 'already exists' in str(e):
        print("Table testtable already exists.")

# DROP TABLE
cursor.execute('DROP TABLE testtable')
print("table testtable dropped")

conn.commit()
conn.close()
```

### Node.js Implementation
```javascript
const mariadb = require('mariadb');

async function ddlOperations() {
    const conn = await mariadb.createConnection({...});
    
    // CREATE TABLE
    try {
        await conn.query(
            'CREATE TABLE testtable(' +
            'id INT NOT NULL AUTO_INCREMENT,' +
            'name VARCHAR(100) NOT NULL,' +
            'PRIMARY KEY (id))'
        );
        console.log("table testtable created");
    } catch (err) {
        if (err.code === 'ER_TABLE_EXISTS_ERROR') {
            console.log("Table testtable already exists.");
        }
    }
    
    // DROP TABLE
    await conn.query('DROP TABLE testtable');
    console.log("table testtable dropped");
    
    await conn.end();
}
```

## Security Considerations
- **DDL Operations**: Require elevated privileges
- **Production**: Restrict DDL to DBAs, use migration tools, version control schema changes
- **Hardcoded Credentials**: Critical security issue
