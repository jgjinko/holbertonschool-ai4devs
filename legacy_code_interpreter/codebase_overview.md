# Codebase Overview - osCommerce Online Merchant v2.2

## Age
Initial release in March 2000. Version 2.2 MS2, which remains the most representative legacy version, was released in July 2003.

## Size
Approximately 38,000 Lines of Code (LOC) in PHP.

## Main Dependencies
- **PHP 4.1+ / 5.0:** Developed before modern PHP standards (PSR) or Object-Oriented Programming (OOP) were widely adopted in the ecosystem.
- **MySQL 3.23 / 4.0:** Utilizes legacy `mysql_*` functions which are now deprecated and removed in modern PHP versions.
- **Register Globals:** Heavily dependent on the insecure `register_globals` PHP configuration.

## Known Issues or Pain Points
- **Mixed Presentation and Logic:** The codebase lacks a templating engine; business logic, database queries, and HTML are tightly coupled within the same files.
- **Procedural Architecture:** Almost entirely procedural with minimal use of classes, making it difficult to implement modern design patterns or dependency injection.
- **Security Vulnerabilities:** Frequent use of string concatenation for SQL queries makes the system highly susceptible to SQL injection. It also lacks modern CSRF protection.
- **No Automated Testing:** There is no unit testing or integration testing suite, making any refactoring effort high-risk.
- **Manual State Management:** Extensive use of the `$GLOBALS` array and manual session handling creates "spaghetti code" that is difficult to trace.