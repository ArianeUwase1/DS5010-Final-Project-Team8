#!/usr/bin/env python
# coding: utf-8

# In[12]:

import datetime
import pandas as pd
import matplotlib.pyplot as plt

class Income:
    def __init__(self, amount, date, category):
        self.amount = amount
        self.date = date
        self.category = category

class Expense:
    def __init__(self, amount, date, category, budget=None):
        self.amount = amount
        self.date = date
        self.category = category
        self.budget = budget

class BudgetTracker:
    def __init__(self):
        self.incomes = []
        self.expenses = []
        self.categories = {}
        self.goals = []
        self.budgets = {}
        self.bill_reminders = []

    def add_income(self, amount, date, category):
        income = Income(amount, date, category)
        self.incomes.append(income)
        self.categories.setdefault(category, []).append(income)

    def add_expense(self, amount, date, category):
        expense = Expense(amount, date, category, self.budgets.get(category))
        self.expenses.append(expense)
        self.categories.setdefault(category, []).append(expense)

        if expense.budget is not None and expense.amount > expense.budget:
            print(f"Alert: You have exceeded your budget of {expense.budget} for {expense.category} expenses.")

    def set_budget(self, category, budget):
        self.budgets[category] = budget

    def track_budget(self):
        for category, transactions in self.categories.items():
            expenses = [t.amount for t in transactions if isinstance(t, Expense)]
            total_expenses = sum(expenses)
            budget = self.budgets.get(category)
            if budget is not None and total_expenses > budget:
                print(f"Alert: You have exceeded your budgetof {budget} for {category} expenses.")
                
    def plot_expense_categories(self):
        expenses_df = pd.DataFrame([{'category': t.category, 'amount': t.amount} for t in self.expenses])
        expenses_df = expenses_df.groupby('category').sum().reset_index()
        expenses_df.plot(kind='bar', x='category', y='amount', title='Total expenses by category')
        plt.show()

    def plot_income_vs_expenses(self):
        incomes_df = pd.DataFrame([{'date': t.date, 'amount': t.amount} for t in self.incomes])
        incomes_df = incomes_df.groupby('date').sum().reset_index()
        expenses_df = pd.DataFrame([{'date': t.date, 'amount': t.amount} for t in self.expenses])
        expenses_df = expenses_df.groupby('date').sum().reset_index()
        df = pd.merge(incomes_df, expenses_df, on='date', how='outer').fillna(0)
        df.plot(kind='line', x='date', y=['amount_x', 'amount_y'])
        plt.legend(['Income', 'Expenses'])
        plt.show()

class Budget:
    def __init__(self, name):
        self.name = name
        self.transactions = []
        self.investments = []
        self.currencies = set()
        
    def add_transaction(self, date, type, amount, currency):
        self.transactions.append({'date': date, 'type': type, 'amount': amount, 'currency': currency})
        self.currencies.add(currency)
        
    
    def add_investment(self, symbol, name, quantity, purchase_price, current_price):
        self.investments.append({'symbol': symbol, 'name': name, 'quantity': quantity, 
                                 'purchase_price': purchase_price, 'current_price': current_price})
        
    def get_transactions_by_type(self, type):
        return [t for t in self.transactions if t['type'] == type]
    
    def get_transactions_by_currency(self, currency):
        return [t for t in self.transactions if t['currency'] == currency]
    
    def generate_tax_report(self):
        income = 0
        expenses = 0

        for transaction in self.transactions:
            if transaction['type'] == 'income':
                income += transaction['amount']
            elif transaction['type'] == 'expense':
                expenses += transaction['amount']

        net_income = income - expenses

        print("Income: $", income)
        print("Expenses: $", expenses)
        print("Net Income: $", net_income)

        if net_income < 0:
            print("You had a loss this year. Consider consulting a tax professional to see if you are eligible for any deductions or credits.")
        else:
            print("Congratulations on your positive net income! Consider consulting a tax professional to see if you are eligible for any deductions or credits.")

    def generate_investment_report(self):
        total_investment_value = 0
        total_current_value = 0

        for investment in self.investments:
            investment_value = investment['quantity'] * investment['purchase_price']
            current_value = investment['quantity'] * investment['current_price']

            total_investment_value += investment_value
            total_current_value += current_value

            print(investment['name'], '(', investment['symbol'], ')')
            print('Investment value: $', investment_value)
            print('Current value: $', current_value)
            print('Gain/loss: $', current_value - investment_value)

        overall_gain_loss = total_current_value - total_investment_value

        print('\nTotal investment value: $', total_investment_value)
        print('Total current value: $', total_current_value)
        print('Overall gain/loss: $', overall_gain_loss)
        
    def get_available_currencies(self):
        return self.currencies


