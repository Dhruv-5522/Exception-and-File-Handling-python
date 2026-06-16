# Project: File Operator (Personal Journal Manager)

## Project Overview
This is a menu-driven Python application designed to maintain a personal journal. The application uses object-oriented programming (OOP) principles, text file handling to store entries, and exception handling to manage potential errors gracefully without crashing.

---

## Features
1. **Add a New Entry:** Appends a new journal text with an automatic timestamp (`YYYY-MM-DD HH:MM:SS`) to `journal.txt`.
2. **View All Entries:** Reads and displays all saved entries. Handles cases where the file doesn't exist yet.
3. **Search for an Entry:** Allows users to find specific entries using keywords or dates.
4. **Delete All Entries:** Permanently deletes the `journal.txt` file after asking for user confirmation.
5. **Exit:** Safely closes the application.

---

## Technical Specifications & Learning Objectives
* **Language:** Python 3
* **OOP Architecture:** Code is encapsulated within the `JournalManager` class using instance methods.
* **File Handling Modes Used:** * `a` (Append) for adding entries without overwriting existing data.
  * `r` (Read) for viewing and searching entries.
* **Exception Handling:** Built-in safeguards for `FileNotFoundError`, `PermissionError`, and invalid user menu choices.

---

## Project Structure
```text
├── journal.py       # Main application source code
├── journal.txt      # Text file where entries are stored (auto-generated)
└── README.md        # Project documentation
