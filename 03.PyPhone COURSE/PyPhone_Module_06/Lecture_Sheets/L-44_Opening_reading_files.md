# 📘 PyPhone Emperor · Module 6
# 📖 L‑44 – Opening & Reading Files

---

## 🎯 OBJECTIVE
Learn to read data from files on disk using Python's
built‑in `open()` function and the `with` statement.
This is the gateway to processing logs, configuration,
and any persistent data storage.

---

## 🧱 BRICK 1 – Opening a File with `open()`

`open(filename, mode)` returns a file object.
The most common mode is `'r'` for reading (default).

```python
f = open("data.txt", "r")   # open for reading
content = f.read()          # read entire file as a string
f.close()                   # always close when done
```

**Reading methods:**
- `.read()` – whole file as one string
- `.readline()` – read next line (including `\n`)
- `.readlines()` – list of all lines

```python
f = open("data.txt", "r")
first_line = f.readline()
all_lines = f.readlines()
f.close()
```

> ⚠️ **WARNING:** Always call `.close()`. If your program
> crashes before `close()`, the file may stay locked.

---

## 🧱 BRICK 2 – The `with` Statement (Safe Mode)

`with open(...) as f:` automatically closes the file
when the indented block finishes, even if an error occurs.

```python
with open("data.txt", "r") as f:
    content = f.read()
# file is automatically closed here
```

**Iterate over lines efficiently:**
```python
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())   # .strip() removes \n
```

**Example – read configuration:**
```python
config = {}
with open("config.ini", "r") as f:
    for line in f:
        if "=" in line:
            key, val = line.strip().split("=")
            config[key.strip()] = val.strip()
```

> 💡 **INSIGHT:** `with open(...)` is the industry standard
> for file handling. It eliminates resource leaks.

---

## 📌 Key Takeaway
- `open("file", "r")` returns a file object for reading.
- `.read()`, `.readline()`, `.readlines()` get the content.
- `with open(...) as f:` automatically closes the file.
- Always use `with` to prevent resource leaks.