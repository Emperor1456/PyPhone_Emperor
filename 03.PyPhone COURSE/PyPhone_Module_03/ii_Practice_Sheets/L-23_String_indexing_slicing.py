# =============================================
#  PyPhone Emperor · Module 3
#  PRACTICE L‑23  –  String Indexing & Slicing
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

print("\n🎯 WELCOME TO L‑23 COACHING")
print("Master string indexing and slicing.\n")

# TASK 1
task(
    "Create a variable `word` with value 'Python'. Then extract the first character using indexing and store in `first`.",
    lambda: check_var('first', str, 'P'),
    hint="word = 'Python'\nfirst = word[0]"
)

# TASK 2
task(
    "Using the same `word`, extract the last character using a negative index and store in `last`.",
    lambda: check_var('last', str, 'n'),
    hint="last = word[-1]"
)

# TASK 3
task(
    "Slice `word` to get the substring 'yth' (indices 1,2,3) and store in `sub`.",
    lambda: check_var('sub', str, 'yth'),
    hint="sub = word[1:4]"
)

# TASK 4
task(
    "Reverse the string `word` using slicing and store in `rev`.",
    lambda: check_var('rev', str, 'nohtyP'),
    hint="rev = word[::-1]"
)

# TASK 5
task(
    "Create `text = 'Hello World'`. Use slicing to extract 'World' (negative index slicing) and store in `part`.",
    lambda: check_var('part', str, 'World'),
    hint="text = 'Hello World'\npart = text[-5:]"
)

print("\n" + "="*44)
print("🏆 L‑23 complete – Indexing & slicing")
print("are at your fingertips.")
print("="*44)