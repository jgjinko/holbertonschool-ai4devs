# Risk Assessment - osCommerce Legacy Codebase (v2.2)

This document prioritizes the technical and security risks found in the legacy codebase, providing clear descriptions and implementation notes for refactoring.

---

## 1. SQL Injection Vulnerabilities
- **Description**: The application constructs database queries by concatenating raw user input directly into SQL strings without sanitization or parameterization.
- **Severity**: High
- **Notes**: This is the most critical security flaw. An attacker can bypass authentication or dump the entire database. Requires a shift to PDO or MySQLi with prepared statements.

## 2. PHP Version Incompatibility (Hard Deprecations)
- **Description**: The codebase utilizes the `mysql_` extension and relies on the `register_globals` directive, both of which were deprecated and removed in modern PHP (7.x and 8.x).
- **Severity**: High
- **Notes**: The system is physically unable to run on modern, secure server environments. This forces the business to use outdated, vulnerable server software.

## 3. Absence of Automated Testing Suite
- **Description**: There are zero unit, integration, or end-to-end tests within the repository.
- **Severity**: High
- **Notes**: Any attempt to refactor the legacy "spaghetti" code carries a high risk of regression. Manual testing is currently the only safeguard, which is slow and prone to human error.

## 4. Cross-Site Scripting (XSS)
- **Description**: Input received from users (such as product reviews or customer profiles) is rendered back to the browser without consistent output encoding.
- **Severity**: Medium
- **Notes**: Attackers can inject malicious JavaScript to steal session cookies. Modern templating engines like Twig or Blade should be used to enforce automatic escaping.

## 5. Tight Coupling and Global State
- **Description**: Logic is heavily dependent on the `$GLOBALS` array and the massive `application_top.php` bootstrap file, which handles everything from sessions to currencies.
- **Severity**: Medium
- **Notes**: This makes the code "brittle." Changing a variable in one section often causes unexpected failures in unrelated modules. This prevents the adoption of a clean Model-View-Controller (MVC) architecture.

## 6. Lack of Secure Session Management
- **Description**: Session IDs are often passed via URLs (SID), and the application lacks modern flags like `HttpOnly` or `SameSite` for cookies.
- **Severity**: Medium
- **Notes**: Increases the risk of session hijacking and fixation attacks. Session handling should be moved to a standard, secure library rather than custom procedural functions.