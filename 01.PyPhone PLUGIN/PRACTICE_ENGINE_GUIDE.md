# 🧠 PyPhone Emperor – Practice Engine Guide

## What It Is
The practice engine (`practice_engine.py`) is the interactive core of every PyPhone practice sheet. It transforms a static `.py` file into a smart, three‑level challenge system that runs entirely offline in Termux.

## How It Works
1. You run a practice sheet in Termux:
   ```bash
   python ii_Practice_Sheets/L-01_Variables_Data_Types.py
   ```
2. The engine asks you to choose a difficulty: **Easy**, **Medium**, or **Hard**.
3. It shows the task description and waits for your Python code input.
4. After you type your code and press Enter, the engine executes it in a safe, isolated global namespace.
5. A verification function checks your code (e.g., does the correct variable exist? Does it have the right value?).
6. If correct → `✅ Correct!` and the task ends.
7. If wrong → `❌ Try again.` You can retry, ask for a hint (`:hint`), or quit (`:quit`).

## Special Commands
- `:hint` – reveals the next progressive clue (up to 3 per task).
- `:quit` – exits the task without completing it.
- `exit` or `quit` (typed as code) – ends the entire practice session.

## Difficulty Levels
- **Easy** – mirror the exact pattern from the lecture sheet.
  *Goal: build confidence and muscle memory.*
- **Medium** – apply the same concept with a twist (e.g., different variable names, extra conditions).
  *Goal: demonstrate understanding, not just copying.*
- **Hard** – solve a novel problem that combines multiple concepts.
  *Goal: prove mastery and prepare for real‑world coding.*

## The Hints System
Each task has a list of hints ordered from general to specific.
- Hint 1: gentle nudge in the right direction.
- Hint 2: more concrete clue (e.g., function name or syntax).
- Hint 3: near‑solution (still requires you to type it correctly).

Hints are revealed one at a time only when you explicitly request them with `:hint`. This prevents accidental spoilers and encourages genuine problem‑solving.

## The Verification Function
Every task has a custom `verify(globals_dict)` function that checks:
- Existence of required variables.
- Their types (int, float, str, list, callable function, etc.).
- Their exact values or computed results.
- In more advanced tasks, the existence and correctness of classes or functions.

The verification logic is strict — your output must match the expected result precisely.

## Why It Makes PyPhone Emperor Elite
- **Zero internet required** – runs entirely in Termux.
- **Instant feedback** – no waiting for a grader.
- **Safe sandbox** – your code is executed in an isolated namespace; nothing is saved to disk.
- **Adaptive difficulty** – you choose the level that matches your current skill.
- **Progressive hints** – you learn to problem‑solve, not just copy answers.
- **Deliberate practice** – every task is designed to build a specific skill.

## The Engine File
The engine file is `practice_engine.py`, located in `03.PyPhone COURSE/`. All practice sheets import it with:
```python
from practice_engine import Task, Level, run_task
```

## Tips for Best Use
- Always start with Easy if the concept is new.
- Use Medium to solidify; Hard to prove mastery.
- Don’t overuse hints – struggle builds long‑term memory.
- After completing a module, re‑run Hard tasks from earlier modules as spaced repetition.
- If the engine reports `ModuleNotFoundError`, make sure you’re running the practice sheet from the module folder and that `practice_engine.py` is in the course root.

*The engine doesn’t teach you Python. It makes you unbeatable at it.*