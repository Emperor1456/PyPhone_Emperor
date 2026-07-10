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

## 8. Understanding the Course Structure (v3.0)
The entire course lives inside `03.PyPhone COURSE/`.  
Inside, you’ll find:

- `practice_engine.py` – the interactive engine that powers every practice sheet
- `debug_engine.py` – the engine for debugging challenges
- 10 module folders (e.g., `Module_01_Python_Core`)
- Each module contains:
  - `i_Lecture_Sheets/` – Markdown lessons (read in Acode)
  - `ii_Practice_Sheets/` – Python practice coaches (Easy/Medium/Hard)
  - `iii_Debugging_Sheets/` – one broken script per lesson to fix
  - `iv_Review_Sheet/` – final module capstone (`.md` brief + `.py` practice)
  - `v_Solution_Sheets/` – correct code for every practice task
  - `Module_Progress_Tracker.md` – checklist for the module

Root side files: `GETTING_STARTED.md`, `README.md`, `SETUP_GUIDE.md`

---

## 9. The Interactive Practice Engine
Every practice sheet offers:

- **Three difficulty levels:** Easy, Medium, Hard. Choose at the start.
- **Multi‑line input:** write your code, empty line to submit.
- **Live preview:** see your code and its output before submitting.
- **Progressive hints:** Type `:hint` to get a clue.
- **Instant verification:** Your code is executed and checked immediately.
- **Mistake tracking:** the engine shows what you got wrong so you learn.
- **Auto‑progress:** after completing a level, you can continue to the next.

---

## 10. Daily Workflow: Read → Practice → Debug → Review
### 10.1. Read the Lecture
- Open the `.md` file from `i_Lecture_Sheets/` in Acode.

### 10.2. Practice with the Engine
- Switch to Termux, navigate to the module folder:

```bash
cd ~/PyPhone_Emperor/03.PyPhone\ COURSE/Module_01_Python_Core
python ii_Practice_Sheets/L01_Variables_Memory_Typing.py
```

- The engine presents Easy first; after success, you can continue to Medium and Hard.
- Type your Python code.  
  - Use `:hint` if stuck.
  - Use `:quit` to exit early.
- The engine shows a live preview, then you submit with `(s)ubmit`, edit with `(e)dit`, or quit with `(q)uit`.

### 10.3. Debug Broken Code
- After the practice sheet, open the matching file in `iii_Debugging_Sheets/`.
- Run it to see the error, fix the code, and re‑run until the debug engine congratulates you.

### 10.4. Module Review
- Complete the final review challenge in `iv_Review_Sheet/` (run the `.py` file).
- Mark the lesson as complete in the module's `Module_Progress_Tracker.md`.

---

## 11. Commit and Push to GitHub
After completing a lesson or a module:

```bash
cd ~/PyPhone_Emperor
git add .
git commit -m "Completed Module 01 – Python Core"
git push origin main
```

---

## 12. The Capstone – Imperial Contact Book
After you finish all 10 modules, head to  
`Module_10_Capstone/vi_Imperial_Contact_Book/`.  
Build a complete CLI contact book backed by Python and SQLite – your first full‑stack application, and a direct bridge to the SQLPhone course.

---

## 13. Your Diploma
Once the capstone is complete, generate your personalized PyPhone Emperor certificate:

```bash
python generate_certificate.py
```

Answer the prompts. A stunning HTML diploma will open in your browser, and a gold‑coloured terminal version will appear instantly.

---

## 14. Learning Method: One Topic, Total Mastery
Each lesson covers exactly one concept – but to an invincible depth.  
You type the code, understand the mental model, solve the hard tasks, and only then move forward.  
This builds deep, lasting knowledge.

---

## 15. Common Errors & Fixes
- **`fatal: not a git repository`** – Run the command inside `~/PyPhone_Emperor`.
- **`fatal: detected dubious ownership`** – Run the suggested `git config --global --add safe.directory` command.
- **`repository not found`** – Verify the GitHub URL; ensure the repo exists.
- **Push rejected** – If the remote has commits you don’t, use `git push origin main --force` only if you’re sure.
- **`input()` keyboard doesn’t appear** – Tap the Termux screen once to focus.
- **`python: command not found`** – Use `python3` instead, or reinstall `python`.
- **`ModuleNotFoundError: No module named 'practice_engine'`** – Ensure you’re running the practice sheet from its own module folder and that `practice_engine.py` is in `03.PyPhone COURSE/`.

---

## 16. You’re Ready
Open `Module_01_Python_Core`, start with `i_Lecture_Sheets/L01_Variables_Memory_Typing.md`, then run the matching practice coach.  
Type every line. Commit every lesson. Build your empire.

*Stay consistent. Stay sovereign. Start coding.*  
**— Emperor**