# =============================================
#  PyPhone Emperor · Module 7
#  PRACTICE L‑58  –  Property Decorators
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

print("\n🎯 WELCOME TO L‑58 COACHING")
print("Control attribute access with")
print("@property, setters, and deleters.\n")

# TASK 1 – read-only property
task(
    "Define a class `Circle` with `__init__(self, radius)`. Add a `@property` method `diameter` that returns `2 * self.radius`. Create `c = Circle(5)`. Store `c.diameter` in `dia`.",
    lambda: check_var('dia', int, 10),
    hint="class Circle:\n    def __init__(self, radius):\n        self.radius = radius\n    @property\n    def diameter(self):\n        return 2 * self.radius\n\nc = Circle(5)\ndia = c.diameter"
)

# TASK 2 – setter with validation
task(
    "Extend the `Circle` class: rename the internal attribute to `_radius`. Add a `@property` for `radius` that returns `self._radius`. Add a `@radius.setter` that raises `ValueError('Radius cannot be negative')` if `value < 0`, else sets `self._radius = value`. Then create `c2 = Circle(10)` and try to set `c2.radius = -2` inside a try/except ValueError and set `error_caught = True`.",
    lambda: check_var('error_caught', bool, True),
    hint="class Circle:\n    def __init__(self, radius):\n        self._radius = radius\n    @property\n    def radius(self):\n        return self._radius\n    @radius.setter\n    def radius(self, value):\n        if value < 0:\n            raise ValueError('Radius cannot be negative')\n        self._radius = value\n\nc2 = Circle(10)\nerror_caught = False\ntry:\n    c2.radius = -2\nexcept ValueError:\n    error_caught = True"
)

# TASK 3 – deleter
task(
    "Add a `@radius.deleter` to the Circle class that deletes `self._radius`. Then create `c3 = Circle(7)`, delete `c3.radius` with `del c3.radius`, and check that `hasattr(c3, '_radius')` is False. Store the boolean result in `deleted`.",
    lambda: check_var('deleted', bool, False),  # hasattr returns False after deletion
    hint="class Circle:\n    ... (keep previous) \n    @radius.deleter\n    def radius(self):\n        del self._radius\n\nc3 = Circle(7)\ndel c3.radius\ndeleted = hasattr(c3, '_radius')"
)

print("\n" + "="*44)
print("🏆 L‑58 complete – Properties")
print("give you clean, Pythonic control.")
print("="*44)