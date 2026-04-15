# Module: Database Wrapper (`functions/database.php`)

## Overview
This module provides a procedural abstraction layer over the legacy MySQL extension. It is responsible for connection management and query execution.

## Key Functions
- `tep_db_connect()`: Establishes a connection to the database.
- `tep_db_query($query)`: Executes a raw SQL string.
- `tep_db_fetch_array($result)`: Retrieves a row as an associative array.

## Security Note
**Warning**: This module does not support prepared statements. All variables must be manually sanitized using `tep_db_input()` before being passed to `tep_db_query()`.