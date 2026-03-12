# Prompt Patterns Library

## Project Introduction

The **Prompt Patterns Library** is a curated collection of carefully crafted prompt templates designed to leverage AI assistance effectively across the entire software development lifecycle. Each template is optimized for specific development tasks, combining role-based instructions, structured input placeholders, and clear output expectations.

This library helps developers:
- **Accelerate code reviews** with comprehensive checklists
- **Improve code quality** through refactoring and style optimization
- **Enhance security** by identifying vulnerabilities and privacy concerns
- **Boost testing coverage** with automated test generation
- **Design better architecture** using established design patterns
- **Document effectively** with standardized documentation templates

Whether you're building features, maintaining code, or ensuring quality, these prompts provide a framework for consistent, high-quality AI-assisted development.

---

## Categories Overview

The library is organized into six main categories, each addressing a specific aspect of the development process:

| Category | Purpose | Key Focus |
|----------|---------|-----------|
| **Code Quality & Maintenance** | Improve readability and health of existing code | Refactoring, style, comments, dead code |
| **Testing & Quality Assurance** | Ensure comprehensive test coverage and validation | Unit tests, test cases, regression testing |
| **Security & Compliance** | Identify risks and ensure regulatory compliance | Vulnerabilities, privacy, data protection |
| **Documentation** | Create clear, comprehensive documentation | APIs, READMEs, interfaces |
| **Performance & Architecture** | Optimize performance and design systems | Speed, complexity, patterns, dependencies |
| **Code Review & Analysis** | Evaluate code quality and identify issues | Reviews, errors, bug detection |

---

## Templates by Category

### 1. Code Quality & Maintenance

Templates for improving code clarity, consistency, and long-term maintainability.

- [**Refactoring**](./prompts/refactoring.md) - Refactor code for clarity and performance with detailed explanations of changes
- [**Code Comments**](./prompts/code_comments.md) - Generate meaningful comments that explain intent and complex logic
- [**Style Enforcement**](./prompts/style_enforcement.md) - Identify and fix style violations across codebases
- [**Dead Code Removal**](./prompts/dead_code_removal.md) - Find and safely remove unused code and imports

### 2. Testing & Quality Assurance

Templates for generating tests and validation strategies to ensure code reliability.

- [**Unit Test Generation**](./prompts/unit_test_generation.md) - Create comprehensive unit tests covering normal cases, edge cases, and error conditions
- [**Test Case Design**](./prompts/test_case_design.md) - Design effective test cases with clear scenarios and expected outcomes
- [**Regression Testing**](./prompts/regression_testing.md) - Plan and execute regression test strategies for safe deployments

### 3. Security & Compliance

Templates for identifying security risks and ensuring compliance with regulations.

- [**Vulnerability Detection**](./prompts/vulnerability_detection.md) - Identify security vulnerabilities and suggest fixes with severity ratings
- [**Data Privacy Audit**](./prompts/data_privacy_audit.md) - Audit code for GDPR, CCPA, and other privacy compliance requirements

### 4. Documentation

Templates for creating clear, developer-friendly documentation.

- [**API Documentation**](./prompts/api_documentation.md) - Generate comprehensive API documentation with examples and error codes
- [**README Writing**](./prompts/readme_writing.md) - Create effective READMEs with setup, usage, and contribution guidelines
- [**Interface Design**](./prompts/interface_design.md) - Document interfaces, contracts, and expected behaviors

### 5. Performance & Architecture

Templates for optimizing performance and designing robust systems.

- [**Performance Optimization**](./prompts/performance_optimization.md) - Analyze and optimize code with complexity analysis and benchmarking recommendations
- [**Design Patterns**](./prompts/design_patterns.md) - Suggest appropriate design patterns with implementation examples and trade-offs
- [**Dependency Analysis**](./prompts/dependency_analysis.md) - Analyze dependencies for conflicts, security issues, and optimization opportunities

### 6. Code Review & Analysis

Templates for evaluating code quality and identifying issues.

- [**Code Review Checklist**](./prompts/code_review_checklist.md) - Generate context-specific code review checklists for your tech stack and compliance needs
- [**Error Analysis**](./prompts/error_analysis.md) - Analyze error messages and logs to identify root causes and solutions
- [**Bug Identification**](./prompts/bug_identification.md) - Identify potential bugs by analyzing code logic and edge cases

