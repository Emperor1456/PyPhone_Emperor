# 📘 PyPhone Emperor v3.0 · Module 9
# 📖 L‑50 – Virtual Environments & `pip freeze`

---

## 🎯 OBJECTIVE — What You Will Master

> Isolate project dependencies like a professional.

- 🧪 **Virtual environment** – an isolated Python installation
- 🛠️ **`venv`** – built‑in module to create environments
- 📋 **`pip freeze`** – capture exact package versions
- 📄 **`requirements.txt`** – reproduce environments anywhere

---

## 🧱 CREATING A VIRTUAL ENVIRONMENT

```bash
python -m venv myenv
source myenv/bin/activate   # Linux/macOS (Termux)
myenv\Scripts\activate      # Windows
```

Once activated, your prompt changes and `pip` installs packages locally.

---

## 🧱 INSTALLING PACKAGES & FREEZING

```bash
pip install requests
pip freeze > requirements.txt
```

The `requirements.txt` file lists all installed packages with versions.

---

## 🧱 RECREATING AN ENVIRONMENT

```bash
python -m venv fresh_env
source fresh_env/bin/activate
pip install -r requirements.txt
```

Now the new environment is identical to the original.

---

## 💡 Real‑world Usage

**Banking – isolate backend dependencies**
```bash
cd banking_service && python -m venv .venv && source .venv/bin/activate
```

**E‑commerce – separate services**
```bash
cd shop_service && python -m venv .venv && source .venv/bin/activate
cd ../inventory_service && python -m venv .venv && source .venv/bin/activate
```

**Logistics – deploy to production**
```bash
git clone repo && cd repo && python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
```

---

## 🔍 Practice Preview

| Level | Task |
|-------|------|
| Easy | Print the command to create a virtual environment. |
| Medium | Print the activation command. |
| Hard | Print the command to freeze installed packages. |

Run the coach:
```bash
python ii_Practice_Sheets/L50_Virtual_Environments_pip_freeze.py
```

---

## 📌 Key Takeaway
- Virtual environments prevent dependency conflicts.
- Use `pip freeze > requirements.txt` to lock versions.
- Always activate the environment before working on a project.

*For Emperor.*