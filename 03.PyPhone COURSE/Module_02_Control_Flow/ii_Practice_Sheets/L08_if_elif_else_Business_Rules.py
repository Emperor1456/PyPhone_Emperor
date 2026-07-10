import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks (2) ──────────────────────────

easy1 = Task(
    description=(
        "📦  Stock Availability – Check Inventory\n\n"
        "You are a warehouse clerk. Check if a product is in stock.\n"
        "Given:\n"
        "  stock = 12\n\n"
        "If stock is greater than 0, print 'Available'.\n"
        "Otherwise, print 'Out of stock'.\n\n"
        "Expected output: Available"
    ),
    expected_output="Available",
    level=Level.EASY,
    hints=[
        "stock = 12",
        "if stock > 0:",
        "    print('Available')",
        "else:",
        "    print('Out of stock')"
    ]
)

easy2 = Task(
    description=(
        "🌡️  Temperature Alert – Hot or Not\n\n"
        "A sensor reports the current temperature.\n"
        "Given:\n"
        "  temp = 28\n\n"
        "If temp > 30, print 'Hot day'.\n"
        "Else, print 'Not too hot'.\n\n"
        "Expected output: Not too hot"
    ),
    expected_output="Not too hot",
    level=Level.EASY,
    hints=[
        "temp = 28",
        "if temp > 30: print('Hot day')",
        "else: print('Not too hot')"
    ]
)

# ── Medium Tasks (2) ──────────────────────

medium1 = Task(
    description=(
        "💰  Tax Bracket – Income‑Based Tax Rate\n\n"
        "The Imperial Revenue Service taxes citizens by income.\n"
        "Given:\n"
        "  income = 25000\n\n"
        "Apply these rules and print the tax rate:\n"
        "  • income >= 50000 → 'High tax'\n"
        "  • income >= 20000 → 'Medium tax'\n"
        "  • otherwise → 'Low tax'\n\n"
        "Expected output: Medium tax"
    ),
    expected_output="Medium tax",
    level=Level.MEDIUM,
    hints=[
        "income = 25000",
        "if income >= 50000: print('High tax')",
        "elif income >= 20000: print('Medium tax')",
        "else: print('Low tax')"
    ]
)

medium2 = Task(
    description=(
        "🚚  Shipping Cost – By Weight\n\n"
        "The Imperial Post charges by weight.\n"
        "Given:\n"
        "  weight_kg = 12\n\n"
        "Print the shipping category:\n"
        "  • weight > 20 → 'Heavy shipment'\n"
        "  • weight > 10 → 'Standard shipment'\n"
        "  • weight > 5  → 'Light shipment'\n"
        "  • otherwise → 'Envelope'\n\n"
        "Expected output: Standard shipment"
    ),
    expected_output="Standard shipment",
    level=Level.MEDIUM,
    hints=[
        "weight_kg = 12",
        "if weight_kg > 20: print('Heavy shipment')",
        "elif weight_kg > 10: print('Standard shipment')",
        "elif weight_kg > 5: print('Light shipment')",
        "else: print('Envelope')"
    ]
)

# ── Hard Tasks (2) ────────────────────────

hard1 = Task(
    description=(
        "🎖️  Loan Qualification – Multiple Conditions\n\n"
        "A bank approves a loan if the applicant meets ALL conditions:\n"
        "  • age >= 21\n"
        "  • income >= 30000\n"
        "  • existing_loans == 0\n\n"
        "Given:\n"
        "  age = 25\n"
        "  income = 32000\n"
        "  existing_loans = 0\n\n"
        "Print 'Approved' if all are true, else 'Denied'.\n\n"
        "Expected output: Approved"
    ),
    expected_output="Approved",
    level=Level.HARD,
    hints=[
        "age = 25",
        "income = 32000",
        "existing_loans = 0",
        "if age >= 21 and income >= 30000 and existing_loans == 0:",
        "    print('Approved')",
        "else:",
        "    print('Denied')"
    ]
)

hard2 = Task(
    description=(
        "🧊  Cold Storage – Temperature & Humidity Check\n\n"
        "A warehouse stores sensitive goods. It is safe only if\n"
        "temperature is between 2 and 8 degrees (inclusive)\n"
        "AND humidity is below 60%.\n\n"
        "Given:\n"
        "  temp = 5\n"
        "  humidity = 55\n\n"
        "Print 'Safe' if conditions are met, else 'Unsafe'.\n\n"
        "Expected output: Safe"
    ),
    expected_output="Safe",
    level=Level.HARD,
    hints=[
        "temp = 5; humidity = 55",
        "if 2 <= temp <= 8 and humidity < 60:",
        "    print('Safe')",
        "else:",
        "    print('Unsafe')"
    ]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L08.json")
