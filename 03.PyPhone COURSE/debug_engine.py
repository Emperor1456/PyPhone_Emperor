import sys, io, textwrap

R = "\033[0m"
G = "\033[32m"
RD = "\033[31m"
Y = "\033[33m"
C = "\033[36m"
M = "\033[35m"
B = "\033[1m"

SEP = "━" * 43

def cprint(msg, color=""):
    print(f"{color}{msg}{R}")

def prompt(msg, color=""):
    return input(f"{color}{msg}{R} ").strip().lower()

def read_multiline():
    lines = []
    first = True
    while True:
        try:
            line = input("... " if not first else ">>> ").rstrip()
        except EOFError:
            break
        first = False
        if line == "":
            break
        lines.append(line)
    return "\n".join(lines)

def capture_exec(code):
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    error = None
    try:
        exec(code, {"__builtins__": __builtins__})
    except Exception as e:
        error = str(e)
    finally:
        output = sys.stdout.getvalue().rstrip("\n")
        sys.stdout = old_stdout
    return output, error

def run_debug(lesson_title, broken_code, expected_output, hints=None):
    if hints is None:
        hints = []
    print("\n" + SEP)
    cprint(f"🐞  DEBUGGING CHALLENGE – {lesson_title}", B)
    print(SEP)
    cprint("Here is the broken code:", M)
    print("─" * 43)
    for line in broken_code.split('\n'):
        print(f"  {line}")
    print("─" * 43)
    cprint("Find the bug and type the corrected code below.", C)
    cprint("(empty line to submit, :hint for a clue)", C)
    hint_idx = 0
    while True:
        print()
        fixed = read_multiline()
        cmd = fixed.strip().lower()
        if cmd in (":quit", "quit", "exit", "q"):
            cprint("⏏️  Debugging ended.", Y)
            return False
        if cmd == ":hint":
            if hint_idx < len(hints):
                cprint(f"💡 Hint {hint_idx+1}: {hints[hint_idx]}", C)
                hint_idx += 1
            else:
                cprint("No more hints.", Y)
            continue
        if not fixed.strip():
            continue
        out, err = capture_exec(fixed)
        if err:
            cprint(f"❌ Python Error: {err}", RD)
            continue
        if out == expected_output:
            cprint("✅  Bug squashed! The code now runs correctly.", G)
            return True
        else:
            cprint("❌  Not quite. The output is still wrong.", RD)
            cprint(f"Expected:\n{expected_output}", G)
            cprint(f"Got:\n{out}", RD)
            continue

if __name__ == "__main__":
    cprint("Debug engine loaded. Import and use run_debug().", C)
