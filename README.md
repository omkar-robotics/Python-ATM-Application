# 🏦 Python ATM Application

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Application](https://img.shields.io/badge/Project-ATM-green)
![Exception Handling](https://img.shields.io/badge/Exception-Custom-orange)
![Modules](https://img.shields.io/badge/Code-Modular-red)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

🚀 **A menu-driven ATM simulation developed using Python, demonstrating basic banking operations, modular programming, input validation, and custom exception handling.**

This project focuses on implementing the fundamental operations of an Automated Teller Machine (ATM) using Python. It demonstrates how to organize a program into multiple modules and handle invalid transactions using user-defined exceptions.

It serves as a foundational Python project for learning programming concepts before moving on to object-oriented programming, database integration, and application development.

---

# 📌 Project Overview

The Python ATM Application simulates basic ATM operations through a menu-driven interface.

Users can select different operations, including depositing money, withdrawing money, and checking their account balance.

The application uses separate Python modules to organize the menu, banking operations, exception classes, and main program logic.

Custom exceptions are implemented to handle invalid deposit amounts, invalid withdrawal amounts, and insufficient account balances.

**Note:** This is an educational simulation, not a real banking application. Account information is stored in memory and does not persist after the program exits.

---

# 🔑 Key Concepts Demonstrated

* Python functions
* Modular programming
* Importing user-defined modules
* Conditional statements
* Match-case statements
* Global variables
* User input and type conversion
* Exception handling
* User-defined exceptions
* Basic transaction logic

---

# 🛠️ Technologies Used

| Technology | Description |
|---|---|
| 🐍 **Python** | Programming language |
| 💻 **VS Code** | Code editor |
| ⚙️ **Git** | Version control |
| 🐙 **GitHub** | Source code hosting |
| 🛡️ **Exception Handling** | Handling invalid transactions |
| 📦 **Python Modules** | Organizing application components |

---

# ⚙️ Application Workflow

The application follows these steps:

1️⃣ Display the ATM menu.

2️⃣ Accept the user's operation choice.

3️⃣ Execute the selected banking operation.

4️⃣ Validate the entered transaction amount.

5️⃣ Raise custom exceptions when transaction rules are violated.

6️⃣ Display the transaction result and updated balance.

7️⃣ Allow the user to perform another operation or exit the application.

---

# 💻 System Requirements

Before running this project, ensure the following software is installed:

* Python 3.10 or later recommended
* Visual Studio Code or another Python editor
* Git (optional, for version control)

**Note:** Python 3.10 or later supports the `match-case` statement used in this project.

---

# 📂 Project Structure

```text
Python-ATM-Application/
│
├── ATMMenu.py
├── ATMOperation.py
├── ATMExcept.py
├── ATMMainProg.py
├── README.md
└── .gitignore
```

### 📄 File Descriptions

| File | Description |
|---|---|
| `ATMMenu.py` | Displays the ATM menu and available operations |
| `ATMOperation.py` | Implements deposit, withdrawal, and balance enquiry |
| `ATMExcept.py` | Defines custom exception classes |
| `ATMMainProg.py` | Main program that controls application execution |
| `README.md` | Project documentation |
| `.gitignore` | Excludes unnecessary files from Git tracking |

---

# ✨ Features

## 1️⃣ Deposit Money

Allows the user to deposit money into the simulated account.

* Accepts a deposit amount.
* Rejects zero or negative amounts using a custom exception.
* Updates the account balance.
* Displays the deposited amount and updated balance.

## 2️⃣ Withdraw Money

Allows the user to withdraw money from the simulated account.

* Accepts a withdrawal amount.
* Rejects zero or negative amounts.
* Checks whether sufficient funds are available.
* Updates the account balance after a successful withdrawal.
* Displays the withdrawal amount and remaining balance.

## 3️⃣ Balance Enquiry

Allows the user to check the current account balance.

* Displays the available balance.
* Reflects successful deposits and withdrawals during the current session.

## 4️⃣ Custom Exception Handling

The application defines custom exceptions to handle transaction errors.

```python
class depositeError(Exception):
    pass

class withdrawError(Exception):
    pass

class inSuffFundError(Exception):
    pass
```

These exceptions help separate transaction validation from error-handling logic.

## 5️⃣ Menu-Driven Interface

The application provides four options:

```text
**************************************************
        ATM or Fund Transfer Application
**************************************************
        1. Deposit
        2. Withdraw
        3. Balance Enquiry
        4. Exit
**************************************************
```

The user can select an operation and interact with the application through the terminal.

---

# ▶️ Run the Project

## Step 1: Clone the Repository

Open your terminal and execute:

```bash
git clone https://github.com/omkar-robotics/Python-ATM-Application.git
```

## Step 2: Navigate to the Project Directory

```bash
cd Python-ATM-Application
```

## Step 3: Run the Application

```bash
python ATMMainProg.py
```

On systems where Python 3 is invoked using `python3`, use:

```bash
python3 ATMMainProg.py
```

The ATM menu will appear in the terminal.

---

# 🧪 Example Usage

The following example illustrates a typical interaction with the application.

### Initial Balance

The account starts with a balance of ₹500.

### Deposit Operation

```text
Enter your choice: 1
Enter your deposit amount: 1000

Your account credited with INR: 1000
Current balance: INR 1500
```

### Withdrawal Operation

```text
Enter your choice: 2
Enter your withdrawal amount: 200

Your account debited with INR: 200
Current balance after withdrawal: INR 1300
```

### Balance Enquiry

```text
Enter your choice: 3

Your account balance: INR 1300
```

**Note:** These examples illustrate the expected workflow. Actual output depends on the messages implemented in the Python source files.

---

# 🛡️ Exception Handling

The application demonstrates custom exception handling for invalid banking operations.

| Exception | Purpose |
|---|---|
| `depositeError` | Raised when the deposit amount is zero or negative |
| `withdrawError` | Raised when the withdrawal amount is zero or negative |
| `inSuffFundError` | Raised when the withdrawal amount exceeds the available balance |
| `ValueError` | Handles invalid numeric input, such as entering letters instead of numbers |

These mechanisms help the program handle common user input errors without immediately terminating during normal transaction processing.

---

# 📚 Learning Outcomes

Through this project, I practised:

* Writing reusable Python functions
* Organizing code into multiple modules
* Importing functions and custom exceptions
* Implementing conditional logic
* Using match-case statements
* Working with global variables
* Converting user input into numeric values
* Handling built-in and custom exceptions
* Implementing basic financial transaction logic
* Using Git and GitHub to manage source code

---

# 🚀 Future Improvements

Planned enhancements include:

* Add PIN authentication
* Store account information in a database
* Maintain transaction history
* Support multiple bank accounts
* Improve input validation
* Add object-oriented programming
* Implement a graphical user interface using Tkinter
* Generate transaction receipts
* Add automated unit tests
* Improve financial calculations using decimal arithmetic

---

# 👨‍💻 Author

**Omkar Maroti Honrao**

🎓 B.Tech Electrical Engineering Student

🤖 Robotics Research Intern

### Technical Interests

Python • ROS 2 • Robotics • Artificial Intelligence • Machine Learning • OpenCV • SLAM • Navigation2

🔗 **GitHub Profile:**  
https://github.com/omkar-robotics

🔗 **Project Repository:**  
https://github.com/omkar-robotics/Python-ATM-Application

---

# ⭐ Support

If you find this project helpful, consider giving the repository a ⭐ Star on GitHub.

Your support motivates me to continue learning Python and developing more projects in programming, robotics, and artificial intelligence.

---
