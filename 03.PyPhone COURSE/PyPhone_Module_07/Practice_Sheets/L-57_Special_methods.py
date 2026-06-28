# =============================================
#  PyPhone Emperor · Module 7
#  PRACTICE L‑57  –  Special Methods
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

print("\n🎯 WELCOME TO L‑57 COACHING")
print("Give your objects Python superpowers")
print("with __str__, __repr__, __len__ etc.\n")

# TASK 1 – __str__
task(
    "Define a class `Item` with `__init__(self, name, price)`. Add a `__str__` method that returns f'{self.name} costs ${self.price}'. Then create `item = Item('Widget', 9.99)` and store `str(item)` in `desc`.",
    lambda: check_var('desc', str, 'Widget costs $9.99'),
    hint="class Item:\n    def __init__(self, name, price):\n        self.name = name\n        self.price = price\n    def __str__(self):\n        return f'{self.name} costs ${self.price}'\n\nitem = Item('Widget', 9.99)\ndesc = str(item)"
)

# TASK 2 – __repr__
task(
    "Add a `__repr__` method to `Item` that returns f'Item({self.name!r}, {self.price!r})'. Then store `repr(item)` in `code`.",
    lambda: check_var('code', str, "Item('Widget', 9.99)"),
    hint="class Item:\n    ... (keep previous)\n    def __repr__(self):\n        return f'Item({self.name!r}, {self.price!r})'\n\ncode = repr(item)"
)

# TASK 3 – __len__
task(
    "Define a class `Bundle` with `__init__(self, items)` where items is a list. Add `__len__` to return the number of items. Create `b = Bundle(['a','b','c'])` and store `len(b)` in `size`.",
    lambda: check_var('size', int, 3),
    hint="class Bundle:\n    def __init__(self, items):\n        self.items = items\n    def __len__(self):\n        return len(self.items)\n\nb = Bundle(['a','b','c'])\nsize = len(b)"
)

# TASK 4 – __eq__ and __add__
task(
    "Define a class `Vector` with `__init__(self, x, y)`. Add `__eq__` to compare two vectors (same x and y). Add `__add__` to return a new Vector with summed coordinates. Create `v1 = Vector(1,2)` and `v2 = Vector(3,4)`. Then store `v1 + v2` in `v3`, and test `(v1 == v2, v1 == Vector(1,2))` in a tuple `checks`.",
    lambda: check_var('checks', tuple, (False, True)),
    hint="class Vector:\n    def __init__(self, x, y):\n        self.x, self.y = x, y\n    def __eq__(self, o):\n        return self.x == o.x and self.y == o.y\n    def __add__(self, o):\n        return Vector(self.x+o.x, self.y+o.y)\n\nv1 = Vector(1,2)\nv2 = Vector(3,4)\nv3 = v1 + v2\nchecks = (v1 == v2, v1 == Vector(1,2))"
)

print("\n" + "="*44)
print("🏆 L‑57 complete – Special methods")
print("make your classes Pythonic.")
print("="*44)