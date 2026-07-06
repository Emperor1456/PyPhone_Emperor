# 📘 PyPhone Emperor · Module 6
# 📖 L‑46 – Appending to Files

---

## 🎯 OBJECTIVE
Learn to add new data to the end of an existing file
without erasing its current contents.
Appending is essential for logs, audit trails,
and any time you need to preserve history.

---

## 🧱 BRICK 1 – Opening a File for Appending

Open a file with mode `'a'` (append).
If the file doesn’t exist, it’s created.
If it exists, new data is written **after** the last byte.

```python
with open("log.txt", "a") as f:
    f.write("New entry\n")
```

You can also append multiple lines:
```python
new_entries = ["event1\n", "event2\n"]
with open("log.txt", "a") as f:
    f.writelines(new_entries)
```

> 💡 **INSIGHT:** `'a'` mode always writes to the end,
> regardless of where the file pointer currently sits.

---

## 🧱 BRICK 2 – Real‑world Append Patterns

**① Application logging:**
```python
from datetime import datetime
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("app.log", "a") as f:
    f.write(f"[{timestamp}] User logged in\n")
```

**② Audit trail:**
```python
def record_transaction(user, amount):
    with open("transactions.txt", "a") as f:
        f.write(f"{user} deposited {amount}\n")

record_transaction("Emperor", 500)
record_transaction("Emperor", 200)
```

**③ Data collection over time:**
```python
# Sensor reading
temperature = 22.5
with open("temperatures.txt", "a") as f:
    f.write(f"{temperature}\n")
```

> ⚠️ **WARNING:** `'a'` mode cannot read or modify
> existing content — it is write‑only. To update a
> specific line, you must rewrite the whole file.

---

## 📌 Key Takeaway
- `open("file", "a")` opens for appending without erasing.
- `.write()` and `.writelines()` add data to the end.
- Perfect for logs, audit trails, and incremental data.
- Use `with open(...)` for automatic close.