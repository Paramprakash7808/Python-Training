# Employee Management System

A simple Python console application for managing employee records.

The project allows users to add, remove, update, find, list, and search employees. Employee data is stored in a JSON file so that the data is available even after the program is closed.

## Features

* Add a new employee
* Remove an employee
* Update employee details
* Find an employee by ID
* List all employees
* Search employees by name
* Validate employee data
* Save employee data in JSON
* Load employee data when the application starts
* Handle invalid JSON and file errors
* Log application activities and errors
* Unit testing
* Employee data analysis

## Project Structure

Employee Management System/
│
├── src/
│   ├── employee_management/
│   │   ├── __init__.py
│   │   ├── employee.py
│   │   ├── validation.py
│   │   └── main.py
│   │
│   └── employee_analyzer/
│       ├── __init__.py
│       ├── analyzer.py
│       ├── validation.py
│       └── main.py
│
├── tests/
│   ├── test_employee.py
│   ├── test_validation.py
│   └── test_analyzer.py
│
├── docs/
│   └── ...
│
├── employees.json
├── logs/
│   └── application.log
├── requirements.txt
├── .gitignore
└── README.md

## Technologies Used

* Python 3.13.11
* JSON
* unittest
* Logging
* Git

## How to Run

### 1. Clone the repository
git clone <repository-url>cd "Employee Management System"

### 2. Create a virtual environment
python -m venv taskenv

### 3. Activate the virtual environment
For Windows PowerShell:
powershell
.\taskenv\Scripts\Activate

### 4. Install dependencies
pip install -r requirements.txt

### 5. Run the Employee Management System
python -m src.employee_management.main

### 6. Run the Employee Analyzer
python -m src.employee_analyzer.main

## Employee Data
Employee records are stored in `employees.json`.
Each employee contains:

json
{
    "id": 101,
    "name": "Rahul"
}

The application checks that:
* Employee ID is an integer
* Employee ID is greater than 0
* Employee name is a string
* Employee name cannot be empty

## Logging
Application logs are stored in:
logs/application.log

The application records important events such as:

* Employee added
* Employee removed
* Employee updated
* Employee searched
* Invalid input
* File errors
* Application errors

## Testing
Run all tests using:
python -m unittest discover -s tests -p "test_*.py" -v

To run a specific test file:
python -m unittest tests.test_analyzer -v

## Employee Analyzer
The Employee Analyzer works with employee data and provides functions such as:

* Department analysis
* Highest salary
* Lowest salary
* Average salary
* Department filtering
* Location filtering
* Experience analysis
* Duplicate employee detection
* Invalid record detection
* Sorting
* Employee search

## Documentation
Project research and development documentation is available in the `docs/` folder.

The documentation covers:
* Problem understanding
* Assumptions
* Data structure
* Program flow
* Validation rules
* Edge cases
* Function responsibilities
* Clean code
* Refactoring decisions
* Testing approach

## Main Goal
The main goal of this project is to build a simple and readable Python application while practicing:

* Python functions
* Validation
* CRUD operations
* File handling
* JSON
* Exception handling
* Logging
* Unit testing
* Code organization
* Clean code principles
* Git and project documentation