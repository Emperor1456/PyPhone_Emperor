# 📘 PyPhone Emperor · Module 8  
# 📖 L‑65 – Virtual Environments in Termux (Isolation for Professional Projects)

---

## 🎯 OBJECTIVE  
Master virtual environments (`venv`) to isolate project dependencies.  
This prevents version conflicts, keeps your system Python clean, and mirrors real‑world development workflows — right on your phone in Termux.

---

## 🧱 BRICK 1 – Understanding Isolation

Without a virtual environment, all `pip install` commands go to a global location. Two projects needing different versions of the same package will conflict.

A virtual environment gives each project its own Python interpreter and its own library folder. Activating it changes your shell’s path so that `python` and `pip` point to that isolated copy.

---

## 🧱 BRICK 2 – Creating and Using a venv in Termux

**① Check Python location (Easy practice)**
```python
import sys
print(sys.executable)
```
This prints the full path to the Python interpreter. Inside a venv, this path will change to the environment's `bin/python`.

**② Creating a venv (Medium practice)**
```bash
python -m venv myenv
```
The command is `python -m venv myenv`. The Medium task expects you to print this exact command string.

**③ Activating the venv (Hard practice)**
```bash
source myenv/bin/activate
```
After activation, your prompt shows `(myenv)`, and `pip list` shows only packages installed in that environment. To exit, type `deactivate`.

The Hard task expects you to print the activation command.

**④ Full workflow example**
```bash
cd ~/my_project
python -m venv .venv
source .venv/bin/activate
pip install pandas
python -c "import pandas; print('Ready')"
deactivate
```

> 💡 **INSIGHT:** Always add `.venv/` (or your environment folder) to `.gitignore` — never commit it to version control.

> ⚠️ **WARNING:** Do not move or rename the venv folder after creation. Paths inside the environment are hardcoded.

> 💡 **ADVANCED TIP:** Use `pip freeze > requirements.txt` to capture dependencies, and `pip install -r requirements.txt` to recreate the environment on another machine.

---

## 💡 Real‑world Usage

**Banking app – isolate versions**
```bash
cd banking_project
python -m venv .venv && source .venv/bin/activate
pip install requests==2.25.1
```

**E‑commerce – separate environments for different services**
```bash
cd shop_service && python -m venv .venv && source .venv/bin/activate
cd ../inventory_service && python -m venv .venv && source .venv/bin/activate
```

**Logistics – recreate from requirements**
```bash
source .venv/bin/activate
pip install -r requirements.txt
```

**HR – check environment isolation**
```bash
source .venv/bin/activate
which python   # should point to .venv/bin/python
pip list       # only packages in this environment
```

---

## 🔍 Practice Preview
These tasks simulate the knowledge needed to create and activate a venv in Termux.

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | Print the current Python executable path using `sys.executable`. | (your path) |
| Medium | Print the command to create a virtual environment: `'python -m venv myenv'`. | `python -m venv myenv` |
| Hard   | Print the activation command for a virtual environment: `'source myenv/bin/activate'`. | `source myenv/bin/activate` |

Run the coach:
```bash
python ii_Practice_Sheets/L-65_Virtual_Environments.py
```

---

## 📌 Key Takeaway
- `python -m venv name` creates an isolated Python environment.
- `source name/bin/activate` activates it; `deactivate` exits.
- Always activate the venv before installing or running project code.
- Keep venvs out of version control; use `requirements.txt` for reproducibility.