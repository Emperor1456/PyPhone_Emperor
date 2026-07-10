import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

# ── Easy Tasks (2) ──────────────────────────

easy1 = Task(
    description=(
        "🔤  First Character Extraction – Imperial Product Code\n\n"
        "Every Imperial product code starts with a category letter.\n"
        "Given the variable:\n"
        "  code = 'Emperor'\n\n"
        "Print the first character of the code.\n"
        "Expected output: E"
    ),
    expected_output="E",
    level=Level.EASY,
    hints=["code = 'Emperor'", "print(code[0])"]
)

easy2 = Task(
    description=(
        "🔢  Last Character – Order Verification\n\n"
        "Order IDs end with a checksum digit.\n"
        "Given:\n"
        "  order_id = 'ORD-123-X'\n\n"
        "Print the last character (the checksum).\n"
        "Expected output: X"
    ),
    expected_output="X",
    level=Level.EASY,
    hints=["order_id = 'ORD-123-X'", "print(order_id[-1])"]
)

# ── Medium Tasks (2) ──────────────────────

medium1 = Task(
    description=(
        "✂️  Substring Extraction – SKU Parser\n\n"
        "An SKU code contains embedded product identifiers.\n"
        "Given:\n"
        "  sku = 'PyPhone'\n\n"
        "Extract the substring from index 1 to 4 (exclusive 5)\n"
        "and print it.\n"
        "Expected output: yPho"
    ),
    expected_output="yPho",
    level=Level.MEDIUM,
    hints=["sku = 'PyPhone'", "print(sku[1:5])"]
)

medium2 = Task(
    description=(
        "📧  Domain Extractor – Email Parsing\n\n"
        "Given an email address:\n"
        "  email = 'emperor@pyphone.com'\n\n"
        "Print the domain part (everything after '@').\n"
        "Expected output: pyphone.com"
    ),
    expected_output="pyphone.com",
    level=Level.MEDIUM,
    hints=["email = 'emperor@pyphone.com'", "at_pos = email.find('@')", "domain = email[at_pos+1:]", "print(domain)"]
)

# ── Hard Tasks (2) ────────────────────────

hard1 = Task(
    description=(
        "🔄  Palindrome Detector – Mirror Order Check\n\n"
        "An order ID is a palindrome if it reads the same\n"
        "forward and backward.\n"
        "Given:\n"
        "  s = 'radar'\n\n"
        "If s equals its reverse, print 'Palindrome'.\n"
        "Otherwise, print 'Not Palindrome'.\n\n"
        "Expected output: Palindrome"
    ),
    expected_output="Palindrome",
    level=Level.HARD,
    hints=["s = 'radar'", "if s == s[::-1]:", "    print('Palindrome')", "else:", "    print('Not Palindrome')"]
)

hard2 = Task(
    description=(
        "🔐  Masking – Account Number Privacy\n\n"
        "To display a bank account safely, we mask all\n"
        "digits except the last four.\n"
        "Given:\n"
        "  acct = '1234567890123456'\n\n"
        "Print '****' followed by the last 4 digits.\n"
        "Expected output: ****3456"
    ),
    expected_output="****3456",
    level=Level.HARD,
    hints=["acct = '1234567890123456'", "masked = '****' + acct[-4:]", "print(masked)"]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L03.json")
