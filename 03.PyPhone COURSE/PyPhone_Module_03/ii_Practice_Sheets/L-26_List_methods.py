# =============================================
#  PyPhone Emperor · Module 3
#  PRACTICE L‑26  –  List Methods
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

print("\n🎯 WELCOME TO L‑26 COACHING")
print("Master list manipulation methods.\n")

# TASK 1
task(
    "Create an empty list `items`. Append 'first', then 'second', then 'third'. Check `items` becomes ['first','second','third'].",
    lambda: check_var('items', list, ['first','second','third']),
    hint="items = []\nitems.append('first')\nitems.append('second')\nitems.append('third')"
)

# TASK 2
task(
    "Insert 'middle' at index 1 in `items` (now contains ['first','second','third']). Check `items` equals ['first','middle','second','third'].",
    lambda: check_var('items', list, ['first','middle','second','third']),
    hint="items.insert(1, 'middle')"
)

# TASK 3
task(
    "Remove 'second' from `items` using .remove(). Then check `items` equals ['first','middle','third'].",
    lambda: check_var('items', list, ['first','middle','third']),
    hint="items.remove('second')"
)

# TASK 4
task(
    "Use .pop() to remove and return the last element. Store that element in `popped`. Check `popped` == 'third' and `items` == ['first','middle'].",
    lambda: check_var('popped', str, 'third') and check_var('items', list, ['first','middle']),
    hint="popped = items.pop()"
)

# TASK 5
task(
    "Create `numbers = [3,1,4,1,5]`. Sort it in place, then store the sorted list in `sorted_nums`. Then reverse it in place, store result in `rev_nums`.",
    lambda: check_var('rev_nums', list, [5,4,3,1,1]),
    hint="numbers.sort()\nsorted_nums = numbers.copy()\nnumbers.reverse()\nrev_nums = numbers"
)

print("\n" + "="*44)
print("🏆 L‑26 complete – List methods")
print("now serve your every command.")
print("="*44)