---

## Example Usage

The [**Prompt Examples**](./prompt_examples.md) document provides tested, real-world examples of five key templates in action:

1. **Refactoring Prompt** - Transform messy code into clean, Pythonic implementations
2. **Unit Test Generation** - Generate comprehensive pytest suites from function specifications
3. **Code Review Checklist** - Create tech-stack-specific checklists with compliance requirements
4. **Performance Optimization** - Analyze and optimize algorithms with Big O analysis
5. **Design Pattern Application** - Architect solutions using established patterns

Each example includes:
- The filled prompt with specific values
- Real code/text input
- AI-generated output
- Detailed feedback on quality and effectiveness

👉 **Start here**: [View Prompt Testing Examples](./prompt_examples.md)

---

## Quick Start

1. **Choose a template** from the category that matches your task
2. **Read the template file** to understand the role, task, and expected output
3. **Fill in the placeholders** with your specific code, context, or requirements
4. **Submit to your AI assistant** (Claude, ChatGPT, etc.)
5. **Review and iterate** - The examples show typical output quality

### Example Workflow

```
Need to refactor a Python function?
↓
Go to: Code Quality & Maintenance → Refactoring
↓
Open: prompts/refactoring.md
↓
Fill placeholders: [LANGUAGE] = Python, [CODE_BLOCK] = your function
↓
Paste into AI chat and get optimized code with explanations
```

---

## Tips for Best Results

- **Be specific**: Fill all placeholders with complete, accurate information
- **Provide context**: Include relevant requirements, constraints, or business rules
- **Test the output**: Review AI results before integrating into your codebase
- **Iterate**: Refine prompts based on output quality for your use cases
- **Combine templates**: Use multiple templates for complex tasks (e.g., refactor + test generation)

---

## Use Cases

### For Individual Developers
- Improve code quality through automated refactoring suggestions
- Generate test suites quickly without writing boilerplate
- Catch security issues before deployment
- Learn design patterns in context

### For Code Reviewers
- Use code review checklists for consistency across projects
- Identify performance bottlenecks systematically
- Ensure compliance requirements are met
- Reduce review time with structured guidance

### For Teams
- Standardize code quality expectations
- Create consistent documentation across services
- Establish security practices
- Accelerate onboarding with templated workflows

### For DevOps/Platform Teams
- Audit dependencies for security and conflicts
- Document infrastructure and APIs
- Analyze performance at scale
- Create compliance reports

---

## File Structure

```
prompt_patterns_library/
├── README.md                          (this file)
├── prompt_use_cases.md                (detailed use case guide)
├── prompt_examples.md                 (tested real-world examples)
└── prompts/                           (19 prompt templates)
    ├── refactoring.md
    ├── unit_test_generation.md
    ├── code_review_checklist.md
    ├── performance_optimization.md
    ├── design_patterns.md
    ├── api_documentation.md
    ├── readme_writing.md
    ├── vulnerability_detection.md
    ├── data_privacy_audit.md
    ├── bug_identification.md
    ├── error_analysis.md
    ├── code_comments.md
    ├── style_enforcement.md
    ├── dead_code_removal.md
    ├── test_case_design.md
    ├── regression_testing.md
    ├── interface_design.md
    ├── dependency_analysis.md
    └── prompt_examples.md
```

---

## Additional Resources

- **[Prompt Use Cases](./prompt_use_cases.md)** - Detailed guidance on when and how to use each template
- **[Prompt Examples](./prompt_examples.md)** - Real-world testing with AI outputs and feedback
- **Individual template files** - Each template includes role definition, task description, input placeholders, and expected output format

---

## Contributing

To suggest improvements or add new templates:
1. Review existing templates for consistency in structure
2. Follow the established template format (Role, Task, Input Placeholder, Expected Output)
3. Test templates with real code before submitting
4. Document examples and use cases

---

## License & Usage

These prompt templates are designed for development teams to improve their AI-assisted workflows. Feel free to:
- ✅ Use in your projects
- ✅ Customize for your tech stack
- ✅ Share with your team
- ✅ Extend with new templates

---

**Last Updated**: March 2026

For questions or feedback, refer to [prompt_examples.md](./prompt_examples.md) to understand how each template performs with real inputs and outputs.
