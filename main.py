
from analyzer import analyze_expenses


def main():
    expenses = []

    print("=" * 35)
    print("       SMART EXPENSE ANALYZER")
    print("=" * 35)
    print("Enter your expenses. Type 'done' to finish.")

    while True:
        category = input("\nEnter category: ").strip()

        if category.lower() == "done":
            break

        if not category:
            print("Category cannot be empty.")
            continue

        try:
            amount = float(input("Enter amount (Rs.): "))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

        except ValueError:
            print("Invalid amount. Enter a number.")
            continue

        expenses.append({
            "category": category.title(),
            "amount": amount,
        })

        print("Expense added successfully!")

    report = analyze_expenses(expenses)

    if report["count"] == 0:
        print("\nNo expenses recorded.")
        return

    print("\n" + "=" * 35)
    print("          EXPENSE REPORT")
    print("=" * 35)
    print(f"Total spending: Rs. {report['total']:.2f}")
    print(f"Transactions: {report['count']}")
    print(f"Average expense: Rs. {report['average']:.2f}")

    print("\n--- Category Breakdown ---")
    for category, amount in sorted(
        report["categories"].items(),
        key=lambda item: item[1],
        reverse=True,
    ):
        percentage = amount / report["total"] * 100
        print(f"{category}: Rs. {amount:.2f} ({percentage:.1f}%)")

    largest = report["largest_expense"]

    print(f"\nHighest-spending category: {report['highest_category']}")
    print(
        f"Largest transaction: {largest['category']} "
        f"(Rs. {largest['amount']:.2f})"
    )
    print("=" * 35)


if __name__ == "__main__":
    main()
