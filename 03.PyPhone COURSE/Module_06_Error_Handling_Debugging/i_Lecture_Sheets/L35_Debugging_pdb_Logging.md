# 📘 PyPhone Emperor v3.0 · Module 6
# 📖 L‑35 – Debugging with `pdb` & Logging

---

## 🎯 OBJECTIVE — What You Will Master

> Professional debugging tools beyond `print()`.

- 🐞 **`pdb`** – Python Debugger, interactive debugging
- 📋 **`logging` module** – configurable, leveled logging
- 🧪 **Breakpoints** – pause execution, inspect variables
- 🛠️ **Basic commands** – `n` (next), `s` (step), `c` (continue), `q` (quit)

---

## 🧱 USING `pdb`

```python
import pdb

def calculate(x, y):
    pdb.set_trace()   # execution pauses here
    result = x / y
    return result

calculate(10, 0)
```

Inside the debugger:
- `p` variable – print value
- `n` – next line
- `s` – step into function
- `c` – continue execution
- `q` – quit

---

## 🧱 LOGGING LEVELS

```python
import logging

logging.basicConfig(level=logging.INFO)
logging.debug("Debug info")      # not shown
logging.info("Program started")  # shown
logging.warning("Low disk space")
logging.error("File not found")
logging.critical("System down")
```

Levels: DEBUG < INFO < WARNING < ERROR < CRITICAL.

---

## 💡 Real‑world Usage

**Banking – log transactions**
```python
logging.info(f"Processing payment of {amount}")
```

**E‑commerce – debug checkout**
```python
pdb.set_trace()   # inspect cart before checkout
```

**Logistics – log delivery status**
```python
logging.error(f"Delivery failed for {tracking_id}")
```

---

## 🔍 Practice Preview

| Level | Task |
|-------|------|
| Easy | Use `assert` to verify `1+1==2` and print "pass". |
| Medium | Define a test function with `assert` and call it. |
| Hard | Create a unittest test case with a simple assertion. |

Run the coach:
```bash
python ii_Practice_Sheets/L35_Debugging_pdb_Logging.py
```

---

## 📌 Key Takeaway
- `pdb` lets you step through code interactively.
- `logging` is superior to `print()` for production.
- Use `DEBUG` for development, `INFO`/`WARNING` for production.

*For Emperor.*