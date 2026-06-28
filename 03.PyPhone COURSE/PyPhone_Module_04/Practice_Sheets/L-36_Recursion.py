# =============================================
#  PyPhone Emperor · Module 4
#  PRACTICE L‑36  –  Recursion
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

print("\n🎯 WELCOME TO L‑36 COACHING")
print("Write functions that call themselves.\n")

# TASK 1
task(
    "Define a recursive function `factorial(n)` that returns n! (n factorial). Base: n<=1 returns 1.",
    lambda: callable(globals().get('factorial')) and globals()['factorial'](5) == 120 and globals()['factorial'](0) == 1,
    hint="def factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n-1)"
)

# TASK 2
task(
    "Define a recursive function `sum_list(lst)` that returns the sum of all numbers in the list. Base: empty list returns 0.",
    lambda: callable(globals().get('sum_list')) and globals()['sum_list']([1,2,3,4]) == 10 and globals()['sum_list']([]) == 0,
    hint="def sum_list(lst):\n    if not lst:\n        return 0\n    return lst[0] + sum_list(lst[1:])"
)

# TASK 3
task(
    "Define a recursive function `fib(n)` that returns the nth Fibonacci number (0-based: fib(0)=0, fib(1)=1).",
    lambda: callable(globals().get('fib')) and globals()['fib'](6) == 8 and globals()['fib'](0) == 0,
    hint="def fib(n):\n    if n <= 1:\n        return n\n    return fib(n-1) + fib(n-2)"
)

# TASK 4
task(
    "Define a recursive function `reverse_string(s)` that returns the reversed string. Base: empty string returns empty string.",
    lambda: callable(globals().get('reverse_string')) and globals()['reverse_string']('abc') == 'cba' and globals()['reverse_string']('') == '',
    hint="def reverse_string(s):\n    if len(s) == 0:\n        return s\n    return reverse_string(s[1:]) + s[0]"
)

print("\n" + "="*44)
print("🏆 L‑36 complete – Recursion")
print("is now a tool in your arsenal.")
print("="*44)