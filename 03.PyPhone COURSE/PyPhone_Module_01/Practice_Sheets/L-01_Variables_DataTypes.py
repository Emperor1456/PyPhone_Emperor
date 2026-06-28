# =============================================
#  PyPhone Emperor · Module 1
#  PRACTICE L‑01  –  Variables & Data Types
#  Enterprise Coaching Engine
# =============================================
import sys

def safe_exec(user_code):
    """Execute user's code in global namespace.
       Return None on success, error string otherwise."""
    try:
        exec(user_code, globals())
        return None
    except Exception as e:
        return str(e)

def check_var(name, expected_type, expected_value=None):
    """Return True if variable exists, matches type and (optionally) value."""
    if name not in globals():
        return False
    val = globals()[name]
    if not isinstance(val, expected_type):
        return False
    if expected_value is not None and val != expected_value:
        return False
    return True

def task(instruction, verify_func, hint):
    """Present instruction, wait for correct code."""
    print("\n" + "-"*44)
    # Wrap instruction text to fit phone width
    words = instruction.split()
    line = "  📋 "
    for w in words:
        if len(line) + len(w) + 1 > 42:
            print(line)
            line = "      " + w
        else:
            if line == "  📋 ":
                line += w
            else:
                line += " " + w
    print(line)
    print("-"*44)

    while True:
        code = input("  >>> ").strip()
        if code.lower() in ("exit", "quit"):
            print("\n👋 Practice ended.")
            sys.exit(0)
        err = safe_exec(code)
        if err:
            print(f"  ❌ Python error: {err}")
            print(f"  💡 Hint: {hint}")
            continue
        if verify_func():
            print("  ✅ Correct!")
            break
        else:
            print("  ❌ Not yet. Try again.")
            print(f"  💡 Hint: {hint}")

print("\n🎯 WELCOME TO L‑01 COACHING")
print("For each task, type the exact Python line")
print("to complete it, then press Enter.")
print("Type 'exit' at any time to quit.\n")

# ---- TASK 1 ----
task(
    "Create a variable 'product' with the string value 'Monitor'.",
    lambda: check_var('product', str, 'Monitor'),
    hint="product = 'Monitor'"
)

# ---- TASK 2 ----
task(
    "Create a variable 'quantity' with the integer value 3.",
    lambda: check_var('quantity', int, 3),
    hint="quantity = 3"
)

# ---- TASK 3 ----
task(
    "Create a variable 'price' with the float value 249.95.",
    lambda: check_var('price', float, 249.95),
    hint="price = 249.95"
)

# ---- TASK 4 ----
def total_ok():
    if 'total' not in globals():
        return False
    t = globals()['total']
    expected = 3 * 249.95
    return isinstance(t, float) and abs(t - expected) < 0.001

task(
    "Multiply quantity by price, store result in new variable 'total'.",
    total_ok,
    hint="total = quantity * price"
)

# ---- TASK 5 ----
task(
    "Demonstrate dynamic typing: first write 'x = 100', then 'x = 'hundred''.",
    lambda: check_var('x', str, 'hundred'),
    hint="x = 100   (first line)   then   x = 'hundred'   (second line)"
)

print("\n" + "="*44)
print("🏆 All tasks passed!")
print("L‑01 Variables & Data Types – Mastered")
print("="*44)