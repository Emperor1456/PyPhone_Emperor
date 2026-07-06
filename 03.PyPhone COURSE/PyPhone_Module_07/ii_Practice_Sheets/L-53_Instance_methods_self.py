# =============================================
#  PyPhone Emperor · Module 7
#  PRACTICE L‑53  –  Instance Methods & `self`
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

print("\n🎯 WELCOME TO L‑53 COACHING")
print("Add behaviour to your objects with")
print("instance methods and `self`.\n")

# TASK 1 – define a class with a method that uses self
task(
    "Define a class `Person` with `__init__(self, name)` and a method `greet(self)` that returns 'Hi, I am ' + self.name.",
    lambda: callable(getattr(globals().get('Person'), 'greet', None)) and globals().get('Person')('Emperor').greet() == 'Hi, I am Emperor',
    hint="class Person:\n    def __init__(self, name):\n        self.name = name\n    def greet(self):\n        return 'Hi, I am ' + self.name"
)

# TASK 2 – call the method on an instance
task(
    "Create an instance `p1 = Person('Emperor')` and store the result of `p1.greet()` in `greeting`.",
    lambda: check_var('greeting', str, 'Hi, I am Emperor'),
    hint="p1 = Person('Emperor')\ngreeting = p1.greet()"
)

# TASK 3 – method that modifies state
task(
    "Define a class `Counter` with `__init__(self)` that sets `self.value = 0`, and a method `increment(self)` that adds 1 to `self.value`. Then create an instance `c = Counter()` and call `c.increment()` three times. Finally, set `result = c.value`.",
    lambda: check_var('result', int, 3),
    hint="class Counter:\n    def __init__(self):\n        self.value = 0\n    def increment(self):\n        self.value += 1\n\nc = Counter()\nc.increment()\nc.increment()\nc.increment()\nresult = c.value"
)

# TASK 4 – method with parameters
task(
    "Define a class `Calculator` with a method `add(self, a, b)` that returns a+b. Create an instance `calc = Calculator()` and store the sum of 12 and 8 in `total` using the method.",
    lambda: check_var('total', int, 20),
    hint="class Calculator:\n    def add(self, a, b):\n        return a + b\n\ncalc = Calculator()\ntotal = calc.add(12, 8)"
)

print("\n" + "="*44)
print("🏆 L‑53 complete – Instance methods")
print("now power your objects.")
print("="*44)