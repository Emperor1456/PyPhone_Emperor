import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks (2) ──────────────────────────

easy1 = Task(
    description=(
        "🧼  Strip & Clean – Sanitize Warehouse Input\n\n"
        "A warehouse worker entered a product code with\n"
        "extra spaces: '   EMP-101   '\n\n"
        "1. Strip the whitespace from both ends.\n"
        "2. Print the cleaned code.\n\n"
        "Expected output: EMP-101"
    ),
    expected_output="EMP-101",
    level=Level.EASY,
    hints=["code = '   EMP-101   '", "clean = code.strip()", "print(clean)"]
)

easy2 = Task(
    description=(
        "🔍  Search & Count – Email Inspection\n\n"
        "Given:\n"
        "  email = 'emperor@pyphone.com'\n\n"
        "Print the position of the '@' symbol (using find)\n"
        "and the number of 'o' characters (using count),\n"
        "separated by a space.\n\n"
        "Expected output: 7 2"
    ),
    expected_output="7 2",
    level=Level.EASY,
    hints=["email = 'emperor@pyphone.com'", "pos = email.find('@')", "cnt = email.count('o')", "print(pos, cnt)"]
)

# ── Medium Tasks (2) ──────────────────────

medium1 = Task(
    description=(
        "✂️  Split & Join – CSV to Readable List\n\n"
        "A supplier sent inventory as a comma-separated string:\n"
        "  'laptop,mouse,keyboard,monitor'\n\n"
        "1. Split it into a list.\n"
        "2. Join the list with ' | ' as separator.\n"
        "3. Print the resulting string.\n\n"
        "Expected output: laptop | mouse | keyboard | monitor"
    ),
    expected_output="laptop | mouse | keyboard | monitor",
    level=Level.MEDIUM,
    hints=["data = 'laptop,mouse,keyboard,monitor'", "items = data.split(',')", "result = ' | '.join(items)", "print(result)"]
)

medium2 = Task(
    description=(
        "🔄  Replace – Fix a Product Slug\n\n"
        "A product name was entered with underscores instead\n"
        "of hyphens: 'wireless_mouse_pro'\n\n"
        "1. Replace all underscores with hyphens.\n"
        "2. Convert to uppercase.\n"
        "3. Print the final code.\n\n"
        "Expected output: WIRELESS-MOUSE-PRO"
    ),
    expected_output="WIRELESS-MOUSE-PRO",
    level=Level.MEDIUM,
    hints=["slug = 'wireless_mouse_pro'", "slug = slug.replace('_', '-')", "slug = slug.upper()", "print(slug)"]
)

# ── Hard Tasks (2) ────────────────────────

hard1 = Task(
    description=(
        "💰  Receipt Generator – f‑string Formatting\n\n"
        "Create a receipt for an order:\n"
        "  • item = 'Laptop'\n"
        "  • price = 999.99\n"
        "  • qty = 2\n\n"
        "Print a formatted string:\n"
        "  '2 x Laptop = $1999.98'\n\n"
        "Use f‑string with :.2f for the total.\n"
        "Expected output: 2 x Laptop = $1999.98"
    ),
    expected_output="2 x Laptop = $1999.98",
    level=Level.HARD,
    hints=["item = 'Laptop'", "price = 999.99", "qty = 2", "total = price * qty", "print(f'{qty} x {item} = ${total:.2f}')"]
)

hard2 = Task(
    description=(
        "📊  Column Formatter – Right‑Aligned Table\n\n"
        "Print a simple inventory table with aligned columns.\n"
        "Items:\n"
        "  Mouse     $24.99\n"
        "  Keyboard  $49.99\n\n"
        "Print each line exactly as shown above, with the\n"
        "item left‑justified in 10 spaces and the price\n"
        "right‑justified in 7 spaces.\n\n"
        "Expected output:\nMouse       $24.99\nKeyboard    $49.99"
    ),
    expected_output="Mouse       $24.99\nKeyboard    $49.99",
    level=Level.HARD,
    hints=[
        "print(f'{'Mouse':10} ${24.99:6.2f}')",
        "print(f'{'Keyboard':10} ${49.99:6.2f}')"
    ]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L04.json")
