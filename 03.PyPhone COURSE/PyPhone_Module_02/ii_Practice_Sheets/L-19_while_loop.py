# =============================================
#  PyPhone Emperor · Module 2
#  PRACTICE L‑19  –  `while` Loop
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

print("\n🎯 WELCOME TO L‑19 COACHING")
print("Master the `while` loop to")
print("repeat actions while a condition")
print("holds true.\n")

# TASK 1
task(
    "Create a variable `count = 1`. Write a `while` loop that prints numbers from 1 to 5 (inclusive). Use a condition `count <= 5` and increment inside. (Just write the loop; we'll check `count` is 6 after loop.)",
    lambda: check_var('count', int, 6),
    hint="while count <= 5:\n    print(count)\n    count += 1"
)

# TASK 2
task(
    "Start with `total = 0` and `num = 1`. Write a `while` loop that adds `num` to `total` as long as `num <= 10`, then increment `num`. After loop, `total` should be sum 1..10 = 55.",
    lambda: abs(globals().get('total', 0) - 55) < 0.001,
    hint="while num <= 10:\n    total += num\n    num += 1"
)

# TASK 3
task(
    "Set `password = ''`. Write a `while` loop that keeps asking for input with `input('Enter password: ')` and assigns to `password` until its length is at least 6. (We'll simulate input; just write the loop structure using `input()`.) For testing, we'll check that after a correct input is given, the loop ends. For now, create a variable `attempts = 0` and increment inside, stop after 3 attempts.",
    lambda: check_var('attempts', int, 3),
    hint="attempts = 0\npassword = ''\nwhile len(password) < 6 and attempts < 3:\n    password = input('Enter password: ')\n    attempts += 1"
)

print("\n" + "="*44)
print("🏆 L‑19 complete – `while` loop")
print("is your repetition engine.")
print("="*44)