# 📱 Complete Phone‑Based Python Setup Guide
**Termux + Acode + Git + GitHub + Interactive Practice Engine**

Turn your Android phone into a complete Python development environment.  
No laptop required. All tools are free and open‑source.

---

## 1. What You Need
- Android phone (Android 7+ recommended)
- Internet connection
- GitHub account (free)
- Willingness to type every line yourself — no copy‑paste

---

## 2. Install Termux
Termux is a terminal emulator that gives you a full Linux environment.

- **Do not** install from Google Play Store (outdated).
- Download the latest APK from F‑Droid:  
  `https://f-droid.org/repo/com.termux_118.apk`
- Allow installation from unknown sources if prompted.
- Open Termux. Wait for the base system to install until you see the `$` prompt.

---

## 3. Termux First‑Run Setup
Run these commands one at a time:

```bash
pkg update
pkg upgrade
```

Install Python and Git:

```bash
pkg install python git -y
```

Verify:

```bash
python --version
git --version
```

Grant storage access (required to share files with other apps):

```bash
termux-setup-storage
```
Tap **Allow** on the pop‑up.

---

## 4. Install Acode Code Editor
Acode is a powerful Android code editor with syntax highlighting and a built‑in file explorer.

- Install **Acode** from the Play Store (by Foxdebug).
- Grant storage permissions when asked.

---

## 5. GitHub Setup
### 5.1. Create an Account
If you don’t have one, sign up at [github.com](https://github.com).

### 5.2. Create a Personal Access Token (PAT)
GitHub requires a token instead of a password for Git operations.

- Log in, go to **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)**.
- Generate a new token (classic) with the **repo** scope.
- Copy the token immediately and store it securely.

### 5.3. Create a Repository
- Tap **+** → **New repository**.
- Name it (e.g., `PyPhone_Emperor`).
- Choose **Public** or **Private**.
- Do **not** initialise with README.
- Copy the repository URL (e.g., `https://github.com/your‑username/PyPhone_Emperor.git`).

---

## 6. Configure Git in Termux
Set your identity:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

Enable credential storage:

```bash
git config --global credential.helper store
```

The first time you push, Git will ask for your username and the token you saved earlier. After that, it remembers them.

---

## 7. Clone the Course Repository
Instead of manually creating folders, clone the existing PyPhone_Emperor repository directly into Termux’s private home:

```bash
cd ~
git clone https://github.com/your-username/PyPhone_Emperor.git
cd PyPhone_Emperor
```

All course materials are now inside `~/PyPhone_Emperor/`.

---

## 8. Understanding the New Course Structure (v2.0)
Inside each module folder (e.g., `03.PyPhone COURSE/PyPhone_Module_01/`) you will find:

- **`i_Lecture_Sheets/`** – Markdown lesson files (read in Acode).
- **`ii_Practice_Sheets/`** – Python practice coaches powered by the **interactive engine**.
- **`iii_Debugging_Sheets/`** – Three broken Python scripts per module that you must fix.
- **`iv_Review_Sheets/`** – A final review task to lock in the whole module.

The engine file **`practice_engine.py`** lives in `03.PyPhone COURSE/` and is used by every practice sheet automatically.

---

## 9. The Interactive Practice Engine
Every practice sheet now offers:

- **Three difficulty levels:** Easy, Medium, Hard. Choose at the start.
- **Progressive hints:** Type `:hint` at any time to get a clue.
- **Instant verification:** Your code is executed and checked immediately.
- **Sandbox safety:** Each run is isolated – no risk to your files.

A full guide is available in `01.PyPhone PLUGIN/PRACTICE_ENGINE_GUIDE.md`.

---

## 10. Daily Workflow: Read → Practice → Debug → Review
### 10.1. Read the Lecture
- Open the `.md` file from `i_Lecture_Sheets/` in Acode.

### 10.2. Practice with the Engine
- Switch to Termux, navigate to the module folder:

```bash
cd ~/PyPhone_Emperor/03.PyPhone\ COURSE/PyPhone_Module_01
python ii_Practice_Sheets/L-01_Variables_Data_Types.py
```

- Choose a level (1‑3).
- Type your Python code.  
  - Use `:hint` if stuck.
  - Use `:quit` to exit early.
- The engine will tell you ✅ or ❌ immediately.

### 10.3. Debug Broken Code
- After finishing all practice sheets, open the files in `iii_Debugging_Sheets/`.
- Each contains a deliberate mistake. Find the error, fix it, and run the corrected script.

### 10.4. Module Review
- Complete the final review challenge in `iv_Review_Sheets/` (re‑run the Hard levels without hints).
- Mark the `Progress_Tracker.md` in the module root as complete.

---

## 11. Commit and Push to GitHub
After completing a lesson or a module:

```bash
cd ~/PyPhone_Emperor
git add .
git commit -m "Completed Module 01 – Python Fundamentals"
git push origin main
```

---

## 12. The Capstone – Imperial Finance
After you finish all 8 modules, head to `05.Final Capstone/`.  
You’ll find the project brief (`IMPERIAL_FINANCE_BRIEF.md`) and a starter script (`imperial_finance.py`).  
Build a complete CLI personal finance tracker that integrates every skill from the course.

---

## 13. Your Diploma
Once the capstone is complete, generate your personalized PyPhone Emperor certificate:

```bash
python generate_certificate.py
```

Answer the prompts and a `GRADUATION.md` file will be created. Open it in Acode’s preview to see your name in gold.

---

## 14. Learning Method: Two Bricks at a Time
Each lesson introduces exactly two new concepts. You type the code, run it, understand it, and only then move forward.  
This builds deep, lasting knowledge.

---

## 15. Common Errors & Fixes
- **`fatal: not a git repository`** – Run the command inside `~/PyPhone_Emperor`.
- **`fatal: detected dubious ownership`** – Run the suggested `git config --global --add safe.directory` command.
- **`repository not found`** – Verify the GitHub URL; ensure the repo exists.
- **Push rejected** – If the remote has commits you don’t, use `git push origin main --force` only if you’re sure.
- **`input()` keyboard doesn’t appear** – Tap the Termux screen once to focus.
- **`python: command not found`** – Use `python3` instead, or reinstall `python`.
- **`ModuleNotFoundError: No module named 'practice_engine'`** – Ensure you’re running the practice sheet from the module folder (e.g., `PyPhone_Module_01`) and that `practice_engine.py` is in `03.PyPhone COURSE/`.

---

## 16. You’re Ready
Open `PyPhone_Module_01`, start with `i_Lecture_Sheets/L-01_Variables_Data_Types.md`, then run the matching practice coach.  
Type every line. Commit every lesson. Build your empire.

*Stay consistent. Stay sovereign. Start coding.*  
**— Emperor**