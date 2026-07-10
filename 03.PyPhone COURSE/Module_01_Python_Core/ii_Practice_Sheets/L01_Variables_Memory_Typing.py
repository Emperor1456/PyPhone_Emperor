import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "📦  Imperial Inventory System – Product Record\n\n"
        "Create three variables exactly as shown:\n"
        "  • product_name = 'Wireless Mouse'\n"
        "  • unit_price   = 24.99\n"
        "  • stock        = 150\n\n"
        "Print them all on one line, separated by\n"
        "a comma and a space.\n\n"
        "Example output: Wireless Mouse, 24.99, 150"
    ),
    expected_output="Wireless Mouse, 24.99, 150",
    level=Level.EASY,
    hints=[
        "product_name = 'Wireless Mouse'",
        "unit_price = 24.99",
        "stock = 150",
        "print(product_name, unit_price, stock, sep=', ')"
    ]
)

easy2 = Task(
    description=(
        "🔖  Professional Naming Conventions\n\n"
        "Variables in Python follow strict conventions.\n"
        "Create:\n"
        "  • MAX_RETRIES = 5   (constant, UPPER_CASE)\n"
        "  • _internal = 'secret' (private, underscore prefix)\n\n"
        "Print MAX_RETRIES on the first line,\n"
        "and _internal on the second line."
    ),
    expected_output="5\nsecret",
    level=Level.EASY,
    hints=[
        "MAX_RETRIES = 5",
        "_internal = 'secret'",
        "print(MAX_RETRIES)",
        "print(_internal)"
    ]
)

medium1 = Task(
    description=(
        "🔄  Dynamic Typing in Action\n\n"
        "1. Assign x = 42\n"
        "2. Reassign x = 'Emperor'\n"
        "3. Print the type name of x using type(x).__name__\n\n"
        "You should see 'str' printed."
    ),
    expected_output="str",
    level=Level.MEDIUM,
    hints=[
        "x = 42",
        "x = 'Emperor'",
        "print(type(x).__name__)"
    ]
)

medium2 = Task(
    description=(
        "🔁  Elegant Swapping\n\n"
        "Python can swap values without a temporary variable.\n"
        "Set a = 10, b = 20.\n"
        "Swap their values in one line (a, b = b, a).\n"
        "Print a and b separated by a space.\n\n"
        "Expected output: 20 10"
    ),
    expected_output="20 10",
    level=Level.MEDIUM,
    hints=[
        "a = 10; b = 20",
        "a, b = b, a",
        "print(a, b)"
    ]
)

hard1 = Task(
    description=(
        "🔍  Identity vs Equality – Integer Caching\n\n"
        "Python caches small integers (-5 to 256).\n"
        "Larger integers are separate objects.\n\n"
        "Create:\n"
        "  a = 100, b = 100   (cached, same object)\n"
        "  c = 300, d = 300   (not cached, different)\n\n"
        "Print two boolean values separated by a space:\n"
        "  1. Whether a is b\n"
        "  2. Whether c is NOT d\n\n"
        "Expected output: True True"
    ),
    expected_output="True True",
    level=Level.HARD,
    hints=[
        "a=100; b=100; c=300; d=300",
        "print(a is b, c is not d)"
    ]
)

hard2 = Task(
    description=(
        "🧩  Mutable vs Immutable Identity\n\n"
        "Two lists with the same content are equal (==)\n"
        "but NOT identical (is).\n\n"
        "Create two separate lists:\n"
        "  a = [1, 2]\n"
        "  b = [1, 2]\n\n"
        "Print two booleans:\n"
        "  • a == b   (should be True)\n"
        "  • a is b   (should be False)\n\n"
        "Output should be: True False"
    ),
    expected_output="True False",
    level=Level.HARD,
    hints=[
        "a = [1, 2]; b = [1, 2]",
        "print(a == b, a is b)"
    ]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L01.json")
