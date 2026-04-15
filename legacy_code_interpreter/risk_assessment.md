# Risk Assessment - osCommerce Legacy Codebase (v2.2)

This document prioritizes the technical and security risks found in the legacy codebase, providing clear descriptions and implementation notes for refactoring.

---

## 1. SQL Injection Vulnerabilities
- **Description**: The application constructs database queries by concatenating raw user input directly into SQL strings without sanitization or parameterization.
- **Severity**: High
- **Notes**: This is the most critical security flaw. An attacker can bypass authentication or dump the entire database. Requires a shift to PDO or MySQLi with prepared statements.

## 2. PHP Version Incompatibility (Hard Deprecations)
- **Description**: The codebase utilizes the `mysql_` extension and relies on the `register_globals` directive, both of which were removed in modern PHP (7.x and 8.x).
- **Severity**: High
- **Notes**: The system is physically unable to run on modern, secure server environments. This forces the business to use outdated, vulnerable server software.

## 3. Absence of Automated Testing Suite
- **Description**: There are zero unit, integration, or end-to-end tests within the repository, meaning all verification is manual.
- **Severity**: High
- **Notes**: Any attempt to refactor the legacy "spaghetti" code carries a high risk of regression. Manual testing is slow and prone to human error, making modernization dangerous.

## 4. Insecure Password Hashing & Storage
- **Description**: User and administrator passwords are stored using outdated cryptographic algorithms (like plain MD5 or unsalted hashes) rather than modern, slow-hashing algorithms.
- **Severity**: High
- **Notes**: In the event of a database leak, passwords can be recovered almost instantly using rainbow tables. Must be updated to use `password_hash()` with Bcrypt or Argon2.

## 5. Cross-Site Scripting (XSS)
- **Description**: Input received from users is rendered back to the browser without consistent output encoding or context-aware escaping.
- **Severity**: Medium
- **Notes**: Attackers can inject malicious JavaScript to steal session cookies or deface the site. Modern templating engines should be implemented to enforce automatic escaping.

## 6. Tight Coupling and Global State
- **Description**: Business logic is heavily dependent on the `$GLOBALS` array and the massive `application_top.php` bootstrap file, creating a monolithic structure.
- **Severity**: Medium
- **Notes**: This creates "brittle" code where changing a variable in one section causes unexpected failures elsewhere. It prevents the use of modern MVC patterns or dependency injection.