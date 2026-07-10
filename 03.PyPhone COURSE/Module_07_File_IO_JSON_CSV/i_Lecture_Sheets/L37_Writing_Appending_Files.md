# 📘 PyPhone Emperor v3.0 · Module 7
# 📖 L‑37 – Writing & Appending – `write`, Context Managers

---

## 🎯 OBJECTIVE — What You Will Master

> Save data to files permanently.

- ✍️ `open(file, 'w')` – write mode (overwrites)
- ➕ `open(file, 'a')` – append mode (adds to end)
- 📝 `.write(str)` – write a string
- 📋 `.writelines(list)` – write multiple strings
- 🔒 **Context manager** – always use `with`

---

## 🧱 WRITING TO A FILE

```python
with open("output.txt", "w") as f:
    f.write("Hello, Emperor!\n")
    f.write("Line 2.\n")
```

`'w'` mode erases existing content immediately.

---

## 🧱 APPENDING TO A FILE

```python
with open("log.txt", "a") as f:
    f.write("New entry\n")
```

`'a'` mode creates the file if it doesn't exist.

---

## 🧱 WRITING MULTIPLE LINES

```python
lines = ["First\n", "Second\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)
```

> ⚠️ **WARNING:** `.writelines()` does **not** add newlines automatically. You must include `\n` yourself.

---

## 💡 Real‑world Usage

**Banking – save transaction summary**
```python
with open("summary.txt", "w") as f:
    f.write(f"Balance: {balance}\n")
```

**E‑commerce – generate order confirmation**
```python
with open("order.txt", "w") as f:
    f.write(f"Order {order_id} confirmed\n")
```

**Logistics – append to shipment log**
```python
with open("shipments.log", "a") as f:
    f.write(f"{tracking_id} shipped\n")
```

---

## 🔍 Practice Preview

| Level | Task |
|-------|------|
| Easy | Write "Emperor" to a file and print its content. |
| Medium | Overwrite the same file with "PyPhone". |
| Hard | Write a list `[1,2,3]` to a file as comma‑separated values, then read and print. |

Run the coach:
```bash
python ii_Practice_Sheets/L37_Writing_Appending_Files.py
```

---

## 📌 Key Takeaway
- `'w'` overwrites; `'a'` appends.
- Always use `with open(...)` for automatic cleanup.
- `.write()` and `.writelines()` are your tools.

*For Emperor.*