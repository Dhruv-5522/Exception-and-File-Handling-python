# Lab Work #6.2:

Exception Handling in Python

Welcome to this repository! This project contains a structured collection of Python programs focused on robust error handling, input validation using assertion checks, and designing custom exceptions according to real-world edge cases.

This folder contains a collection of Python programs designed to practice and implement core error-handling mechanisms using `try...except`, `else`, and `finally` blocks. The objective is to write clean, resilient, and crash-free scripts.

## Table of Contents
* [Q1: Division by Zero Handler]
* [Q2: List Index Validation]
* [Q3: Safe File Reader]
* [Q4: String Index Access]
* [Q5: Safe Resource Cleanup]
* [Q6: Robust Division Program]
* [Q7: Square Root Calculator]

---

### Q1: Division by Zero Handler
* **Objective:** Develop a program that divides two numbers provided by the user.
* **Logic:** Employs a `try...except ZeroDivisionError` block to catch and handle cases where the denominator is entered as zero.

### Q2: List Index Validation
* **Objective:** Safely access an element in a list at a non-existent index position.
* **Logic:** Catches an `IndexError` gracefully to prevent script termination when looking up data outside boundaries.

### Q3: Safe File Reader
* **Objective:** Take a filename input from the user, read its contents, and handle file-related issues.
* **Logic:** Manages `FileNotFoundError`. Incorporates an `else` block to print the contents only when the file is read successfully.

### Q4: String Index Access
* **Objective:** Access elements inside a string sequence at a specific index.
* **Logic:** Catches any potential `IndexError`, and uses the `else` block to show the character if the index is valid.

### Q5: Safe Resource Cleanup
* **Objective:** Open a file system object and guarantee its closure.
* **Logic:** Handles exceptions if the file does not exist, and enforces file closure (`.close()`) inside a `finally` block to prevent memory leaks.

### Q6: Robust Division Program
* **Objective:** A standard division script with input format checks.
* **Logic:** Catches both `ValueError` (for non-numeric text input) and `ZeroDivisionError`. Features a `finally` block to show a closing execution message regardless of the result.

### Q7: Square Root Calculator
* **Objective:** Prompts the user for a number to find its square root value.

=============================================================================================================================

Lab Work 6.3

# Python Exception Handling & Assertions Lab

## 🚀 Lab Assignments Overview

Here is a quick summary of the problems implemented in this repository:

| Sr. No. | Question Objective | Exception / Error Handling Used |
| :---: | :--- | :--- |
| **Q.1** | Negative Number Prevention | `ValueError` |
| **Q.2** | Even/Odd & Data Type Validator | `TypeError` & `ValueError` |
| **Q.3** | Age Limit Verification (> 18) | `AssertionError` |
| **Q.4** | Empty String & Palindrome Checker | `AssertionError` |
| **Q.5** | Banking System Withdrawal Simulation | Custom `InsufficientBalanceError` |
| **Q.6** | Email Format Rules (`@`, `.com`, `.org`) | Custom `InvalidEmailError` |
| **Q.7** | Student Grade Compliance System | `ValueError`, `AssertionError` & Custom `InvalidGradeError` |
| **Q.8** | Temperature Scale Bounds Verification | `TypeError`, `AssertionError` & Custom `HighTemperatureError` |

---

## 🛠️ Detailed Logic Breakdown

### Q.1: Negative Number Guard
* Prevents execution if a user types a negative number.
* Throws a clear `ValueError` with a custom descriptive message.

### Q.2: Data Type & Even Check (`check_even`)
* Double-layer protection: Raises a `TypeError` if the input is not a whole number (integer), and a `ValueError` if the number is odd.

### Q.3: Age Gate Validator
* Uses Python's `assert` statement inline to verify if the age is greater than 18, showing a custom `AssertionError` text on failure.

### Q.4: Palindrome Input Assurer
* Ensures the user doesn't pass an empty string before applying the palindrome reversing algorithm by utilizing programmatic assertion.

### Q.5: Bank Account Withdrawal Simulation
* Implements a custom structural class `InsufficientBalanceError`. Raises this exception whenever the withdrawal requested exceeds the existing account balance.

### Q.6: Structural Email Validator
* Implements a custom `InvalidEmailError` exception that checks basic syntax: strings must contain `@` and must end strictly with `.com` or `.org`.

### Q.7: Academic Grade Rule System
* Multiple validations in one block: Asserts input existence, checks realistic bounds (0 to 100) using `ValueError`, and triggers a custom `InvalidGradeError` if the student scores below 40.

### Q.8: Advanced Temperature Converter
* Handles physical bounds check: Raises `TypeError` for non-numeric values, asserts hard absolute ranges (-273°C to 10,000°C), and raises a custom `HighTemperatureError` for anything above 1,000°C to flag unrealistic parameters.

   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
* **Logic:** Uses `try...except` to catch invalid values (negative numbers), an `else` block to print the successful calculation, and a `finally` block to output "Execution complete."
