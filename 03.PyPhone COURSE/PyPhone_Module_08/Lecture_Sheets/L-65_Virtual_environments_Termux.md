# 📘 PyPhone Emperor · Module 8
# 📖 L‑65 – Virtual Environments in Termux

---

## 🎯 OBJECTIVE
Learn to create isolated Python environments using
the built‑in `venv` module. Virtual environments let
you install packages per project, avoid dependency
conflicts, and keep your system Python clean. This
is a mandatory skill for any professional developer.

---

## 🧱 BRICK 1 – Why Virtual Environments?

Without a virtual environment, every package you
install with `pip` goes into a global pool. Two
projects that need different versions of the same
package will clash.

### Problems of global installs:
- Project A needs `requests==2.25`, Project B needs `requests==2.28`.
- Upgrading for one project breaks the other.
- Clutters your system with packages not used daily.

Virtual environments solve this by giving each
project its own **isolated Python interpreter** and
its own `site-packages` folder.

---

## 🧱 BRICK 2 – Creating and Using a venv in Termux

### ① Ensure `venv` is available
Termux’s Python usually includes `venv`. If not:
```bash
pkg install python
```

### ② Create a virtual environment
Navigate to your project folder and run:
```bash
python -m venv .venv
```
This creates a folder `.venv` containing a full
isolated Python installation. The name `.venv` is
a convention; you can use any name.

### ③ Activate the environment
```bash
source .venv/bin/activate
```
Your prompt changes to show the environment name:
```
(.venv) ~/project $
```

### ④ Install packages inside it
Now `pip install` goes into the virtual environment:
```bash
pip install requests
```
Check that it's isolated:
```bash
pip list
```

### ⑤ Deactivate when done
```bash
deactivate
```

### Full example session:
```bash
cd ~/my_project
python -m venv .venv
source .venv/bin/activate
pip install pandas
python -c "import pandas; print('Ready')"
deactivate
```

> 💡 **INSIGHT:** Always add `.venv/` to your `.gitignore`
> file. Never commit virtual environments to version control.

---

## 📌 Key Takeaway
- A virtual environment isolates Python and packages per project.
- `python -m venv .venv` creates it; `source .venv/bin/activate` activates.
- Use `pip install` inside it to keep dependencies separated.
- Deactivate with `deactivate`.