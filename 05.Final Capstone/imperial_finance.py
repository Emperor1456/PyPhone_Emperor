#!/usr/bin/env python3
"""
Imperial Finance – PyPhone Emperor Capstone
============================================
A complete personal finance tracker built with Python on Android.
Integrates all 8 course modules.

Usage:
    python imperial_finance.py
"""

import json
import os
import csv
from datetime import datetime

DATA_FILE = "finance_data.json"

# -------------------------------
# 1. Domain Classes (Module 07 OOP)
# -------------------------------
class Transaction:
    """Represents a single income or expense."""
    def __init__(self, amount, category, date=None, note=""):
        self.amount = float(amount)
        self.category = category
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")
        self.note = note

    def to_dict(self):
        return {"amount": self.amount, "category": self.category, "date": self.date, "note": self.note}

    @classmethod
    def from_dict(cls, d):
        return cls(d["amount"], d["category"], d.get("date"), d.get("note", ""))

class Budget:
    """Monthly budget for a category."""
    def __init__(self, category, limit):
        self.category = category
        self.limit = float(limit)

    def to_dict(self):
        return {"category": self.category, "limit": self.limit}

    @classmethod
    def from_dict(cls, d):
        return cls(d["category"], d["limit"])

# -------------------------------
# 2. Decorator (Module 08)
# -------------------------------
def log_activity(func):
    """Decorator that prints when a method is called."""
    def wrapper(*args, **kwargs):
        print(f"⚡ Action: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# -------------------------------
# 3. Main Manager Class
# -------------------------------
class FinanceManager:
    def __init__(self):
        self.transactions = []
        self.budgets = []
        self.load_data()

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                self.transactions = [Transaction.from_dict(t) for t in data.get("transactions", [])]
                self.budgets = [Budget.from_dict(b) for b in data.get("budgets", [])]

    def save_data(self):
        with open(DATA_FILE, "w") as f:
            json.dump({
                "transactions": [t.to_dict() for t in self.transactions],
                "budgets": [b.to_dict() for b in self.budgets]
            }, f, indent=2)

    @log_activity
    def add_transaction(self, amount, category, date=None, note=""):
        # TODO: validate amount (Module 01 arithmetic, Module 06 exceptions)
        pass

    @log_activity
    def view_transactions(self, category=None, start_date=None, end_date=None):
        # TODO: filter using list comprehensions (Module 03) and conditionals (Module 02)
        pass

    @log_activity
    def set_budget(self, category, limit):
        pass

    @log_activity
    def budget_status(self):
        pass

    @log_activity
    def monthly_report(self, year, month):
        pass

    @log_activity
    def export_csv(self, filename):
        pass

# -------------------------------
# 4. Menu (Module 02 loops & input)
# -------------------------------
def main():
    fm = FinanceManager()
    while True:
        print("\n===== IMPERIAL FINANCE =====")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Set Budget")
        print("4. Budget Status")
        print("5. Monthly Report")
        print("6. Export to CSV")
        print("0. Exit")
        choice = input("> ").strip()
        if choice == "0":
            fm.save_data()
            print("Data saved. Goodbye, Emperor.")
            break
        elif choice == "1":
            # TODO: call add_transaction with user input (Module 03 input/type conversion, Module 06 error handling)
            pass
        elif choice == "2":
            # TODO: call view_transactions
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
