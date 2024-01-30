class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount

    def view_expenses(self):
        print("\nExpense Summary:")
        total_expense = 0
        for category, amount in self.expenses.items():
            print(f"{category}: ${amount}")
            total_expense += amount
        print(f"\nTotal Expense: ${total_expense}")

    def main_menu(self):
        while True:
            print("\nExpense Tracker Menu:")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Exit")

            choice = input("Enter your choice (1/2/3): ")

            if choice == "1":
                category = input("Enter expense category: ")
                amount = float(input("Enter expense amount: "))
                self.add_expense(category, amount)
                print("Expense added successfully!")

            elif choice == "2":
                self.view_expenses()

            elif choice == "3":
                print("Exiting Expense Tracker. Thankyou!")
                break

            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.main_menu()
