import sys, io, textwrap, traceback

class Level:
    EASY = "Easy"
    MEDIUM = "Medium"
    HARD = "Hard"

class Task:
    def __init__(self, description, expected_output, level=Level.EASY, hints=None):
        self.description = description
        self.expected_output = expected_output.strip()
        self.level = level
        self.hints = hints or []
        self.hint_index = 0

    def next_hint(self):
        if self.hint_index < len(self.hints):
            hint = self.hints[self.hint_index]
            self.hint_index += 1
            return hint
        return None

def run_task(task):
    print("=" * 42)
    print(f"🧱 TASK [{task.level.upper()}]")
    # wrap description at 42 chars
    wrapped = textwrap.fill(task.description, width=42,
                            initial_indent="  📋 ", subsequent_indent="     ")
    print(wrapped)
    print("-" * 42)

    attempts = 0
    while True:
        attempts += 1
        print("\nEnter your code below.")
        print("(Blank line to finish, :hint, :quit)")
        lines = []
        while True:
            raw = input("... " if lines else ">>> ").rstrip('\n')
            if raw.strip().lower() in (":quit", "exit"):
                print("Exiting task.")
                return False
            if raw.strip().lower() == ":hint":
                hint = task.next_hint()
                if hint:
                    print(f"💡 HINT: {hint}")
                else:
                    print("No more hints.")
                continue
            if raw == "":
                break
            lines.append(raw)
        user_code = "\n".join(lines)
        if not user_code.strip():
            print("⚠️ No code entered. Try again.")
            continue

        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        user_globals = {}
        try:
            exec(user_code, user_globals)
            output = sys.stdout.getvalue()
        except Exception as e:
            sys.stdout = old_stdout
            print("❌ Error during execution:")
            traceback.print_exc()
            continue
        finally:
            sys.stdout = old_stdout

        out_stripped = output.strip()
        if out_stripped == task.expected_output:
            print(f"✅ Correct! ({attempts} attempt{'s' if attempts != 1 else ''})")
            return True
        else:
            print("❌ Output mismatch.")
            print("Expected (first 120 chars):")
            print(task.expected_output[:120])
            print("Got (first 120 chars):")
            print(out_stripped[:120])
