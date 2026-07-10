# 📘 PyPhone Emperor v3.0 · Module 7
# 📖 L‑40 – `pathlib` – Modern File Path Handling

---

## 🎯 OBJECTIVE — What You Will Master

> Object‑oriented file paths – cleaner and cross‑platform.

- 📂 `Path` object – represent a file or directory
- 🧹 `.exists()`, `.is_file()`, `.is_dir()` – query properties
- 📖 `.read_text()` / ✍️ `.write_text()` – simple I/O
- 🔍 `.glob()` – find files matching a pattern
- 🧪 `.mkdir()`, `.rename()`, `.unlink()` – file operations

---

## 🧱 CREATING A PATH

```python
from pathlib import Path
data_file = Path("data/config.json")
print(data_file.exists())
print(data_file.suffix)   # .json
```

---

## 🧱 READING & WRITING WITH PATHLIB

```python
content = data_file.read_text()
print(content)

log = Path("app.log")
log.write_text("Application started")
```

---

## 🧱 GLOB – FIND FILES

```python
p = Path(".")
for py_file in p.glob("*.py"):
    print(py_file)
```

---

## 🧱 CREATING DIRECTORIES & FILES

```python
Path("output").mkdir(exist_ok=True)
temp = Path("output/temp.txt")
temp.touch()
temp.rename("output/renamed.txt")
temp.unlink()   # delete
```

---

## 💡 Real‑world Usage

**Banking – archive old statements**
```python
archive = Path("archive")
archive.mkdir(exist_ok=True)
for stmt in Path(".").glob("stmt_*.txt"):
    stmt.rename(archive / stmt.name)
```

**E‑commerce – scan product images**
```python
for img in Path("images").glob("*.png"):
    print(f"Processing {img.name}")
```

**Logistics – verify delivery photos**
```python
proof = Path(f"deliveries/{tracking_id}.jpg")
if proof.exists():
    print("Delivered")
```

---

## 🔍 Practice Preview

| Level | Task |
|-------|------|
| Easy | Create a Path object and check if it exists. |
| Medium | Write text to a file using `.write_text()` and read it back. |
| Hard | List all `.py` files in the current directory using `.glob()`. |

Run the coach:
```bash
python ii_Practice_Sheets/L40_pathlib.py
```

---

## 📌 Key Takeaway
- `pathlib` makes file operations cleaner and cross‑platform.
- Use `Path` objects for reading, writing, and file system queries.
- `.glob()` is ideal for batch operations.

*For Emperor.*