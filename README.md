# Smart Expense Analyzer

A modular Python command-line application that tracks personal expenses and generates a spending analysis report.

## Features

- Enter expenses interactively
- Calculate total and average spending
- Count expense transactions
- Group expenses by category
- Calculate category-wise spending percentages
- Identify the highest-spending category
- Find the largest individual transaction
- Validate input and handle invalid amounts
- Separate application logic from user interaction

## Technologies Used

- Python 3
- Lists and dictionaries
- Functions and modules
- `collections.defaultdict`
- Exception handling
- Lambda functions and sorting

## Project Structure

```text
python-smart-expense-analyzer/
├── main.py
├── analyzer.py
└── README.md
```

## How to Run

1. Install Python 3.
2. Open the project folder in VS Code.
3. Open a terminal in that folder.
4. Run:

```bash
python main.py
```

5. Enter a category and expense amount when prompted.
6. Type `done` to generate the final report.

## Example Data

| Category | Amount |
|---|---:|
| Food | 150 |
| Travel | 80 |
| Food | 120 |
| Shopping | 500 |

For this example, total spending is Rs. 850, average spending is Rs. 212.50, and Shopping is the highest-spending category.

## Code Architecture

- **main.py:** Handles user input, validates entries, and displays the report.
- **analyzer.py:** Calculates totals, averages, category breakdowns, and largest expenses.

This separation makes the application easier to maintain, test, and extend.

## Concepts Learned

- Importing functions from another Python module
- Processing lists of dictionaries
- Aggregating data by category
- Calculating percentages and averages
- Sorting dictionary entries
- Finding maximum values
- Handling invalid input with exceptions

## Future Improvements

- Save expenses to CSV
- Add dates and monthly summaries
- Create visual spending charts
- Set category-wise budgets
- Export reports

## Author

Ayushman Tiwari

GitHub: https://github.com/ayushman-ece