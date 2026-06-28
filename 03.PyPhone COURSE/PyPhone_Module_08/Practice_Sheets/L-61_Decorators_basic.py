# =============================================
#  PyPhone Emperor · Module 8
#  PRACTICE L‑61  –  Decorators (Basic)
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

print("\n🎯 WELCOME TO L‑61 COACHING")
print("Wrap functions with decorators.\n")

# TASK 1
task(
    "Define a function `make_multiplier(factor)` that returns a function `multiplier(x)` which returns `x * factor`. Then create `triple = make_multiplier(3)`. Store `triple(7)` in `result`.",
    lambda: check_var('result', int, 21),
    hint="def make_multiplier(factor):\n    def multiplier(x):\n        return x * factor\n    return multiplier\n\ntriple = make_multiplier(3)\nresult = triple(7)"
)

# TASK 2
task(
    "Write a decorator `logger(func)` that prints 'Calling' before and 'Returned' after, then returns the original result. Apply it to a function `add(a,b)` that returns a+b. Call `add(2,3)` and store the returned value in `r`.",
    lambda: check_var('r', int, 5),
    hint="def logger(func):\n    def wrapper(*args, **kwargs):\n        print('Calling')\n        r = func(*args, **kwargs)\n        print('Returned')\n        return r\n    return wrapper\n\n@logger\ndef add(a,b):\n    return a+b\n\nr = add(2,3)"
)

# TASK 3
task(
    "Write a decorator `uppercase` that wraps a function returning a string and converts the result to uppercase. Apply it to a function `greet()` that returns 'hello'. Store `greet()` in `msg`.",
    lambda: check_var('msg', str, 'HELLO'),
    hint="def uppercase(func):\n    def wrapper():\n        return func().upper()\n    return wrapper\n\n@uppercase\ndef greet():\n    return 'hello'\n\nmsg = greet()"
)

print("\n" + "="*44)
print("🏆 L‑61 complete – Decorators")
print("wrap your logic elegantly.")
print("="*44)