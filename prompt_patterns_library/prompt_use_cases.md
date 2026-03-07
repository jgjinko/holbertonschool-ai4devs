# Prompt Use Cases

## Code Quality
- **Refactoring**
  - **Goal**: Improve readability and performance  
  - **Input**: Source function in [LANGUAGE]  
  - **Output**: Optimized code + explanation of changes  

- **Style Enforcement**
  - **Goal**: Enforce consistent naming and formatting  
  - **Input**: Code block with inconsistent style  
  - **Output**: Rewritten code with consistent conventions  

- **Dead Code Removal**
  - **Goal**: Identify and remove unused functions/variables  
  - **Input**: Full module or file  
  - **Output**: Cleaned code with list of removed items  


## Debugging
- **Bug Identification**
  - **Goal**: Identify logical errors and edge cases  
  - **Input**: Buggy source code + expected behavior  
  - **Output**: List of bugs, root causes, and affected code sections  

- **Error Analysis**
  - **Goal**: Explain error messages and suggest fixes  
  - **Input**: Error stack trace + relevant code  
  - **Output**: Error explanation + recommended fixes with code examples  

- **Performance Optimization**
  - **Goal**: Identify bottlenecks and optimize slow code  
  - **Input**: Function with performance issues + performance metrics  
  - **Output**: Optimized code + explanation of improvements  


## Documentation
- **Code Comments Generation**
  - **Goal**: Add clear, concise documentation to code  
  - **Input**: Undocumented source code  
  - **Output**: Code with inline comments and docstrings  

- **API Documentation**
  - **Goal**: Create comprehensive API reference docs  
  - **Input**: Function signatures, parameters, return types  
  - **Output**: Formatted API documentation with examples  

- **README Writing**
  - **Goal**: Generate project overview and setup instructions  
  - **Input**: Project structure, dependencies, key features  
  - **Output**: Well-organized README with setup, usage, and contribution guidelines  


## Testing
- **Unit Test Generation**
  - **Goal**: Create comprehensive unit tests for functions  
  - **Input**: Function implementation + specification  
  - **Output**: Test suite covering normal cases, edge cases, and error conditions  

- **Test Case Design**
  - **Goal**: Define test scenarios for feature validation  
  - **Input**: Feature specification or user story  
  - **Output**: Structured test cases with input, expected output, and test steps  

- **Regression Test Planning**
  - **Goal**: Identify and document potential breaking changes  
  - **Input**: New feature or refactor description + existing implementation  
  - **Output**: List of regression risks + recommended test coverage  


## Architecture & Design
- **Design Pattern Application**
  - **Goal**: Suggest appropriate design patterns for code structure  
  - **Input**: Problem description or existing code structure  
  - **Output**: Recommended design pattern with implementation example  

- **System Interface Design**
  - **Goal**: Define clear, scalable interfaces between components  
  - **Input**: System requirements and component descriptions  
  - **Output**: Interface specifications with methods, parameters, and contracts  

- **Dependency Analysis**
  - **Goal**: Identify and resolve circular dependencies  
  - **Input**: Module/class structure and dependency graph  
  - **Output**: Dependency diagram + refactoring recommendations  


## Security & Compliance
- **Security Vulnerability Detection**
  - **Goal**: Identify common security issues in code  
  - **Input**: Source code (authentication, data handling, etc.)  
  - **Output**: List of vulnerabilities with severity + remediation steps  

- **Code Review Checklist**
  - **Goal**: Generate context-specific code review guidelines  
  - **Input**: Project type, tech stack, compliance requirements  
  - **Output**: Custom code review checklist for team use  

- **Data Privacy Audit**
  - **Goal**: Identify data handling risks and compliance gaps  
  - **Input**: Code handling sensitive data + compliance requirements (GDPR, HIPAA, etc.)  
  - **Output**: Risk assessment + privacy improvement recommendations  
