
from collections import defaultdict


def calculate_total(expenses):
    return sum(expense["amount"] for expense in expenses)


def calculate_average(expenses):
    if not expenses:
        return 0
    return calculate_total(expenses) / len(expenses)


def calculate_category_totals(expenses):
    categories = defaultdict(float)

    for expense in expenses:
        categories[expense["category"]] += expense["amount"]

    return dict(categories)


def get_largest_expense(expenses):
    if not expenses:
        return None
    return max(expenses, key=lambda expense: expense["amount"])


def analyze_expenses(expenses):
    if not expenses:
        return {
            "total": 0,
            "count": 0,
            "average": 0,
            "categories": {},
            "highest_category": None,
            "largest_expense": None,
        }

    total = calculate_total(expenses)
    categories = calculate_category_totals(expenses)

    return {
        "total": total,
        "count": len(expenses),
        "average": calculate_average(expenses),
        "categories": categories,
        "highest_category": max(categories, key=categories.get),
        "largest_expense": get_largest_expense(expenses),
    }
