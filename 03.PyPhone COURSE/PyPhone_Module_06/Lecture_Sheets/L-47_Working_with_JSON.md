# 📘 PyPhone Emperor · Module 6
# 📖 L‑47 – Working with JSON

---

## 🎯 OBJECTIVE
Learn to read and write **JSON** (JavaScript Object Notation),
the universal data‑exchange format. Python’s `json` module
converts dictionaries ↔ JSON strings and files seamlessly,
making it essential for APIs, config files, and storage.

---

## 🧱 BRICK 1 – Writing JSON (`json.dump`)

Python dictionary → JSON file.

```python
import json

user = {
    "name": "Emperor",
    "age": 18,
    "active": True,
    "tags": ["python", "backend"]
}

with open("user.json", "w") as f:
    json.dump(user, f, indent=4)   # indent makes it readable
```

**Output (user.json):**
```json
{
    "name": "Emperor",
    "age": 18,
    "active": true,
    "tags": ["python", "backend"]
}
```

> 💡 **INSIGHT:** `indent=4` adds pretty‑printing, which is
> critical for human‑readable configuration files.

---

## 🧱 BRICK 2 – Reading JSON (`json.load`)

JSON file → Python dictionary.

```python
import json

with open("user.json", "r") as f:
    data = json.load(f)

print(data["name"])     # Emperor
print(data["age"])      # 18
```

**Working with JSON strings directly:**
- `json.dumps(obj)` → returns a JSON string
- `json.loads(str)` → parses a JSON string into a dict

```python
json_string = '{"name": "Emperor", "age": 18}'
user = json.loads(json_string)
print(user["name"])
```

> ⚠️ **WARNING:** JSON only supports: `str`, `int`, `float`,
> `bool`, `None`, `list`, `dict`. Complex Python objects
> (e.g., `datetime`) must be converted before serialising.

---

## 📌 Key Takeaway
- `json.dump(obj, file)` writes Python → JSON file.
- `json.load(file)` reads JSON file → Python dict.
- `json.dumps()` and `json.loads()` work with strings.
- Use `indent` for readable output; JSON is the lingua franca of the web.