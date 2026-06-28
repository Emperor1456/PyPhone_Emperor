# =============================================
#  PyPhone Emperor · Module 4
#  PRACTICE L‑34  –  Local vs Global Scope
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

print("\n🎯 WELCOME TO L‑34 COACHING")
print("Understand where variables live.\n")

# TASK 1 – create a global variable and read it inside a function
task(
    "Create a global variable `x = 'global'`. Then define a function `read_x` that returns the value of `x`. Call it and store the result in `result`.",
    lambda: check_var('result', str, 'global'),
    hint="x = 'global'\ndef read_x():\n    return x\nresult = read_x()"
)

# TASK 2 – shadow a global variable with a local one
task(
    "Define a function `shadow` that creates a local variable `y = 'local'` and returns it. There should also be a global `y = 'global'`. After calling `shadow()`, store the global `y` in `global_y`.",
    lambda: check_var('global_y', str, 'global'),
    hint="y = 'global'\ndef shadow():\n    y = 'local'\n    return y\nshadow()\nglobal_y = y"
)

# TASK 3 – use `global` to modify a global variable
task(
    "Create a global `counter = 0`. Define `increment` that uses `global counter` and adds 1 to it. Call `increment()` twice, then store the final counter in `final_count`.",
    lambda: check_var('final_count', int, 2),
    hint="counter = 0\ndef increment():\n    global counter\n    counter += 1\nincrement()\nincrement()\nfinal_count = counter"
)

# TASK 4 – demonstrate LEGB with nested functions
task(
    "Define `outer` that sets `name = 'enclosing'` and defines an inner function `inner` that sets `name = 'local'` and returns it. Call `outer` and store the returned value in `inner_result`.",
    lambda: check_var('inner_result', str, 'local'),
    hint="def outer():\n    name = 'enclosing'\n    def inner():\n        name = 'local'\n        return name\n    return inner()\ninner_result = outer()"
)

print("\n" + "="*44)
print("🏆 L‑34 complete – Scope")
print("rules are crystal clear.")
print("="*44)