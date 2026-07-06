# practice_engine.py — Hints & Levels Engine for PyPhone Emperor
# Runs Python code tasks with progressive hints and difficulty levels.

import sys
import traceback

class Level:
    EASY = "Easy"
    MEDIUM = "Medium"
    HARD = "Hard"

class Task:
    def __init__(self, description, verify_func, level=Level.EASY, hints=None):
        self.description = description
        self.verify = verify_func
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
    """Run a single task with retries, hints, and input loop."""
    print("=" * 44)
    print(f"🧱 TASK [{task.level.upper()}]")
    # Wrap description to fit phone screen
    words = task.description.split()
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
    print("-" * 44)

    attempts = 0
    while True:
        attempts += 1
        code = input("  >>> ").strip()
        if code.lower() in ("exit", "quit"):
            print("👋 Practice ended.")
            sys.exit(0)
        if code.lower() == ":hint":
            hint = task.next_hint()
            if hint:
                print(f"  💡 HINT: {hint}")
            else:
                print("  No more hints.")
            continue
        if code.lower() == ":quit":
            print("Exiting task.")
            return False

        # Execute user code in a fresh global namespace (isolated per attempt)
        user_globals = {}
        try:
            exec(code, user_globals)
        except Exception as e:
            print(f"  ❌ Python error: {e}")
            hint = task.next_hint()
            if hint:
                print(f"  💡 HINT: {hint}")
            continue

        # Verify using the task's verify function
        try:
            # Pass the user_globals so verification can check variables
            if task.verify(user_globals):
                print(f"  ✅ Correct! ({attempts} attempt{'s' if attempts != 1 else ''})")
                return True
            else:
                print("  ❌ Not quite. Try again or type :hint for help.")
        except Exception as e:
            print(f"  ❌ Verification error: {e}")
            traceback.print_exc()

def main():
    print("PyPhone practice engine loaded. Use `run_task(task)` to start a task.")

if __name__ == "__main__":
    main()
