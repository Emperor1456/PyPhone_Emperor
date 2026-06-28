# =============================================
#  PyPhone Emperor · Module 8
#  PRACTICE L‑60  –  Generator Expressions & yield
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

print("\n🎯 WELCOME TO L‑60 COACHING")
print("Generators and yield – lazy power.\n")

# TASK 1
task(
    "Create a generator expression that yields squares of numbers 0-4. Store it in `gen`. Then get the first value using `next()` and store in `first`.",
    lambda: check_var('first', int, 0),
    hint="gen = (x**2 for x in range(5))\nfirst = next(gen)"
)

# TASK 2
task(
    "Define a generator function `countdown(n)` that yields from n down to 1. Then create `c = countdown(3)`, exhaust it into a list `result`.",
    lambda: check_var('result', list, [3,2,1]),
    hint="def countdown(n):\n    while n>0:\n        yield n\n        n-=1\n\nc = countdown(3)\nresult = list(c)"
)

# TASK 3
task(
    "Define a generator `read_lines(text)` that yields each line stripped. Use it on a multi-line string `'a\\nb\\nc'` and collect results into `lines`.",
    lambda: check_var('lines', list, ['a','b','c']),
    hint="def read_lines(s):\n    for line in s.split('\\n'):\n        yield line.strip()\n\ntext = 'a\\nb\\nc'\nlines = list(read_lines(text))"
)

# TASK 4
task(
    "Create a generator `infinite_evens()` that yields even numbers starting from 0. Use `next()` three times and store the values in `a,b,c` (three variables).",
    lambda: check_var('a', int, 0) and check_var('b', int, 2) and check_var('c', int, 4),
    hint="def infinite_evens():\n    n=0\n    while True:\n        yield n\n        n+=2\n\ng = infinite_evens()\na=next(g)\nb=next(g)\nc=next(g)"
)

print("\n" + "="*44)
print("🏆 L‑60 complete – Generators")
print("and yield are now your tools.")
print("="*44)