def add_transaction(transactions, date, type, amount, currency='USD'):
    """Add a new transaction to the list of transactions."""
    transactions.append({'date': date, 'type': type, 'amount': amount, 'currency': currency})
    print("Transaction added successfully.")
    return transactions

def get_transaction_by_date(transactions, date):
    """Get a list of transactions that match the specified date."""
    matched_transactions = []
    for transaction in transactions:
        if transaction['date'] == date:
            matched_transactions.append(transaction)
    return matched_transactions

def convert_currency(amount, from_currency, to_currency):
    """Convert an amount from one currency to another."""
    # TODO: Implement currency conversion logic
    return amount

def generate_tax_report(transactions):
    """Generate a tax report based on the given transactions."""
    income = 0
    expenses = 0
    for transaction in transactions:
        if transaction['type'] == 'income':
            income += transaction['amount']
        elif transaction['type'] == 'expense':
            expenses += transaction['amount']
    net_income = income - expenses
    print("Income: $", income)
    print("Expenses: $", expenses)
    print("Net Income: $", net_income)
    if net_income < 0:
        print("You had a loss this year. Consider consulting a tax professional to see if you are eligible for any deductions or credits.")
    else:
        print("Congratulations on your positive net income! Consider consulting a tax professional to see if you are eligible for any deductions or credits.")


class FinancialGoal:
    def __init__(self, name, target_amount, current_amount=0):
        self.name = name
        self.target_amount = target_amount
        self.current_amount = current_amount
        
    def add_contribution(self, amount):
        self.current_amount += amount
        
    def progress_percentage(self):
        return round(self.current_amount / self.target_amount * 100, 2)
        
    def is_completed(self):
        return self.current_amount >= self.target_amount
        
class FinancialGoalTracker:
    def __init__(self):  # Fix: Use double underscores for the __init__ method
        self.goals = []
        
    def add_goal(self, goal):
        self.goals.append(goal)
        
    def get_goal(self, name):
        for goal in self.goals:
            if goal.name == name:
                return goal
        return None
        
    def make_contribution(self, name, amount):
        goal = self.get_goal(name)
        if goal is None:
            return False
        goal.add_contribution(amount)
        return True
        
    def get_progress_report(self):
        report = ''
        for goal in self.goals:
            progress = goal.progress_percentage()
            if goal.is_completed():
                report += f'{goal.name}: completed!\n'
            else:
                report += f'{goal.name}: {progress}% complete\n'
        return report
        
# Example usage
tracker = FinancialGoalTracker()

# Add a new goal
vacation_goal = FinancialGoal('Vacation', 5000)
tracker.add_goal(vacation_goal)

# Make some contributions towards the goal
tracker.make_contribution('Vacation', 1000)
tracker.make_contribution('Vacation', 2000)

# Get a progress report
report = tracker.get_progress_report()
print(report)

class Goal:
        def __init__(self, name, amount, start_date, end_date, goal_type):
            self.name = name
            self.amount = amount
            self.start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
            self.end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
            self.progress = 0
            self.goal_type = goal_type

        def update_progress(self, amount):
            self.progress += amount

        def add_goal(self, name, amount, start_date, end_date, goal_type):
            new_goal = BudgetTracker.Goal(name, amount, start_date, end_date, goal_type)
            self.goals.append(new_goal)
            print(f"New goal '{name}' added successfully!")

        def update_goal_progress(self, goal_name, amount):
            for goal in self.goals:
                if goal.name == goal_name:
                    goal.update_progress(amount)
                    print(f"Goal '{goal_name}' progress updated successfully!")
                    return
            print(f"No goal found with the name '{goal_name}'.")

        def generate_goal_report(self):
            total_needed = sum(goal.amount for goal in self.goals)
            total_progress = sum(goal.progress for goal in self.goals)
            print(f"Goal Progress Report")
            print(f"Total Goals: {len(self.goals)}")
            print(f"Total Amount Needed: {total_needed}")
            print(f"Total Amount Saved: {total_progress}")
            print(f"Total Amount Remaining: {total_needed - total_progress}")

        def visualize_data(self):
           for category, transactions in self.categories.items():
            df = pd.DataFrame([(t.amount, t.date) for t in transactions], columns=["Amount", "Date"])
            df = df.set_index("Date")
            ax = df.plot(kind ="bar", title=f"{category.capitalize()} Transactions", legend=False)
            ax.set_xlabel("Date")
            ax.set_ylabel("Amount")
            plt.show()

        def set_reminder(self, bill_name, bill_date):
         """
           This function sets a reminder for an upcoming bill or payment.

          Parameters:
          bill_name (str): The name or description of the bill.
          bill_date (str): The due date of the bill in the format "YYYY-MM-DD".

         Returns:
         None
         """
         reminder_date = datetime.datetime.strptime(bill_date, "%Y-%m-%d").date()
         reminder = (bill_name, reminder_date)

         if "reminders" not in self.categories:
          self.categories["reminders"] = []

         self.categories["reminders"].append(reminder)
         print(f"Reminder set for '{bill_name}' on {bill_date}.")

