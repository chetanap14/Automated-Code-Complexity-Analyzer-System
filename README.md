# Automated Code Analyzer System

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Project](https://img.shields.io/badge/Project-Code%20Analyzer-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# Overview

The **Automated Code Analyzer System** is a tool designed to automatically analyze source code and detect potential issues such as bugs, inefficient code patterns, high complexity, and poor coding practices.

The goal of this system is to help developers improve **code quality, readability, and maintainability** by providing automated feedback and suggestions.

This project demonstrates the concept of **static code analysis** using Python.

---

# Problem Statement

Manual code review is time-consuming and developers may overlook hidden bugs or inefficient logic.

This project solves the problem by:

- Automatically scanning source code
- Detecting common coding mistakes
- Measuring code complexity
- Suggesting improvements
- Generating structured reports

---

# Key Features

### Static Code Analysis
Analyzes code without executing it.

### Bug Detection
Detects common issues such as:
- Unused variables
- Logical errors
- Infinite loops
- Poor variable naming

### Code Quality Check
Identifies:
- Bad coding practices
- Duplicate code
- Poor formatting

### Complexity Analysis
Measures complexity using:
- Cyclomatic complexity
- Nested loops
- Function length

### Automated Report Generation
Produces a report containing:
- Errors
- Warnings
- Suggestions

---

# Tech Stack

| Component | Technology |
|----------|-----------|
| Programming Language | Python |
| Code Parsing | Python AST |
| Backend Logic | Python |
| Version Control | Git |
| Repository | GitHub |

---

# System Architecture
+----------------------+
| User Input |
| (Source Code File) |
+----------+-----------+
|
v
+----------------------+
| Code Parser |
| (AST Parser) |
+----------+-----------+
|
v
+----------------------+
| Code Analyzer |
| - Bug Detection |
| - Complexity Check |
| - Style Analysis |
+----------+-----------+
|
v
+----------------------+
| Report Generator |
+----------+-----------+
|
v
+----------------------+
| Output Report |
| (Warnings/Suggestions)|
+----------------------+


---

# System Workflow

User uploads source code
|
v
Code is parsed using AST
|
v
Analyzer scans the code
|
v
Issues and complexity detected
|
v
Report is generated
|
v
Developer receives suggestions


---

# Project Structure


code-complexity-analyzer
│
├── analyzer.py
├── parser.py
├── complexity_checker.py
├── report_generator.py
│
├── sample_code
│ └── test_file.py
│
├── requirements.txt
└── README.md


---

<img width="1902" height="730" alt="Screenshot 2026-03-10 104919" src="https://github.com/user-attachments/assets/1e5621fc-b808-4743-9378-b21dbb3c3c62" />

Screenshot 1 – Code input


<img width="1919" height="792" alt="Screenshot 2026-03-10 110919" src="https://github.com/user-attachments/assets/e07928ea-e931-46ff-9b5f-7910898bd679" />

Screenshot 2 - Analysis result


<img width="1903" height="1010" alt="Screenshot 2026-03-10 103222" src="https://github.com/user-attachments/assets/413e8762-005e-4040-9e01-442f9e70957c" />

Screenshot 3 – Generated report










