# 💰 Smart Expense Analyzer

**A modular Python application for tracking expenses, analyzing spending habits, and generating clear financial summaries directly from your terminal.**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-CLI-111827)
![Dependencies](https://img.shields.io/badge/Dependencies-Standard%20Library-16A34A)
![Status](https://img.shields.io/badge/Status-Completed-22C55E)

---

## 📌 Overview

Managing everyday expenses becomes easier when spending is organized and analyzed. **Smart Expense Analyzer** is a lightweight command-line application built with Python that collects expense records and transforms them into a useful spending report.

The project follows a modular architecture: expense calculations are handled separately from user interaction, making the code easier to maintain, understand, and extend.

## ✨ Features

- **Expense Tracking** — Enter expense categories and amounts interactively.
- **Total Spending** — Calculate the total amount spent.
- **Average Transaction** — Find the average expense per transaction.
- **Category Analysis** — Group expenses and calculate totals for each category.
- **Spending Percentages** — See what percentage of total spending belongs to each category.
- **Highest-Spending Category** — Identify the category with the greatest total expenditure.
- **Largest Transaction** — Find the single most expensive transaction.
- **Input Validation** — Handle empty categories, invalid numbers, and non-positive amounts.
- **Modular Design** — Keep business logic separate from the command-line interface.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| Lists & Dictionaries | Store expense records |
| Functions & Modules | Organize reusable logic |
| `collections.defaultdict` | Aggregate spending by category |
| Exception Handling | Handle invalid user input |
| Lambda Functions | Sort expenses and identify maximum values |

No third-party packages or API keys are required.

## 📁 Project Structure

```text
python-smart-expense-analyzer/
│
├── main.py       # User interaction and report display
├── analyzer.py   # Expense calculations and analysis
└── README.md     # Project documentation
```

### Architecture

- **`main.py`** collects expense details, validates input, calls the analyzer, and displays the final report.
- **`analyzer.py`** calculates totals, averages, category breakdowns, and the largest transaction.

This separation of responsibilities keeps the application organized and makes the analysis functions reusable.

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or newer
- A terminal or code editor such as Visual Studio Code

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/ayushman-ece/python-smart-expense-analyzer.git
```

**2. Navigate to the project directory**

```bash
cd python-smart-expense-analyzer
```

**3. Run the application**

```bash
python main.py
```

On some systems, you may need to use `python3 main.py` instead.

## 💻 Usage

Launch the program and enter an expense category followed by its amount. Repeat for each transaction, then type `done` to generate your report.

### Sample Input

```text
===== SMART EXPENSE ANALYZER =====
Enter your expenses. Type 'done' to finish.

Enter category: Food
Enter amount (Rs.): 150
Expense added successfully!

Enter category: Travel
Enter amount (Rs.): 80
Expense added successfully!

Enter category: Food
Enter amount (Rs.): 120
Expense added successfully!

Enter category: Shopping
Enter amount (Rs.): 500
Expense added successfully!

Enter category: done
```

### Example Report

For the sample expenses above, the application produces results like these:

```text
===================================
          EXPENSE REPORT
===================================
Total spending: Rs. 850.00
Transactions: 4
Average expense: Rs. 212.50

--- Category Breakdown ---
Shopping: Rs. 500.00 (58.8%)
Food: Rs. 270.00 (31.8%)
Travel: Rs. 80.00 (9.4%)

Highest-spending category: Shopping
Largest transaction: Shopping (Rs. 500.00)
===================================
```

*Example output is illustrative; actual results depend on the expenses entered.*

## 🧠 Key Concepts Demonstrated

- **Data Structures:** Represent and organize expense records using lists and dictionaries.
- **Aggregation:** Accumulate transaction amounts into category totals.
- **Functional Decomposition:** Break the application into focused, reusable functions.
- **Module Imports:** Import analysis functions into the main application.
- **Data Processing:** Calculate averages, percentages, and maximum values.
- **Input Validation:** Use exception handling to prevent invalid amounts from crashing the program.
- **Sorting:** Rank spending categories from highest to lowest.

## 🔮 Future Enhancements

- [ ] Save expenses permanently using CSV or JSON.
- [ ] Add transaction dates and monthly summaries.
- [ ] Set spending limits for individual categories.
- [ ] Generate charts using Matplotlib.
- [ ] Export expense reports to CSV.
- [ ] Add editing and deletion of existing transactions.
- [ ] Create a graphical user interface.

## 🎯 Learning Outcome

This project demonstrates how to build a clean, modular Python application that processes real-world data, validates user input, and generates meaningful summaries without relying on external services.

It is a practical step toward more advanced projects involving data analysis, file handling, visualization, and personal finance tools.

## 👨‍💻 Author

**Ayushman Tiwari**

GitHub: [@ayushman-ece](https://github.com/ayushman-ece)

---

*Built with Python to practise modular programming and data analysis.*
