# Risk Assessment - osCommerce Legacy Codebase

| Risk | Severity | Notes |
| :--- | :--- | :--- |
| **SQL Injection Vulnerabilities** | **High** | The codebase uses string concatenation for queries. Without prepared statements, the database is highly vulnerable to unauthorized access and data breaches. |
| **PHP Version Incompatibility** | **High** | Relies on `mysql_*` functions and `register_globals`, which were removed in modern PHP versions. The system cannot run on modern, secure servers without a complete rewrite. |
| **Lack of Automated Testing** | **High** | With zero unit or integration tests, any logic change has a high probability of introducing "breaking" bugs that remain undetected until production. |
| **Cross-Site Scripting (XSS)** | **Medium** | Input validation and output encoding are inconsistent across the UI, allowing potential attackers to inject malicious scripts into the storefront. |
| **Global State & Tight Coupling** | **Medium** | Heavy reliance on `application_top.php` and `$GLOBALS` makes it impossible to isolate components for refactoring or modernizing individual features. |
| **No Dependency Management** | **Low** | Lack of a package manager (like Composer) means updates to third-party scripts must be done manually, increasing the risk of using outdated, insecure libraries. |