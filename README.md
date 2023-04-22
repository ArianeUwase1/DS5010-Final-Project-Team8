# DS5010Final-Project

# README

## Introduction

This is a Python program that helps to track income, expenses and budget.

## How to Use

### Prerequisites

- Python 3.x
- pandas
- matplotlib

### Installation

To run the program, install the required packages by running the following command:

```python
pip install pandas matplotlib
```

### Usage

The program consists of several classes, which can be used to perform different tasks related to budget tracking. 

#### Income and Expense

The `Income` and `Expense` classes are used to represent income and expenses, respectively. The `Income` class has three attributes: `amount`, `date`, and `category`. The `Expense` class has four attributes: `amount`, `date`, `category`, and `budget`. 

#### BudgetTracker

The `BudgetTracker` class is used to track income, expenses, and budget. It has several methods:

** __init__(): Initializes empty lists for incomes, expenses, categories, goals, budgets, and bill reminders.
** add_income(amount, date, category): Adds an income to the incomes list and to its respective category in the categories dictionary.
** add_expense(amount, date, category): Adds an expense to the expenses list and to its respective category in the categories dictionary. If the expense exceeds the budget for its category (if one is set), it prints an alert.
** set_budget(category, budget): Sets the budget for a specific category.
** track_budget(): Checks whether expenses exceed their respective budgets and prints an alert if they do.
** plot_expense_categories(): Creates a bar plot of total expenses by category.
** plot_income_vs_expenses(): Creates a line plot of income and expenses over time.

#### Budget

The `Budget` class is used to track transactions and investments. It has several methods:

--__init__(name): Initializes empty lists for transactions, investments, and currencies, and sets the budget name.
** add_transaction(date, type, amount, currency): Adds a transaction to the transactions list and adds the currency to the currencies set.
** add_investment(symbol, name, quantity, purchase_price, current_price): Adds an investment to the investments list.
** get_transactions_by_type(type): Returns a list of transactions of a specific type.
** get_transactions_by_currency(currency): Returns a list of transactions in a specific currency.
** generate_tax_report(): Prints the total income, expenses, and net income, and provides a recommendation based on net income.
** generate_investment_report(): Prints the investment value, current value, and gain/loss for each investment, as well as the total investment value, current value, and overall gain/loss.
** get_available_currencies(): Returns a list of available currencies in the transactions.

## Example

Here is an example of how to use the `BudgetTracker` and `Budget` classes:

```python
from datetime import datetime
from budget_tracker import BudgetTracker, Budget

# Create a budget tracker
bt = BudgetTracker()

# Add income and expenses
bt.add_income(500, datetime(2022, 1, 1), 'salary')
bt.add_expense(50, datetime(2022, 1, 3), 'food')
bt.add_expense(100, datetime(2022, 1, 5), 'rent')

# Set budgets
bt.set_budget('food', 150)
bt.set_budget('rent', 500)

# Plot expenses by category
bt.plot_expense_categories()

# Plot income vs expenses
bt.plot_income_vs_expenses()

# Create a budget
b = Budget('My Budget')

# Add transactions and investments
b.add_transaction(datetime(2022, 1, 1), 'income', 500, 'USD')
b.add_transaction(datetime(2022, 1, 3), 'expense', 50, 'USD')
b.add_transaction(datetime(2022, 1, 5), 'expense', 100, 'USD')
b.add_investment('AAPL', 'Apple Inc.', 10, 150, 160)

# Generate reports
b.generate_tax_report()
b.generate_investment_report()

# Get available currencies
currencies = my_budget.get_available_currencies()
print('Available currencies:', currencies)
