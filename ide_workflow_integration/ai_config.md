# AI Configuration & Workflow Governance

This document defines the settings and specialized workflows for AI-powered coding within this repository.

## 1. Overview
We utilize **GitHub Copilot** as the primary AI coding assistant. To maintain consistency across the codebase, the AI is governed by the `.copilot-settings.yaml` file located in the project root.

## 2. Language-Specific Rules
To ensure the AI generates code that matches our standards, we have enforced the following:
- **JavaScript**: Follows the Airbnb style guide, requiring semicolons and single quotes.
- **Python**: Enforces PEP8 standards with mandatory type hints and Google-style docstrings.

## 3. Specialized AI Workflows
We have configured two primary specialized workflows to automate repetitive tasks:

### **Workflow A: Code Review (Security & Performance)**
- **Trigger**: Copilot Chat (`/review`)
- **Focus**: The AI is instructed to prioritize identifying SQL injection risks, insecure dependencies, and O(n^2) complexity in loops.

### **Workflow B: Documentation Generator**
- **Trigger**: Function creation
- **Focus**: Automatically suggests JSDoc or Google-style docstrings to ensure every public function is documented upon creation.

## 4. Manual Oversight Policy
AI suggestions are treated as "Draft" quality. All generated logic must pass:
1. Local linting checks (`ESLint`/`Flake8`).
2. Manual peer review or human-led audit.
3. Unit test verification.