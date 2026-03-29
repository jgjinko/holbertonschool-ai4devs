# AI-Assisted Development Notes


This log tracks the interaction with the AI coding assistant to solve the benchmark tasks.

| Task | Prompt Used | AI Dev Time | Notes |
| :--- | :--- | :--- | :--- |
| **Task 1** | "Write a JS function to validate email domain against a whitelist. Trim input, case-insensitive, return false if invalid." | 1.5 min | Copilot provided the split/destructuring pattern instantly. I just had to verify the `@` count logic. |
| **Task 2** | "Create a function to aggregate transaction amounts by category from an array of objects. Round to 2 decimals." | 2 min | The AI initially forgot the empty array check; I had to add the optional chaining `?.length`. |
| **Task 3** | "Regex to extract markdown links [text](url) but ignore images starting with ! in JS." | 3 min | The AI generated the negative lookbehind correctly on the first try, saving significant manual testing time. |

**Total AI-Assisted Effort: 6.5 Minutes**

### Comparison Observations
- **Speed**: AI support reduced development time from 44 minutes to under 7 minutes (an 84% reduction).
- **Conciseness**: The AI favored modern ES6+ syntax (`reduce`, `matchAll`, destructuring) which resulted in fewer lines of code.
- **Verification**: The primary "human" role shifted from writing syntax to verifying edge cases (e.g., ensuring `null` inputs don't crash the script).