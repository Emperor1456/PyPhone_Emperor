# =============================================
#  PyPhone Emperor · Module 4
#  PRACTICE L‑30  –  Parameters & Arguments
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

print("\n🎯 WELCOME TO L‑30 COACHING")
print("Master positional & keyword arguments.\n")

# TASK 1
task(
    "Define a function `greet` that takes a parameter `name` and returns 'Hello, {name}!'.",
    lambda: callable(globals().get('greet')) and globals()['greet']('Emperor') == 'Hello, Emperor!',
    hint="def greet(name):\n    return f'Hello, {name}!'"
)

# TASK 2
task(
    "Define a function `rectangle_area` that takes `length` and `width` and returns the area.",
    lambda: callable(globals().get('rectangle_area')) and globals()['rectangle_area'](5, 4) == 20,
    hint="def rectangle_area(length, width):\n    return length * width"
)

# TASK 3
task(
    "Call `rectangle_area` using keyword arguments (width=7, length=3) and store the result in `area`. (Define the function first if you haven't.)",
    lambda: check_var('area', int, 21),
    hint="area = rectangle_area(width=7, length=3)"
)

# TASK 4
task(
    "Define a function `describe_person` with parameters `name, age, city` that returns a string like 'Emperor is 18 years old and lives in Dhaka'.",
    lambda: callable(globals().get('describe_person')) and globals()['describe_person']('Emperor', 18, 'Dhaka') == 'Emperor is 18 years old and lives in Dhaka',
    hint="def describe_person(name, age, city):\n    return f'{name} is {age} years old and lives in {city}'"
)

# TASK 5
task(
    "Call `describe_person` using a mix: positional for 'Emperor', keyword for age=18, keyword for city='Dhaka'. Store the result in `desc`.",
    lambda: check_var('desc', str, 'Emperor is 18 years old and lives in Dhaka'),
    hint="desc = describe_person('Emperor', age=18, city='Dhaka')"
)

print("\n" + "="*44)
print("🏆 L‑30 complete – Arguments")
print("flow with precision.")
print("="*44)