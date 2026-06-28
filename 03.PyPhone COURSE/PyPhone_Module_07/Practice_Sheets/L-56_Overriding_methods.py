# =============================================
#  PyPhone Emperor · Module 7
#  PRACTICE L‑56  –  Overriding Methods
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

print("\n🎯 WELCOME TO L‑56 COACHING")
print("Override parent methods and extend")
print("behaviour with super().\n")

# TASK 1 – basic override
task(
    "Define a class `Vehicle` with method `move(self)` returning 'moving'. Then define `Car(Vehicle)` that overrides `move` to return 'driving'. Create a Car instance and store `action = car.move()`.",
    lambda: check_var('action', str, 'driving'),
    hint="class Vehicle:\n    def move(self):\n        return 'moving'\n\nclass Car(Vehicle):\n    def move(self):\n        return 'driving'\n\ncar = Car()\naction = car.move()"
)

# TASK 2 – overriding __init__ without super (be careful)
task(
    "Define `Person` with `__init__(self, name)`. Then define `Student(Person)` with its own `__init__(self, name, school)` that sets both attributes. Create `s = Student('Emperor', 'PyPhone Uni')` and store `(s.name, s.school)` in `student_info`.",
    lambda: check_var('student_info', tuple, ('Emperor', 'PyPhone Uni')),
    hint="class Person:\n    def __init__(self, name):\n        self.name = name\n\nclass Student(Person):\n    def __init__(self, name, school):\n        self.name = name   # manually set instead of super\n        self.school = school\n\ns = Student('Emperor', 'PyPhone Uni')\nstudent_info = (s.name, s.school)"
)

# TASK 3 – extending with super()
task(
    "Define `Employee` with `__init__(self, name, salary)` and `details(self)` returning 'name earns salary'. Then define `Manager(Employee)` that overrides `__init__` to add `department`, calls `super().__init__(name, salary)`, and overrides `details` to return the parent details + ' and manages ' + department. Create `m = Manager('Emperor', 50000, 'IT')` and store `m.details()` in `info`.",
    lambda: check_var('info', str, 'Emperor earns 50000 and manages IT'),
    hint="class Employee:\n    def __init__(self, name, salary):\n        self.name = name\n        self.salary = salary\n    def details(self):\n        return f'{self.name} earns {self.salary}'\n\nclass Manager(Employee):\n    def __init__(self, name, salary, department):\n        super().__init__(name, salary)\n        self.department = department\n    def details(self):\n        return super().details() + f' and manages {self.department}'\n\nm = Manager('Emperor', 50000, 'IT')\ninfo = m.details()"
)

# TASK 4 – check isinstance and method resolution
task(
    "Using the above, store `is_manager_employee = isinstance(m, Employee)` in a variable.",
    lambda: check_var('is_manager_employee', bool, True),
    hint="is_manager_employee = isinstance(m, Employee)"
)

print("\n" + "="*44)
print("🏆 L‑56 complete – Overriding")
print("and super() are now natural.")
print("="*44)