def check_reminders(self, today=None):
    """
    This function checks if there are any upcoming bills or payments and sends a reminder if there are.

    Parameters:
    today (datetime.date): The current date. Defaults to the current date if not specified.

    Returns:
    None
    """
    if today is None:
        today = datetime.date.today()

    reminders = [r for r in self.categories.get("reminders", []) if r[1] >= today]

    if not reminders:
        print("No reminders today.")
        return

    print("Upcoming reminders:")
    for reminder in reminders:
        print(f"- {reminder[0]} is due on {reminder[1]}")

def main(self):
    self.add_income(5000, "2022-03-15", "Salary")
    self.add_income(2000, "2022-03-20", "Bonus")
    self.add_expense(1500, "2022-03-17", "Food")
    self.add_expense(300, "2022-03-18", "Transportation")
    self.add_expense(200, "2022-03-20", "Food")
    self.set_budget("Food", 1000)
    self.track_budget()
    self.set_reminder("Electricity Bill", "2022-04-20")
    self.set_reminder("Credit Card Payment", "2022-04-25")
    self.check_reminders()
class Budget1:
    def __init__(self, income, expenses):
        self.income = income
        self.expenses = expenses
        self.balance = income - expenses
        self.goals = []

    def add_goal(self, name, target):
        goal = {"name": name, "target": target, "progress": 0}
        self.goals.append(goal)

    def update_goal_progress(self, goal_name, amount):
        for goal in self.goals:
            if goal["name"] == goal_name:
                goal["progress"] += amount
                if goal["progress"] > goal["target"]:
                    goal["progress"] = goal["target"]
                break

    def generate_report(self):
        print(f"Income: {self.income}")
        print(f"Expenses: {self.expenses}")
        print(f"Balance: {self.balance}")
        if self.goals:
            print("Goals:")
            for goal in self.goals:
                progress_percent = goal["progress"] / goal["target"] * 100
                print(f"{goal['name']}: {goal['progress']} / {goal['target']} ({progress_percent:.2f}%)")
        else:
            print("No goals set.")


    def generate_visualization(self):
        import matplotlib.pyplot as plt

        if self.goals:
            labels = [goal["name"] for goal in self.goals]
            sizes = [goal["progress"] for goal in self.goals]
            colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'orange']
            plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
            plt.axis('equal')
            plt.show()
        else:
            print("No goals set.")

budget = Budget1(8000, 3000)
budget.add_goal("Save for vacation", 2500)
budget.add_goal("Pay off debt", 3000)
budget.update_goal_progress("Save for vacation", 800)
budget.update_goal_progress("Pay off debt", 100)
budget.generate_report()
budget.generate_visualization()

tracker = BudgetTracker()
tracker.add_income(1000, '2023-04-01', 'Salary')
tracker.add_income(500, '2023-04-15', 'Bonus')
tracker.add_expense(100, '2023-04-05', 'Rent')
tracker.add_expense(50, '2023-04-08', 'Groceries')
tracker.add_expense(200, '2023-04-10', 'Entertainment')
tracker.set_budget('Rent', 150)
tracker.set_budget('Entertainment', 100)
tracker.track_budget()
tracker.plot_expense_categories()
tracker.plot_income_vs_expenses()

my_budget = Budget('Monthly Budget')
my_budget.add_transaction('2023-04-01', 'income', 1000, 'USD')
my_budget.add_transaction('2023-04-05', 'expense', 150, 'USD')
my_budget.add_transaction('2023-04-10', 'expense', 50, 'USD')
my_budget.add_investment('AAPL', 'Apple Inc.', 10, 200, 250)
my_budget.add_investment('MSFT', 'Microsoft Corporation', 5, 100, 120)
my_budget.generate_tax_report()
my_budget.generate_investment_report()

currencies = my_budget.get_available_currencies()
print('Available currencies:', currencies)

# In[ ]:




