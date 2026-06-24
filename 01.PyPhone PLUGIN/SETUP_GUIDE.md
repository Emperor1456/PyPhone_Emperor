# 📱 Complete Phone‑Based Python Setup Guide
**Termux + Acode + GitHub + DeepSeek AI**

This guide will take you from a bare Android phone to a fully working Python development environment, with Git version control and an AI coding partner.  
You don’t need a laptop, root access, or any prior experience – just your phone, internet, and the willingness to type every line yourself.

---

## Table of Contents
1. [What You Need](#1-what-you-need)
2. [Install Termux](#2-install-termux)
3. [Termux First‑Run Setup](#3-termux-first‑run-setup)
4. [Install Acode Code Editor](#4-install-acode-code-editor)
5. [Create a GitHub Account & Repository](#5-create-a-github-account--repository)
6. [Configure Git in Termux](#6-configure-git-in-termux)
7. [Create Your Project Folder & Link to GitHub](#7-create-your-project-folder--link-to-github)
8. [Daily Workflow: Write → Run → Commit → Push](#8-daily-workflow-write--run--commit--push)
9. [Set Up DeepSeek AI as Your Mentor](#9-set-up-deepseek-ai-as-your-mentor)
10. [Learning Methodology: Two Bricks at a Time](#10-learning-methodology-two-bricks-at-a-time)
11. [Common Errors & How to Fix Them](#11-common-errors--how-to-fix-them)
12. [Next Steps](#12-next-steps)

---

## 1. What You Need
- An Android phone (Android 7+ recommended)
- Stable internet connection
- A free GitHub account ([github.com](https://github.com))
- The will to type everything by hand – no copy/paste!

All tools used in this guide are free and open‑source.

---

## 2. Install Termux
Termux is a terminal emulator and Linux environment that runs directly on Android without root.

**Important:** Do **not** install Termux from the Google Play Store – that version is outdated and buggy. Use the latest version from F‑Droid.

- Open your phone’s browser and go to:  
  `https://f-droid.org/repo/com.termux_118.apk`
- Download and install the APK (you may need to allow “Install from unknown sources” in Settings → Security).
- Once installed, open Termux. You’ll see a black screen with a `$` prompt.

---

## 3. Termux First‑Run Setup
When you first open Termux, it will finish installing the base system automatically. Wait until you see the `$` prompt ready.

Now run these commands **one at a time**, pressing Enter after each:

```bash
pkg update
```

(If asked to continue, type y and press Enter.)

```bash
pkg upgrade
```

Install essential packages:

```bash
pkg install python git -y
```

This installs Python 3 and Git. The -y flag automatically answers “yes” to prompts.

Verify the installations:

```bash
python --version
git --version
```

Both should show version numbers.

Grant storage permission so Termux can access your phone’s shared folders (where you’ll save code):

```bash
termux-setup-storage
```

When a pop‑up appears, tap Allow. This creates a storage folder inside Termux that links to your phone’s internal storage.

---

4. Install Acode Code Editor

Acode is a powerful, free code editor for Android with syntax highlighting and a built‑in file browser.

· Open the Google Play Store and search for Acode.
· Install the app by Foxdebug (or download from F‑Droid if you prefer).
· Open Acode and grant storage permissions when asked.

Acode will be your place to write and save Python files. Termux will be used to run them.

---

5. Create a GitHub Account & Repository

If you already have a GitHub account, skip to step 5.3.

5.1. Sign Up

· Go to https://github.com/signup in your browser.
· Enter a username, email, and password. Choose a username that represents you professionally.

5.2. Create a Personal Access Token (PAT)

GitHub no longer accepts your password for Git operations from the terminal. You must use a token.

· After logging in, tap your avatar (top right) → Settings.
· Scroll down to Developer settings → Personal access tokens → Tokens (classic).
· Tap Generate new token → Generate new token (classic).
· Give it a note like “Termux phone”.
· Under Select scopes, check the box for repo (this gives full control of your repositories).
· Scroll down and tap Generate token.
· Copy the token immediately – you won’t see it again. Save it in a secure note (like a Notion page). You’ll use this instead of a password.

5.3. Create a New Repository

· On GitHub, tap the + icon (top right) → New repository.
· Give it a name, for example my-python-journey.
· Choose Public (or Private if you prefer).
· Do not check “Add a README” – we will push our own files.
· Tap Create repository.
· After creation, copy the repository URL. It will look like:
    https://github.com/your-username/my-python-journey.git

---

6. Configure Git in Termux

Now we tell Git who you are and how to remember your token.

In Termux, set your name and email (use the same email as your GitHub account):

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

Set Git to store your credentials so you don’t have to enter the token every time:

```bash
git config --global credential.helper store
```

The first time you push, Git will ask for your username and password.

· Username: your GitHub username (e.g., Emperor1456)
· Password: paste the personal access token you created earlier

After that, Git will remember it.

---

7. Create Your Project Folder & Link to GitHub

Choose a location for your Python projects. We’ll use the phone’s Download folder because it’s easy to access from both Acode and Termux.

In Termux, navigate to your shared storage:

```bash
cd /storage/emulated/0/Download
```

Create a new folder for your Python course and enter it:

```bash
mkdir my-python-course
cd my-python-course
```

Initialize a Git repository:

```bash
git init
```

Add your GitHub remote (replace the URL with the one you copied from step 5.3):

```bash
git remote add origin https://github.com/your-username/my-python-journey.git
```

Now your local folder is connected to GitHub. We’ll push the first file in the next section.

---

8. Daily Workflow: Write → Run → Commit → Push

This is the cycle you’ll repeat every single day.

8.1. Write Code in Acode

· Open Acode.
· Tap the folder icon (top left) and navigate to:
    Internal Storage → Download → my-python-course
· Tap the + button to create a new file (e.g., lesson01.py).
· Type your Python code.
· Save the file (checkmark icon).

8.2. Run the Code in Termux

· Switch back to Termux.
· Ensure you’re in the correct folder:
  ```bash
  cd /storage/emulated/0/Download/my-python-course
  ```
· Run your file with:
  ```bash
  python lesson01.py
  ```
  Tip: When input() is used, tap the Termux screen to bring up the keyboard and enter your input.

8.3. Commit and Push to GitHub

After you’ve completed a lesson and the code runs correctly:

```bash
git add lesson01.py
git commit -m "Lesson 01: Variables and Data Types"
git push origin main
```

If your branch is master instead of main, use git push origin master.
The first push will ask for username and token – enter them as described in section 6.

Check GitHub – your file should now appear.

Repeat this cycle for every lesson. Over time, you can add multiple files with git add . (but be careful not to push any secret files).

---

9. Set Up DeepSeek AI as Your Mentor

DeepSeek is a powerful, free AI assistant you can use for guided Python learning. We’ll use the provided curriculum prompt to turn it into a personal mentor.

9.1. Get the AI Prompt

Inside the PyPhone repository (or any source), you’ll find a file called Python_Curriculum_[Ai_Prompt].md. This file contains a complete prompt that transforms the AI into a two‑bricks‑at‑a‑time Python teacher.

· Open that file in Acode or any text viewer and copy the entire content.

9.2. Start a New Conversation

· Open the DeepSeek website or app: https://chat.deepseek.com/
· Create a new conversation.
· Paste the entire prompt as your first message.
· The AI will immediately assume the role of your Python mentor and begin guiding you through the syllabus.

9.3. Follow Along

When the AI asks you to write a new lesson file, do it in Acode, run it in Termux, push it, and then reply “Next” or “Done” as instructed. The AI will wait for you, and never jump ahead.

---

10. Learning Methodology: Two Bricks at a Time

The entire curriculum uses a method called “two bricks at a time”:

· Each lesson introduces exactly two new concepts (no more, no less).
· You get a tiny practice task that uses both concepts.
· You type the code, run it, understand it, and only then move forward.

This prevents overwhelm and ensures you truly internalize every idea.
Never rush – understanding > speed.

---

11. Common Errors & How to Fix Them

11.1. fatal: not a git repository

You ran a Git command outside your project folder.
Fix: navigate to your project folder first with cd.

11.2. fatal: detected dubious ownership...

Git doesn’t trust the folder because of Android’s storage permissions.
Run the command it suggests:

```bash
git config --global --add safe.directory /storage/emulated/0/Download/my-python-course
```

11.3. remote: Repository not found

The GitHub URL is incorrect or the repo doesn’t exist yet.
Fix: double‑check the URL, or create the repo on GitHub first. Use git remote set-url origin <correct-url> to fix it.

11.4. error: failed to push... (rejected)

The remote repository has commits that you don’t have locally. This often happens if you created a README or LICENSE on GitHub directly.
If you’re sure your local code is correct and you don’t need the remote content, use force push:

```bash
git push origin main --force
```

Use force push only when necessary.

11.5. Python input() doesn’t work (keyboard won’t appear)

In Termux, tap the black screen area once to focus the terminal. The keyboard should appear.

11.6. “command not found” when running python

You may need to use python3 instead. Try:

```bash
python3 lesson01.py
```

If that works, you can create an alias or just stick to python3.

---

12. Next Steps

· Start with Lesson 01 of your Python curriculum. Open the corresponding .py file (or create it) and follow the AI mentor’s instructions.
· After each lesson, commit and push.
· As you progress, explore the README.md, Python_Curriculum.md, and GETTING_STARTED.md files in the PyPhone repo for a full overview.
· Join the open‑source community around the course: open issues, share your progress, and help others who are just starting.

---

You now have everything a beginner needs – no laptop required.
Stay consistent. Stay sovereign. Start coding right now !!