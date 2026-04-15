# Module: Session Management (`functions/sessions.php`)

## Overview
Handles user persistence across requests. It relies on custom session handlers that can store data either in the file system or the `sessions` table in the database.

## Key Functions
- `tep_session_start()`: Initializes the session logic.
- `tep_session_register($variable)`: Registers a global variable into the session.
- `tep_session_is_registered($variable)`: Checks if a specific key exists in the session.

## Issues
Relies on deprecated "Register Globals" logic. Modern implementations should use the `$_SESSION` superglobal directly.