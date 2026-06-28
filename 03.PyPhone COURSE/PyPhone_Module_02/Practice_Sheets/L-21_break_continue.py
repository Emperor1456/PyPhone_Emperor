# =============================================
#  PyPhone Emperor · Module 2
#  PRACTICE L‑21  –  `break` and `continue`
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

print("\n🎯 WELCOME TO L‑21 COACHING")
print("Control loop flow with `break`")
print("and `continue`.\n")

# TASK 1
task(
    "Use a `for` loop with `range(1,10)`. Inside, if `i == 5`, break. After the loop, set a variable `stopped_at` to the value of `i` when the loop exited (should be 5).",
    lambda: check_var('stopped_at', int, 5),
    hint="for i in range(1,10):\n    if i == 5:\n        stopped_at = i\n        break"
)

# TASK 2
task(
    "Use a `for` loop with `range(1,6)`. If `i` is even, use `continue` to skip printing. Otherwise, accumulate a string `odds` with the odd numbers concatenated (e.g., '135').",
    lambda: check_var('odds', str, '135'),
    hint="odds = ''\nfor i in range(1,6):\n    if i % 2 == 0:\n        continue\n    odds += str(i)"
)

# TASK 3
task(
    "Simulate searching: iterate over list `names = ['Ana','Bob','Emperor','Zoe']`. When you find 'Emperor', set `found = True` and break. If loop finishes without break, set `found = False`.",
    lambda: check_var('found', bool, True),
    hint="found = False\nfor name in names:\n    if name == 'Emperor':\n        found = True\n        break"
)

# TASK 4
task(
    "Use a `while` loop starting with `x = 10`. Subtract 2 each iteration. If `x` becomes negative, break. Otherwise, `continue` (implicitly by not breaking). After loop, set `final_x` to the value of x when loop ended (should be -2).",
    lambda: check_var('final_x', int, -2),
    hint="x = 10\nwhile True:\n    x -= 2\n    if x < 0:\n        final_x = x\n        break"
)

print("\n" + "="*44)
print("🏆 L‑21 complete – `break` and")
print("`continue` give you fine control.")
print("="*44)