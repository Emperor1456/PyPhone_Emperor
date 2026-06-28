# 📱 Complete Phone‑Based Python Setup Guide
**Termux + Acode + Git + GitHub**

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

## 8. Daily Workflow: Write → Run → Commit → Push
### 8.1. Write Code in Acode
- Open Acode → tap the folder icon.
- Navigate to **Termux home** → `PyPhone_Emperor` (you may need to grant Acode access to Termux’s storage via the file manager).
- Inside the appropriate module folder (e.g., `03.PyPhone COURSE/PyPhone_Module_01/Practice_Sheets/`), open a `.py` file or create a new one.
- Type your code, save.

### 8.2. Run Code in Termux
Switch to Termux, navigate to the practice folder:

```bash
cd ~/PyPhone_Emperor/03.PyPhone\ COURSE/PyPhone_Module_01/Practice_Sheets
python L-01_Variables_DataTypes.py
```

### 8.3. Commit and Push to GitHub
After completing a lesson:

```bash
cd ~/PyPhone_Emperor
git add .
git commit -m "Completed L‑01: Variables and Data Types"
git push origin main
```

(If your default branch is `master`, use `git push origin master`.)

---

## 9. Learning Method: Two Bricks at a Time
Each lesson introduces exactly two new concepts. You type the code, run it, understand it, and only then move forward.  
This builds deep, lasting knowledge.

---

## 10. Common Errors & Fixes
- **`fatal: not a git repository`** – Run the command inside `~/PyPhone_Emperor`.
- **`fatal: detected dubious ownership`** – Run the suggested `git config --global --add safe.directory` command.
- **`repository not found`** – Verify the GitHub URL; ensure the repo exists.
- **Push rejected** – If the remote has commits you don’t, use `git push origin main --force` only if you’re sure.
- **`input()` keyboard doesn’t appear** – Tap the Termux screen once to focus.
- **`python: command not found`** – Use `python3` instead, or reinstall `python`.

---

## 11. You’re Ready
Open `PyPhone_Module_01`, start with `Lecture_Sheets/L-01_Variables_DataTypes.md`, then run the matching practice coach.  
Type every line. Commit every lesson. Build your empire.

*Stay consistent. Stay sovereign. Start coding.*  
**— Emperor**