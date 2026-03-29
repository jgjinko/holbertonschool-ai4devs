# Productivity Comparison: Manual vs. AI-Assisted

This document quantifies the performance difference between traditional manual coding and using GitHub Copilot for common development tasks.

| Metric | Without AI | With AI | Difference |
| :--- | :---: | :---: | :---: |
| **Total Completion Time (min)** | 44 | 7 | -84% |
| **Average Time per Task (min)** | 14.7 | 2.3 | -84% |
| **Lines of Code (LOC) Written** | 78 | 42 | -46% |
| **Bugs / Test Failures** | 2 | 1 | -50% |

## Metric Analysis

### 1. Completion Time
The most significant gain was in speed. Manual development required significant time for syntax research (especially Regex) and manual input sanitization. The AI reduced this to just the time needed for prompting and verification.

### 2. Lines of Code (LOC)
The AI assistant favored concise ES6+ patterns, such as arrow functions, array destructuring, and `.reduce()`. This resulted in nearly 50% fewer lines of code while maintaining (or improving) functionality and readability.

### 3. Bugs and Quality
- **Manual**: Encountered a minor rounding error in the aggregator and a regex backtracking issue.
- **AI**: The AI initially missed a null-check for the aggregator input, which was caught during the "Reviewer" phase. Overall, the AI's logic for standard patterns was more robust on the first attempt.

## Final Conclusion
Using an AI coding assistant transformed the workflow from a **writing-heavy** process to a **verification-heavy** process. For these types of utility tasks, the productivity increase is approximately 6x.