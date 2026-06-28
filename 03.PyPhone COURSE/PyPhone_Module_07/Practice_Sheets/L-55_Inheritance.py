# =============================================
#  PyPhone Emperor · Module 7
#  PRACTICE L‑55  –  Inheritance
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

print("\n🎯 WELCOME TO L‑55 COACHING")
print("Reuse and extend classes with")
print("inheritance.\n")

# TASK 1 – define parent and child class
task(
    "Define a class `Animal` with `__init__(self, name)` and method `speak(self)` returning 'Some sound'. Then define `Dog` inheriting `Animal` (just `pass`).",
    lambda: type(globals().get('Dog')) == type and issubclass(globals().get('Dog'), globals().get('Animal')),
    hint="class Animal:\n    def __init__(self, name):\n        self.name = name\n    def speak(self):\n        return 'Some sound'\n\nclass Dog(Animal):\n    pass"
)

# TASK 2 – create Dog instance and call inherited methods
task(
    "Create `d = Dog('Buddy')`. Then store `d.name` in `dog_name` and `d.speak()` in `dog_speak`.",
    lambda: check_var('dog_name', str, 'Buddy') and check_var('dog_speak', str, 'Some sound'),
    hint="d = Dog('Buddy')\ndog_name = d.name\ndog_speak = d.speak()"
)

# TASK 3 – override speak in a child class
task(
    "Define a class `Cat(Animal)` that overrides `speak` to return 'Meow'. Create `c = Cat('Whiskers')` and store `c.speak()` in `meow`.",
    lambda: check_var('meow', str, 'Meow'),
    hint="class Cat(Animal):\n    def speak(self):\n        return 'Meow'\nc = Cat('Whiskers')\nmeow = c.speak()"
)

# TASK 4 – using super() to extend parent
task(
    "Define `Bird(Animal)` with `__init__(self, name, can_fly)`. Inside, call `super().__init__(name)` and set `self.can_fly = can_fly`. Then create `b = Bird('Tweety', True)` and store `(b.name, b.can_fly)` as a tuple in `bird_info`.",
    lambda: check_var('bird_info', tuple, ('Tweety', True)),
    hint="class Bird(Animal):\n    def __init__(self, name, can_fly):\n        super().__init__(name)\n        self.can_fly = can_fly\nb = Bird('Tweety', True)\nbird_info = (b.name, b.can_fly)"
)

# TASK 5 – isinstance check
task(
    "Check if `b` (the Bird instance) is an instance of `Animal` and store the boolean result in `is_animal`.",
    lambda: check_var('is_animal', bool, True),
    hint="is_animal = isinstance(b, Animal)"
)

print("\n" + "="*44)
print("🏆 L‑55 complete – Inheritance")
print("is now your code reuse superpower.")
print("="*44)