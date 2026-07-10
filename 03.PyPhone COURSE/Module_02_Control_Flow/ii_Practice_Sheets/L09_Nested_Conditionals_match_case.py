import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks (2) ──────────────────────────

easy1 = Task(
    description=(
        "🪪  Access Control – Login & Admin\n\n"
        "A system checks if a user is logged in first.\n"
        "Only then it checks if they are an admin.\n\n"
        "Given:\n"
        "  is_logged_in = True\n"
        "  is_admin = False\n\n"
        "Print 'Admin panel' if both are true,\n"
        "'User dashboard' if logged in but not admin,\n"
        "'Please log in' otherwise.\n\n"
        "Expected output: User dashboard"
    ),
    expected_output="User dashboard",
    level=Level.EASY,
    hints=[
        "is_logged_in = True",
        "is_admin = False",
        "if is_logged_in:",
        "    if is_admin: print('Admin panel')",
        "    else: print('User dashboard')",
        "else: print('Please log in')"
    ]
)

easy2 = Task(
    description=(
        "🎫  Discount Engine – Member & Purchase\n\n"
        "A store gives discounts to members.\n"
        "Given:\n"
        "  member = True\n"
        "  purchase = 150\n\n"
        "If member and purchase > 100, print '20% off'.\n"
        "If member but purchase <= 100, print '10% off'.\n"
        "If not a member, print 'No discount'.\n\n"
        "Expected output: 20% off"
    ),
    expected_output="20% off",
    level=Level.EASY,
    hints=[
        "member = True; purchase = 150",
        "if member:",
        "    if purchase > 100: print('20% off')",
        "    else: print('10% off')",
        "else: print('No discount')"
    ]
)

# ── Medium Tasks (2) ──────────────────────

medium1 = Task(
    description=(
        "🏧  ATM Menu – Basic match‑case\n\n"
        "Use a match‑case to handle ATM options.\n"
        "Given:\n"
        "  choice = 2\n\n"
        "Print:\n"
        "  • 1 → 'Balance inquiry'\n"
        "  • 2 → 'Cash withdrawal'\n"
        "  • 3 → 'Deposit'\n"
        "  • _ → 'Invalid'\n\n"
        "Expected output: Cash withdrawal"
    ),
    expected_output="Cash withdrawal",
    level=Level.MEDIUM,
    hints=[
        "choice = 2",
        "match choice:",
        "    case 1: print('Balance inquiry')",
        "    case 2: print('Cash withdrawal')",
        "    case 3: print('Deposit')",
        "    case _: print('Invalid')"
    ]
)

medium2 = Task(
    description=(
        "🌍  Language Selector – match with strings\n\n"
        "A greeting system supports multiple languages.\n"
        "Given:\n"
        "  lang = 'fr'\n\n"
        "Print:\n"
        "  • 'en' → 'Hello'\n"
        "  • 'fr' → 'Bonjour'\n"
        "  • 'es' → 'Hola'\n"
        "  • _    → 'Unknown language'\n\n"
        "Expected output: Bonjour"
    ),
    expected_output="Bonjour",
    level=Level.MEDIUM,
    hints=[
        "lang = 'fr'",
        "match lang:",
        "    case 'en': print('Hello')",
        "    case 'fr': print('Bonjour')",
        "    case 'es': print('Hola')",
        "    case _: print('Unknown language')"
    ]
)

# ── Hard Tasks (2) ────────────────────────

hard1 = Task(
    description=(
        "🧪  Lab Result – match with guard\n\n"
        "A medical system classifies a test result.\n"
        "Given:\n"
        "  value = 12\n\n"
        "Use match with guards to print:\n"
        "  • value < 0  → 'Negative'\n"
        "  • value == 0 → 'Zero'\n"
        "  • value > 0  → 'Positive'\n\n"
        "Expected output: Positive"
    ),
    expected_output="Positive",
    level=Level.HARD,
    hints=[
        "value = 12",
        "match value:",
        "    case x if x < 0: print('Negative')",
        "    case 0: print('Zero')",
        "    case x if x > 0: print('Positive')"
    ]
)

hard2 = Task(
    description=(
        "📦  Warehouse – Nested Conditions + match\n\n"
        "A shipment is classified by weight and destination.\n"
        "Given:\n"
        "  weight = 15\n"
        "  destination = 'international'\n\n"
        "Use nested logic (if inside match or match inside if):\n"
        "If destination is 'domestic':\n"
        "  weight <= 10 → 'Standard domestic'\n"
        "  weight > 10  → 'Heavy domestic'\n"
        "If destination is 'international':\n"
        "  weight <= 10 → 'Standard international'\n"
        "  weight > 10  → 'Heavy international'\n"
        "Otherwise: 'Unknown destination'\n\n"
        "Expected output: Heavy international"
    ),
    expected_output="Heavy international",
    level=Level.HARD,
    hints=[
        "weight = 15; destination = 'international'",
        "if destination == 'domestic':",
        "    if weight <= 10: print('Standard domestic')",
        "    else: print('Heavy domestic')",
        "elif destination == 'international':",
        "    if weight <= 10: print('Standard international')",
        "    else: print('Heavy international')",
        "else: print('Unknown destination')"
    ]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L09.json")
