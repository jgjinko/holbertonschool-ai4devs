# Workflow Baseline

This document outlines the standard development environment and performance metrics prior to the integration of AI-assisted coding tools.

## Current IDE Setup
- **Primary IDE**: Visual Studio Code (v1.114.0)
- **Key Extensions**: 
  - **ESLint**: For standardizing code quality and catching syntax errors.
  - **Prettier**: For automated code formatting.
  - **GitLens**: For tracking version history and managing commits.
  - **Live Server**: For real-time web development testing.
- **Language/Environment**: JavaScript (Node.js runtime), HTML/CSS.

## Pain Points
- **Manual Regex Construction**: Writing and testing complex regular expressions (like Markdown link extraction) consumes a disproportionate amount of development time.
- **Boilerplate Fatigue**: Repetitive tasks, such as setting up CRUD endpoints or basic validation logic, distract from solving core business problems.
- **Context-Switching for Docs**: Moving between the code editor and documentation files (like `setup_notes.md`) breaks focus and slows down the delivery cycle.

## Productivity Metrics
- **Avg Task Completion**: 15–20 minutes (for small-to-medium utility functions).
- **Bug Fix Turnaround**: ~45 minutes (including identification, manual testing, and verification).
- **Weekly Commits**: ~15–20 (focused on feature modules and manual refactoring).
- **Manual Baseline Total**: 44 minutes for 3 standard logic tasks.