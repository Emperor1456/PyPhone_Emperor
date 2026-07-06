# =============================================
#  PyPhone Emperor · Module 8
#  PRACTICE L‑66  –  Introduction to Testing
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

print("\n🎯 WELCOME TO L‑66 COACHING")
print("Write tests with assert and unittest.\n")

# TASK 1
task(
    "Define a function `multiply(a,b)` that returns a*b. Then use `assert` to test: `assert multiply(2,3) == 6`. After the assert, set `passed = True`.",
    lambda: check_var('passed', bool, True),
    hint="def multiply(a,b):\n    return a*b\n\nassert multiply(2,3) == 6\npassed = True"
)

# TASK 2
task(
    "Write a unittest class `TestAdd` that tests a function `add(a,b)` returning a+b. Include test methods `test_pos`, `test_neg`, `test_zero`. At the end, set `tests_written = 3`.",
    lambda: check_var('tests_written', int, 3),
    hint="import unittest\n\ndef add(a,b):\n    return a+b\n\nclass TestAdd(unittest.TestCase):\n    def test_pos(self):\n        self.assertEqual(add(2,3), 5)\n    def test_neg(self):\n        self.assertEqual(add(-1,-1), -2)\n    def test_zero(self):\n        self.assertEqual(add(0,5), 5)\n\ntests_written = 3"
)

# TASK 3
task(
    "Demonstrate `setUp` in unittest: write a class `TestCounter` with `setUp` that creates `self.count = 0`. One test method `test_increment` that adds 1 and asserts `self.count == 1`. Set `has_setup = True` after defining the class.",
    lambda: check_var('has_setup', bool, True),
    hint="import unittest\n\nclass TestCounter(unittest.TestCase):\n    def setUp(self):\n        self.count = 0\n    def test_increment(self):\n        self.count += 1\n        self.assertEqual(self.count, 1)\n\nhas_setup = True"
)

# TASK 4
task(
    "Explain in a string `why_test`: why is testing important? (at least 20 chars).",
    lambda: check_var('why_test', str) and len(globals()['why_test']) > 20,
    hint="why_test = 'Testing catches bugs early, ensures code works correctly, and allows safe refactoring.'"
)

print("\n" + "="*44)
print("🏆 L‑66 complete – Testing is now")
print("part of your professional workflow.")
print("="*44)