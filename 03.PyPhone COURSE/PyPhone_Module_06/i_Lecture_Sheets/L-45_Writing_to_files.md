# 📘 PyPhone Emperor · Module 6
# 📖 L‑45 – Writing to Files

---

## 🎯 OBJECTIVE
Learn to write data to files using Python.
You'll overwrite existing content with `'w'` mode
or create entirely new files.
This is how programs save results, logs,
and user-generated data permanently.

---

## 🧱 BRICK 1 – Opening a File for Writing

Open a file with mode `'w'`. If the file exists,
its contents are **erased immediately**.
If it doesn't exist, a new file is created.

```python
with open("output.txt", "w") as f:
    f.write("Hello, Emperor!\n")
    f.write("This is line 2.\n")
```

**Writing methods:**
- `.write(str)` – writes a single string
- `.writelines(list)` – writes a list of strings

```python
lines = ["First line\n", "Second line\n", "Third line\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)
```

> ⚠️ **WARNING:** `'w'` mode destroys previous content
> silently. Use it only when you want a fresh file.

---

## 🧱 BRICK 2 – Real‑world Writing Patterns

**① Saving user data:**
```python
username = "Emperor"
score = 1500
with open("savegame.txt", "w") as f:
    f.write(f"player={username}\n")
    f.write(f"highscore={score}\n")
```

**② Generating reports:**
```python
sales = {"Jan": 4500, "Feb": 5200, "Mar": 6100}
with open("report.csv", "w") as f:
    f.write("Month,Sales\n")
    for month, amount in sales.items():
        f.write(f"{month},{amount}\n")
```

**③ Logging events:**
```python
from datetime import datetime
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("app.log", "w") as f:
    f.write(f"[{timestamp}] Application started\n")
```

> 💡 **INSIGHT:** Files are buffered — data may not
> appear on disk until the `with` block exits or
> you call `.flush()`.

---

## 📌 Key Takeaway
- `open("file", "w")` opens for writing (erases existing content).
- `.write()` writes a string; `.writelines()` writes a list.
- Always use `with open(...)` to ensure the file closes.
- Write logs, reports, and user data to persistent storage.