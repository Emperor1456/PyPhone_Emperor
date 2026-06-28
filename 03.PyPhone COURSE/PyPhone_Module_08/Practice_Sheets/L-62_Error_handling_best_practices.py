# =============================================
#  PyPhone Emperor · Module 8
#  PRACTICE L‑62  –  Error Handling Best Practices
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

print("\n🎯 WELCOME TO L‑62 COACHING")
print("Write robust, maintainable error handling.\n")

# TASK 1
task(
    "Write a try/except that converts `s = '42'` to int. Catch only ValueError. On success, set `ok = True`. On ValueError, set `ok = False`. The input is valid so `ok` should be True.",
    lambda: check_var('ok', bool, True),
    hint="s = '42'\ntry:\n    int(s)\n    ok = True\nexcept ValueError:\n    ok = False"
)

# TASK 2
task(
    "Demonstrate good practice: put only the risky line inside try. Convert `s = 'abc'` to int, catch ValueError, set `value = 0`. Then after the except, set `status = 'processed'`. Ensure both variables are set.",
    lambda: check_var('value', int, 0) and check_var('status', str, 'processed'),
    hint="s = 'abc'\ntry:\n    value = int(s)\nexcept ValueError:\n    value = 0\nstatus = 'processed'"
)

# TASK 3
task(
    "Show the danger of bare except. Write a try/except with bare `except:` that sets `bad_practice = True`. Then write another with `except Exception:` that sets `better = True`. We'll check both are True (just for learning).",
    lambda: check_var('bad_practice', bool, True) and check_var('better', bool, True),
    hint="try:\n    raise ValueError()\nexcept:\n    bad_practice = True\n\ntry:\n    raise ValueError()\nexcept Exception:\n    better = True"
)

# TASK 4
task(
    "Never use exception for flow control: Write an if statement that checks if a string `s = '123'` is all digits using `.isdigit()` before converting, instead of try/except. Set `valid = True` if it is all digits, else `False`.",
    lambda: check_var('valid', bool, True),
    hint="s = '123'\nif s.isdigit():\n    valid = True\nelse:\n    valid = False"
)

print("\n" + "="*44)
print("🏆 L‑62 complete – Error handling")
print("best practices locked in.")
print("="*44)