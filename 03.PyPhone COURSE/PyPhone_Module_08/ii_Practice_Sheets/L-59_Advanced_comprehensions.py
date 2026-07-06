# =============================================
#  PyPhone Emperor · Module 8
#  PRACTICE L‑59  –  Advanced Comprehensions
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

print("\n🎯 WELCOME TO L‑59 COACHING")
print("Master advanced comprehensions.\n")

# TASK 1
task(
    "Create a list comprehension that produces squares of even numbers from 0 to 9. Store in `even_squares`.",
    lambda: check_var('even_squares', list, [0, 4, 16, 36, 64]),
    hint="even_squares = [x**2 for x in range(10) if x % 2 == 0]"
)

# TASK 2
task(
    "Create a list comprehension with a ternary: map numbers 1-5 to 'odd'/'even'. Store in `labels`.",
    lambda: check_var('labels', list, ['odd','even','odd','even','odd']),
    hint="labels = ['even' if x%2==0 else 'odd' for x in range(1,6)]"
)

# TASK 3
task(
    "Flatten `matrix = [[1,2],[3,4],[5,6]]` using a nested list comprehension. Store in `flat`.",
    lambda: check_var('flat', list, [1,2,3,4,5,6]),
    hint="flat = [n for row in matrix for n in row]"
)

# TASK 4
task(
    "Create a dict comprehension: keys 0-4, values their squares. Store in `sq_dict`.",
    lambda: check_var('sq_dict', dict, {0:0,1:1,2:4,3:9,4:16}),
    hint="sq_dict = {x: x**2 for x in range(5)}"
)

# TASK 5
task(
    "Given `words = ['apple','banana','cherry','apple']`, create a set comprehension of their lengths. Store in `lengths`.",
    lambda: check_var('lengths', set, {5,6}),
    hint="lengths = {len(w) for w in words}"
)

print("\n" + "="*44)
print("🏆 L‑59 complete – Advanced")
print("comprehensions mastered.")
print("="*44)