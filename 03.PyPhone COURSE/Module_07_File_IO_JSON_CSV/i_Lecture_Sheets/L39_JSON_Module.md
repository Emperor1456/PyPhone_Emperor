# 📘 PyPhone Emperor v3.0 · Module 7
# 📖 L‑39 – JSON – `load`, `dump`, `loads`, `dumps` & Schema Validation

---

## 🎯 OBJECTIVE — What You Will Master

> The universal data interchange format – JSON.

- 📖 `json.load(file)` – read JSON from a file → Python dict
- ✍️ `json.dump(obj, file)` – write Python object to file as JSON
- 🔄 `json.loads(str)` – parse a JSON string
- 🔄 `json.dumps(obj)` – convert Python object to JSON string
- 🧪 `indent` – pretty printing for readability

---

## 🧱 READING JSON FROM FILE

```python
import json
with open("config.json", "r") as f:
    data = json.load(f)
print(data["host"])
```

---

## 🧱 WRITING JSON TO FILE

```python
config = {"host": "localhost", "port": 8080}
with open("config.json", "w") as f:
    json.dump(config, f, indent=4)
```

---

## 🧱 WORKING WITH JSON STRINGS

```python
json_str = '{"name": "Emperor", "age": 18}'
user = json.loads(json_str)
print(user["name"])

# back to string
print(json.dumps(user))
```

---

## 💡 Real‑world Usage

**Banking – load account data**
```python
with open("accounts.json") as f:
    accounts = json.load(f)
```

**E‑commerce – product catalog**
```python
catalog = {"products": [...]}
with open("catalog.json", "w") as f:
    json.dump(catalog, f, indent=2)
```

**Logistics – shipment details**
```python
shipment = json.loads('{"tracking": "TRK-1", "weight": 12.5}')
```

---

## 🔍 Practice Preview

| Level | Task |
|-------|------|
| Easy | Parse a JSON string into a dict and print it. |
| Medium | Convert a dict to a JSON string and print it. |
| Hard | Write a dict to a file, read it back, and print the dict. |

Run the coach:
```bash
python ii_Practice_Sheets/L39_JSON_Module.py
```

---

## 📌 Key Takeaway
- `json.load`/`dump` for files; `json.loads`/`dumps` for strings.
- `indent` makes JSON human‑readable.
- JSON is the backbone of APIs and configuration.

*For Emperor.*