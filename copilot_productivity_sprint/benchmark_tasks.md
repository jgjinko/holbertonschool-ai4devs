# Coding Assistant Benchmark Tasks

This document defines three modular tasks used to evaluate the speed and accuracy of the AI coding assistant.

---

## Task 1 - Email Domain Validator
**Requirements**: Implement a function that extracts the domain from an email string and validates it against a provided whitelist of allowed domains.
**Inputs**: 
- `email`: A string (e.g., "dev@corepoint.al").
- `whitelist`: An array of strings (e.g., ["gmail.com", "outlook.com", "corepoint.al"]).
**Outputs**: Boolean (true if valid and in whitelist, false otherwise).
**Acceptance Criteria**: 
- Must return `false` for malformed emails (missing @ or domain).
- Must be case-insensitive for the domain comparison.
- Must handle leading/trailing whitespace in the input string.

---

## Task 2 - Transaction Aggregator
**Requirements**: Process a list of transaction objects and return a single object containing the total sum of amounts grouped by category.
**Inputs**: An array of objects: `[{ "category": "Hosting", "amount": 20.00 }, { "category": "API", "amount": 5.50 }]`.
**Outputs**: A single object: `{ "Hosting": 20.00, "API": 5.50 }`.
**Acceptance Criteria**: 
- Returns an empty object `{}` if the input array is empty.
- Correctly sums multiple entries within the same category.
- Values must be rounded to two decimal places.

---

## Task 3 - Markdown Link Extractor
**Requirements**: Use a regular expression or a parsing library to find all Markdown links within a block of text and extract them into an array of objects.
**Inputs**: A string (e.g., "Check our [Website](https://example.com) and [Docs](https://docs.example.com)").
**Outputs**: An array of objects: `[{ "text": "Website", "url": "https://example.com" }, { "text": "Docs", "url": "https://docs.example.com" }]`.
**Acceptance Criteria**: 
- Successfully identifies the standard `[text](url)` format.
- Ignores images `![alt](url)`.
- Returns an empty array if no links are found.