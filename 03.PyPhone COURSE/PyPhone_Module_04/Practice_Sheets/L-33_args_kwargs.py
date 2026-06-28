# =============================================
#  PyPhone Emperor · Module 4
#  PRACTICE L‑33  –  `*args` & `**kwargs`
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

print("\n🎯 WELCOME TO L‑33 COACHING")
print("Handle any number of positional")
print("and keyword arguments.\n")

# TASK 1
task(
    "Define `sum_all(*args)` that returns the sum of all positional arguments.",
    lambda: callable(globals().get('sum_all')) and globals()['sum_all'](1,2,3) == 6 and globals()['sum_all']() == 0,
    hint="def sum_all(*args):\n    return sum(args)"
)

# TASK 2
task(
    "Define `greet_all(greeting, *names)` that prints 'greeting, name!' for each name. Then call it with 'Hi' and three names. (We'll just check the function exists.)",
    lambda: callable(globals().get('greet_all')),
    hint="def greet_all(greeting, *names):\n    for n in names:\n        print(f'{greeting}, {n}!')"
)

# TASK 3
task(
    "Define `show_details(**kwargs)` that returns a list of 'key: value' strings for each kwarg. Use list comprehension.",
    lambda: callable(globals().get('show_details')) and globals()['show_details'](a=1, b=2) == ['a: 1', 'b: 2'],
    hint="def show_details(**kwargs):\n    return [f'{k}: {v}' for k, v in kwargs.items()]"
)

# TASK 4
task(
    "Define `full_func(a, b=10, *args, **kwargs)` that returns a tuple: (a, b, args, kwargs).",
    lambda: callable(globals().get('full_func')) and globals()['full_func'](1, 2, 3, 4, x=5) == (1, 2, (3,4), {'x':5}),
    hint="def full_func(a, b=10, *args, **kwargs):\n    return (a, b, args, kwargs)"
)

print("\n" + "="*44)
print("🏆 L‑33 complete – *args & **kwargs")
print("now bend to your will.")
print("="*44)