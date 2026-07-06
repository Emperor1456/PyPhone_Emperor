# =============================================
#  PyPhone Emperor · Module 2
#  PRACTICE L‑20  –  `for` Loop
#  Enterprise Coaching Engine
# =============================================
import sys

def safe_exec(code):
    try:
        exec(code, globals())
        return None
    except Exception as e:
        return str(e)

def check_var(name, expected_type, expected_value=None):
    if name not in globals():
        return False
    val = globals()[name]
    if not isinstance(val, expected_type):
        return False
    if expected_value is not None and val != expected_value:
        return False
    return True

def task(instruction, verify_func, hint):
    print("\n" + "-"*44)
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

print("\n🎯 WELCOME TO L‑20 COACHING")
print("Iterate with `for` loops over")
print("ranges, strings, and lists.\n")

# TASK 1
task(
    "Use a `for` loop with `range(1,6)` to print numbers 1 through 5. After the loop, create a variable `done` and set it to True. (We'll check `done`.)",
    lambda: check_var('done', bool, True),
    hint="for i in range(1,6):\n    print(i)\ndone = True"
)

# TASK 2
task(
    "Create a variable `total = 0`. Use a `for` loop to sum all numbers from 1 to 100 (inclusive) using `range(1,101)`. After the loop, `total` should be 5050.",
    lambda: abs(globals().get('total', 0) - 5050) < 0.001,
    hint="for num in range(1,101):\n    total += num"
)

# TASK 3
task(
    "Given the string `word = 'Python'`, use a `for` loop to iterate over each character, and build a new string `reverse` that contains the characters in reverse order. (Hint: prepend each char.)",
    lambda: check_var('reverse', str, 'nohtyP'),
    hint="reverse = ''\nfor ch in word:\n    reverse = ch + reverse"
)

# TASK 4
task(
    "Given `numbers = [10, 20, 30, 40]`, use a `for` loop to compute the product of all numbers and store it in `product`. (Start product=1.)",
    lambda: abs(globals().get('product', 0) - 240000) < 0.001,
    hint="product = 1\nfor n in numbers:\n    product *= n"
)

print("\n" + "="*44)
print("🏆 L‑20 complete – `for` loop")
print("is your iteration workhorse.")
print("="*44)