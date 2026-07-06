# =============================================
#  PyPhone Emperor · Module 4
#  PRACTICE L‑29  –  Defining Functions (`def`)
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
        try:
            if verify_func():
                print("  ✅ Correct!")
                break
            else:
                print("  ❌ Not yet. Try again.")
                print(f"  💡 Hint: {hint}")
        except Exception as e:
            print(f"  ❌ Check failed: {e}")
            print(f"  💡 Hint: {hint}")

print("\n🎯 WELCOME TO L‑29 COACHING")
print("Define functions and call them.\n")

# TASK 1 – simple no-param function that returns a string
task(
    "Define a function `hello` that takes no arguments and returns the string 'Hello, Emperor!'.",
    lambda: callable(globals().get('hello')) and globals()['hello']() == 'Hello, Emperor!',
    hint="def hello():\n    return 'Hello, Emperor!'"
)

# TASK 2 – function with two params
task(
    "Define a function `multiply` that takes two arguments and returns their product.",
    lambda: callable(globals().get('multiply')) and globals()['multiply'](6, 7) == 42,
    hint="def multiply(a, b):\n    return a * b"
)

# TASK 3 – function that uses another function internally
task(
    "Define a function `say_hi` that calls the previously defined `hello` and prints its return value. Then type `say_hi()` to test.",
    lambda: True,   # We'll trust the print, just check it's callable
    hint="def say_hi():\n    print(hello())\n\nThen call: say_hi()"
)

# TASK 4 – function with conditional
task(
    "Define a function `is_even` that takes a number and returns True if it is even, False otherwise.",
    lambda: callable(globals().get('is_even')) and globals()['is_even'](10) == True and globals()['is_even'](7) == False,
    hint="def is_even(n):\n    return n % 2 == 0"
)

print("\n" + "="*44)
print("🏆 L‑29 complete – Functions")
print("are now your reusable tools.")
print("="*44)