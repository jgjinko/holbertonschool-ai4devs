# AI-Assisted Development Notes


These solutions were implemented using GitHub Copilot to evaluate the efficiency gain of an AI coding assistant.

| Task | AI Dev Time | Prompts Used | Notes |
| :--- | :--- | :--- | :--- |
| **Task 1** | 1.5 minutes | "JS function to validate email domain against a whitelist. Trim input, case-insensitive." | Copilot suggested the array destructuring `[user, domain]` which made the logic very clean. |
| **Task 2** | 2 minutes | "Function to aggregate transaction amounts by category from array of objects, round to 2 decimals." | The assistant favored `.reduce()`. I had to manually add a check for `null` inputs to meet the criteria. |
| **Task 3** | 3.5 minutes | "Regex to extract markdown links [text](url) but ignore images starting with ! in JS." | The AI generated the negative lookbehind `(?<!\!)` perfectly on the first try, which saved the most time. |

**Total AI-Assisted Effort: 7 Minutes**

### Observations
- **Efficiency**: The total development time dropped from **44 minutes (manual)** to **7 minutes (AI)**, a speed increase of approximately 84%.
- **Pattern Recognition**: The AI consistently suggested modern ES6+ patterns (like arrow functions and optional chaining) that were more concise than the manual baseline.
- **Role Shift**: My role shifted from "Writer" to "Reviewer," spending more time reading the generated code for edge-case safety than actually typing syntax.