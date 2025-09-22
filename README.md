# Interactive Calculator (Command-Line Application)

A simple interactive command-line calculator written in Python.  
Supports basic arithmetic operations and includes full test coverage with automated GitHub Actions CI.

---

##  Features

- REPL interface (keeps running until you type `quit`)
- Supported operations:
  - Addition
  - Subtraction
  - Multiplication
  - Division (with zero division protection)
- Input validation & error handling
- 100% test coverage using `pytest`
- GitHub Actions CI for automatic test enforcement

---

##  Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Mikev2002/interactive_calculator.git
   cd interactive_calculator

Create and activate virtual environment

Windows:
py -m venv venv
.\venv\Scripts\activate

Use this command to temporarily allow scripts for just this terminal session:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

Then try activating the environment again:
.\venv\Scripts\activate


Install dependencies:
pip install -r requirements.txt


How to Run the Calculator: 
Make sure you're in the project folder and the virtual environment is activated.
python main.py

You’ll see:

Welcome to the CLI Calculator!
Available operations: add, subtract, multiply, divide, quit

To run all tests:
pytest

To run tests with coverage report (required for GitHub Actions):
pytest --cov=calculator tests/
