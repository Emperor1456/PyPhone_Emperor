# Getting Started with PyPhone Emperor

Welcome. This guide will help you navigate the complete Python foundation course.  
No prior experience needed — just dedication and a phone.

---

## 1. The Course at a Glance

The curriculum contains **8 modules** and **66 lessons**.  
Every lesson now includes four resources, organised in Roman‑numeral order:

- **i_Lecture_Sheets/** – the concept, explained clearly.
- **ii_Practice_Sheets/** – an interactive coach with Easy/Medium/Hard levels and hints.
- **iii_Debugging_Sheets/** – three broken Python files that train your debugging eye.
- **iv_Review_Sheets/** – a final consolidation task for the whole module.

All lessons live inside the folder `03.PyPhone COURSE/`.

---

## 2. How to Progress

1. Open any module (e.g., `PyPhone_Module_01`).
2. Read the **Progress_Tracker.md** to see the checklist.
3. Start with the first lecture sheet inside `i_Lecture_Sheets/`.
4. Once you understand the ideas, open the matching practice sheet inside `ii_Practice_Sheets/` and run it in Termux:
   ```bash
   cd "03.PyPhone COURSE/PyPhone_Module_01"
   python ii_Practice_Sheets/L-01_Variables_Data_Types.py
   ```
5. Choose a difficulty: **1 Easy**, **2 Medium**, or **3 Hard**.
6. Type your Python code. The engine checks your answer instantly.
   - Stuck? Type `:hint` for a clue.
   - Want to exit? Type `:quit`.
7. After completing all lessons, fix the three broken scripts in `iii_Debugging_Sheets/`.
8. Finish with the final review in `iv_Review_Sheets/` to lock in the knowledge.
9. Move to the next module only when the Progress Tracker is fully checked.

---

## 3. Folder Structure (Simplified)

```
03.PyPhone COURSE/
├── practice_engine.py          ← the engine that powers every practice sheet
├── PyPhone_Module_01/
│   ├── Progress_Tracker.md
│   ├── i_Lecture_Sheets/
│   ├── ii_Practice_Sheets/
│   ├── iii_Debugging_Sheets/
│   └── iv_Review_Sheets/
├── PyPhone_Module_02/
...
└── PyPhone_Module_08/
```

The same structure repeats for every module.

---

## 4. Tools You Need

- **Termux** (terminal) – to run Python files.
- **Acode** (editor) – to read lecture sheets and write code.
- **Git** – to track your progress (optional but recommended).

Setup instructions are in `SETUP_GUIDE.md` inside `01.PyPhone PLUGIN/`.

---

## 5. The Practice Engine

Every practice sheet now uses a central **practice engine** (`practice_engine.py`) that:
- Offers three difficulty levels per task.
- Provides progressive hints on demand.
- Executes your code in a sandbox and gives instant pass/fail feedback.
- Works completely offline, no internet required.

A full guide to the engine is in `01.PyPhone PLUGIN/PRACTICE_ENGINE_GUIDE.md`.

---

## 6. Cheat Sheets & Notes

- **04.PyPhone NOTES/** contains a one‑page cheat sheet for each module.
- Use them for quick revision before interviews or practice.

---

## 7. The Capstone – Imperial Finance

After you conquer all 8 modules, head to `05.Final Capstone/`.  
There you’ll find the project brief and a starter script.  
Build a complete CLI personal finance tracker that integrates everything you’ve learned.  
It’s your portfolio centerpiece.

---

## 8. Your Diploma

When the capstone is done, generate your official PyPhone Emperor certificate:

```bash
python generate_certificate.py
```

Answer the prompts and a `GRADUATION.md` file will be created. Open it in Acode’s preview to see your name in gold.

---

## 9. The Golden Rule

Type every line yourself.  
Never copy‑paste.  
Understanding comes from your fingers, not from reading alone.

---

*Built entirely on a phone by Emperor.*  
*Stay consistent. Stay sovereign. Finish what you start.*