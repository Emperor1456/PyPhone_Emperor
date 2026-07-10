import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "🧮  Imperial Arithmetic – Operator Precedence\n\n"
        "Calculate the following expression and print the result:\n"
        "  10 + 3 * 4\n\n"
        "Remember PEMDAS: multiplication before addition.\n"
        "Expected output: 22"
    ),
    expected_output="22",
    level=Level.EASY,
    hints=["print(10 + 3 * 4)"]
)

easy2 = Task(
    description=(
        "📏  Floor Division & Modulo – Box Packing\n\n"
        "The Imperial Depot needs to pack 250 items into boxes\n"
        "that hold 24 items each.\n\n"
        "Compute:\n"
        "  • boxes = 250 // 24  (full boxes)\n"
        "  • left  = 250 % 24   (items left over)\n\n"
        "Print boxes and left separated by a space.\n"
        "Expected output: 10 10"
    ),
    expected_output="10 10",
    level=Level.EASY,
    hints=["boxes = 250 // 24", "left = 250 % 24", "print(boxes, left)"]
)

medium1 = Task(
    description=(
        "🔄  Safe Type Casting – Clean User Input\n\n"
        "A supplier sent a stock count as a string: '  42  '\n"
        "1. Strip the whitespace\n"
        "2. Convert it to an integer\n"
        "3. Print the integer\n\n"
        "Expected output: 42"
    ),
    expected_output="42",
    level=Level.MEDIUM,
    hints=["raw = '  42  '", "clean = raw.strip()", "stock = int(clean)", "print(stock)"]
)

medium2 = Task(
    description=(
        "💰  Float Precision – Currency Display\n\n"
        "You sold 3 items at $24.99 each.\n"
        "Compute the total and print it formatted to 2 decimal places\n"
        "using f‑string or round.\n\n"
        "Expected output: 74.97"
    ),
    expected_output="74.97",
    level=Level.MEDIUM,
    hints=["price = 24.99", "qty = 3", "total = price * qty", "print(f'{total:.2f}')"]
)

hard1 = Task(
    description=(
        "⚡  Exponentiation – Compound Growth\n\n"
        "The Emperor's investment doubles every period.\n"
        "Start with 1 unit. After 10 periods, the value is 2**10.\n"
        "Compute and print 2 to the power of 10.\n\n"
        "Expected output: 1024"
    ),
    expected_output="1024",
    level=Level.HARD,
    hints=["print(2 ** 10)"]
)

hard2 = Task(
    description=(
        "🧪  Type Casting Chain – String to Float to Int\n\n"
        "A sensor reports temperature as '98.6' (a string).\n"
        "1. Convert it to a float\n"
        "2. Convert that float to an integer (truncation)\n"
        "3. Print the integer value\n\n"
        "Expected output: 98"
    ),
    expected_output="98",
    level=Level.HARD,
    hints=["temp_str = '98.6'", "temp_float = float(temp_str)", "temp_int = int(temp_float)", "print(temp_int)"]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L02.json")
