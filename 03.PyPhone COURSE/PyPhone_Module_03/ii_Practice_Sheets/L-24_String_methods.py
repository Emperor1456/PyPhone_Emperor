# =============================================
#  PyPhone Emperor · Module 3
#  PRACTICE L‑24  –  String Methods
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

print("\n🎯 WELCOME TO L‑24 COACHING")
print("Use string methods to transform")
print("and analyze text.\n")

# TASK 1
task(
    "Create `msg = ' hello world '`. Use a method to convert to uppercase and strip whitespace, storing result in `clean`.",
    lambda: check_var('clean', str, 'HELLO WORLD'),
    hint="msg = ' hello world '\nclean = msg.strip().upper()"
)

# TASK 2
task(
    "Given `email = 'emperor@domain.com'`, find the position of '@' and store in `at_pos`.",
    lambda: check_var('at_pos', int, 7),
    hint="at_pos = email.find('@')"
)

# TASK 3
task(
    "Count how many times 'o' appears in `email` and store in `o_count`.",
    lambda: check_var('o_count', int, 2),
    hint="o_count = email.count('o')"
)

# TASK 4
task(
    "Given `data = 'apple,banana,grape'`, split by ',' and store the list in `fruits`.",
    lambda: check_var('fruits', list, ['apple', 'banana', 'grape']),
    hint="fruits = data.split(',')"
)

# TASK 5
task(
    "Create a list `words = ['PyPhone', 'Emperor']`. Use join to make a single string with space separator and store in `title`.",
    lambda: check_var('title', str, 'PyPhone Emperor'),
    hint="title = ' '.join(words)"
)

# TASK 6
task(
    "Given `path = 'C:\\\\Users\\\\OldName\\\\docs'`, replace 'OldName' with 'Emperor' and store in `new_path`.",
    lambda: check_var('new_path', str, 'C:\\Users\\Emperor\\docs'),
    hint="new_path = path.replace('OldName', 'Emperor')"
)

print("\n" + "="*44)
print("🏆 L‑24 complete – String methods")
print("now flow through your code.")
print("="*44)