# 📘 PyPhone Emperor · Module 6  
# 📖 L‑47 – Working with JSON (Data Interchange Format)

---

## 🎯 OBJECTIVE  
Master JSON — the universal data format — using Python's `json` module.  
Convert dictionaries to JSON strings and files, and parse JSON back into Python objects.  
This is the backbone of configuration storage, API communication, and data persistence.

---

## 🧱 BRICK 1 – JSON Strings: `loads` and `dumps`

**① Parse a JSON string into a dictionary (Easy practice)**
```python
import json
data = json.loads('{"key": "value"}')
print(data)   # {'key': 'value'}
```
`json.loads()` takes a string and returns the corresponding Python dict.

**② Convert a dictionary to a JSON string (Medium practice)**
```python
import json
json_str = json.dumps({'name': 'Emperor'})
print(json_str)   # {"name": "Emperor"}
```
`json.dumps()` serializes a Python object into a JSON string. Use `indent` for readability.

**③ File I/O: write a dict to file, then read it back (Hard practice)**
```python
import json
# Write
with open('data.json', 'w') as f:
    json.dump({'age': 18}, f)

# Read
with open('data.json', 'r') as f:
    data = json.load(f)
print(data)   # {'age': 18}
```
`json.dump()` writes directly to a file; `json.load()` reads from a file.

> 💡 **INSIGHT:** JSON types map cleanly to Python: `dict` ↔ object, `list` ↔ array, `str` ↔ string, `int/float` ↔ number, `True/False` ↔ true/false, `None` ↔ null.

---

## 🧱 BRICK 2 – Business Use of JSON

**④ Storing configuration**
```python
config = {"host": "localhost", "port": 8080, "debug": True}
with open('config.json', 'w') as f:
    json.dump(config, f, indent=4)
```

**⑤ Sending data over an API (simulated)**
```python
response = '{"status": "success", "balance": 1200}'
data = json.loads(response)
print(data['balance'])   # 1200
```

**⑥ Logging structured events**
```python
import json
event = {"user": "Emperor", "action": "login", "time": "2026-07-09"}
with open('events.json', 'a') as f:
    f.write(json.dumps(event) + '\n')
```

> ⚠️ **WARNING:** JSON does not support tuples, sets, or complex Python objects. Convert them to lists/strings before serializing.

> 💡 **ADVANCED TIP – `default` parameter:**  
> For custom objects, provide a `default` function to `json.dumps()` to convert them to a serializable format.

---

## 💡 Real‑world Usage

**Banking – load account data from a JSON file**
```python
with open('accounts.json', 'r') as f:
    accounts = json.load(f)
print(accounts['A100']['balance'])
```

**E‑commerce – product catalog**
```python
catalog = {"products": [{"id": 1, "name": "Mouse"}, {"id": 2, "name": "Keyboard"}]}
with open('catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)
```

**Logistics – import shipment details**
```python
shipment_json = '{"tracking": "TRK-123", "weight": 12.5}'
shipment = json.loads(shipment_json)
print(shipment['tracking'])
```

**HR – employee database export**
```python
employees = [{"name": "Emperor", "dept": "Eng"}, {"name": "Rahim", "dept": "Sales"}]
with open('hr.json', 'w') as f:
    json.dump(employees, f)
```

---

## 🔍 Practice Preview

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | Parse the JSON string `'{"key":"value"}'` into a dict and print it. | `{'key': 'value'}` |
| Medium | Convert the dict `{'name':'Emperor'}` to a JSON string and print it. | `{"name": "Emperor"}` |
| Hard   | Write dict `{'age':18}` to a file `data.json`, then read it back and print the dict. | `{'age': 18}` |

Run the coach:
```bash
python ii_Practice_Sheets/L-47_JSON.py
```

---

## 📌 Key Takeaway
- `json.loads(str)` → Python object; `json.dumps(obj)` → JSON string.
- `json.load(file)` reads JSON from file; `json.dump(obj, file)` writes to file.
- JSON is the standard for data interchange in web APIs, configs, and data storage.
- Companion will use JSON for configuration and export/import of memory fragments.