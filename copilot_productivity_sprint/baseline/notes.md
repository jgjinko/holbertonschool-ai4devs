# Baseline Development Notes

These solutions were implemented manually to serve as a control group for the AI Coding Assistant benchmark.

| Task | Estimated Manual Time | Notes |
| :--- | :--- | :--- |
| **Task 1** | 10 minutes | Focused on ensuring `split('@')` didn't break on multiple `@` symbols or empty strings. |
| **Task 2** | 12 minutes | Used `Number.EPSILON` for more accurate rounding to meet the 2-decimal place criteria. |
| **Task 3** | 22 minutes | Spent the most time refining the Regex to correctly distinguish between standard links and image syntax. |

**Total Manual Effort: 44 Minutes**

### Observations
- Manual implementation ensures high control over edge cases (like whitespace and case sensitivity).
- Regular expressions for parsing (Task 3) remain the most time-consuming part of manual scripting.