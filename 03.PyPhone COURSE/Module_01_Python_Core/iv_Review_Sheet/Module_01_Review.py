import sys, os
sys.path.append("../..")          # reaches 03.PyPhone COURSE/
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy: Inventory Summary (variables, f‑string, arithmetic) ──
easy = Task(
    description=(
        "📦  Imperial Inventory Summary\n\n"
        "Create the following variables exactly:\n"
        "  • product = 'Keyboard'\n"
        "  • unit_price = 49.99\n"
        "  • stock = 23\n"
        "  • reorder = 10\n\n"
        "Then print a single line summary:\n"
        "  'Keyboard: 23 in stock, reorder at 10'\n\n"
        "Use an f‑string to embed the variables.\n"
        "Expected output: Keyboard: 23 in stock, reorder at 10"
    ),
    expected_output="Keyboard: 23 in stock, reorder at 10",
    level=Level.EASY,
    hints=[
        "product = 'Keyboard'",
        "unit_price = 49.99",
        "stock = 23",
        "reorder = 10",
        "print(f'{product}: {stock} in stock, reorder at {reorder}')"
    ]
)

# ── Medium: Employee Validator (string methods, casting, truthiness) ──
medium = Task(
    description=(
        "🧑‍💼  Employee ID Validator\n\n"
        "The Imperial HR system receives raw employee IDs.\n"
        "A valid ID must be exactly 6 characters after stripping\n"
        "and must end with a digit.\n\n"
        "Given:\n"
        "  raw_id = '  EMP123  '\n\n"
        "1. Strip whitespace.\n"
        "2. Check if length is 6 AND the last character is a digit.\n"
        "   (Hint: string's .isdigit() method)\n"
        "3. Print 'Valid' if both conditions are true, else 'Invalid'.\n\n"
        "Expected output: Valid"
    ),
    expected_output="Valid",
    level=Level.MEDIUM,
    hints=[
        "raw_id = '  EMP123  '",
        "clean = raw_id.strip()",
        "if len(clean) == 6 and clean[-1].isdigit(): print('Valid')",
        "else: print('Invalid')"
    ]
)

# ── Hard: Command‑Line Temperature Converter (sys.argv, casting, None) ──
hard = Task(
    description=(
        "🌡️  Imperial Temperature Converter (CLI)\n\n"
        "Write a script that reads a Celsius temperature from\n"
        "the command line and converts it to Fahrenheit.\n"
        "Formula: F = C * 9/5 + 32\n\n"
        "If no argument is given, print 'No input'.\n"
        "If the argument cannot be converted to a float, print 'Invalid'.\n"
        "Otherwise, print the Fahrenheit value with 1 decimal place.\n\n"
        "Example run (with argument 100): 212.0\n"
        "But we'll run without arguments, so expect 'No input'."
    ),
    expected_output="No input",
    level=Level.HARD,
    hints=[
        "import sys",
        "if len(sys.argv) < 2: print('No input')",
        "else:",
        "    try:",
        "        c = float(sys.argv[1])",
        "        f = c * 9/5 + 32",
        "        print(f'{f:.1f}')",
        "    except ValueError:",
        "        print('Invalid')"
    ]
)

if __name__ == "__main__":
    run_sequence([easy, medium, hard],
                 save_path=MODULE_DIR,
                 progress_name=".progress_review_M01.json")
