# 📘 PyPhone Emperor · Module 3  
# 📖 L‑23 – String Indexing & Slicing (Text Processing Essentials)

---

## 🎯 OBJECTIVE  
Master **string indexing** and **slicing** to extract characters and substrings.  
Use these to parse product codes, transaction IDs, and log entries.  
Every character in a string has a fixed position; indexing grabs one, slicing grabs a range.

---

## 🧱 BRICK 1 – Indexing (Single Character Extraction)

An **index** is an integer offset from the start (0) or end (-1).

```python
s = 'PyPhone'
print(s[0])     # P  (first character)
print(s[2])     # h  (third character)
print(s[-1])    # e  (last character)
print(s[-3])    # o  (third‑from‑last)
```

**① Extract a transaction type flag**
```python
tx_code = 'P12345'
flag = tx_code[0]          # 'P' means purchase
if flag == 'P':
    print('Purchase order')
```

**② Validate a product code prefix**
```python
product = 'A100'
if product[0] == 'A':
    print('Active product')
```

> 💡 **INSIGHT:** Indexing returns exactly **one character**.  
> Use it for flags, prefixes, and single‑character checks.

> ⚠️ **WARNING:** Accessing an invalid index (e.g., `s[10]`) raises an `IndexError`.  
> Always check `len(s)` first or use slicing for safe ranges.

---

## 🧱 BRICK 2 – Slicing (Substring Extraction)

A **slice** extracts a substring: `string[start:stop:step]`.  
- `start` is inclusive, `stop` is exclusive.  
- Omitting `start` defaults to 0; omitting `stop` defaults to the end.  
- A negative `step` reverses the string.

**③ Extract a portion of a serial number**
```python
serial = 'SN‑2026‑07'
date_part = serial[3:7]   # '2026'
print(date_part)
```

**④ Get the middle segment of a product code**
```python
code = 'PRD‑EM‑001'
category = code[4:6]      # 'EM' (Emperor line)
print(category)
```

**⑤ Reverse an order ID for checksum**
```python
order_id = 'ORD‑123'
reversed_id = order_id[::-1]   # '321‑DRO'
print(reversed_id)
```

**⑥ Extract a substring from your practice variable**
```python
s = 'PyPhone'
# Task: substring from index 1 to 3 (exclusive 4)
print(s[1:4])   # 'yPh'
```

**⑦ Reverse the string (Hard practice task)**
```python
s = 'PyPhone'
print(s[::-1])   # 'enohPyP'
```

> 💡 **ADVANCED TIP – Safe slicing:**  
> Slicing never raises an `IndexError`. If the range is off the string, Python returns an empty string.  
> This makes slicing safer than indexing when you’re unsure of the length.

---

## 💡 Real‑world Usage

**Logistics – extract carrier code from tracking number**
```python
tracking = 'UPS‑1Z999AA1012345678'
carrier = tracking[:3]      # 'UPS'
print(f"Carrier: {carrier}")
```

**Banking – get the last 4 digits of an account number**
```python
account = '1234‑5678‑9012‑3456'
last_four = account[-4:]    # '3456'
print(f"Account ending in {last_four}")
```

**E‑commerce – parse SKU components**
```python
sku = 'ELEC‑PHONE‑BLK'
department = sku[:4]         # 'ELEC'
color = sku[-3:]             # 'BLK'
print(f"Dept: {department}, Color: {color}")
```

**HR – extract domain from email**
```python
email = 'emperor@pyphone.com'
domain = email[email.find('@')+1:]   # 'pyphone.com'
print(f"Domain: {domain}")
```

**Reporting – reverse a date string for sorting**
```python
date_str = '2026‑07‑08'
reversed_date = date_str[::-1]   # '80‑70‑6202'
print(f"Reversed: {reversed_date}")
```

---

## 🔍 Practice Preview
You will write three indexing/slicing mini‑programs.

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | `s='PyPhone'`. Print the first character. | `P`             |
| Medium | `s='PyPhone'`. Print substring from index 1 to 3 (exclusive 4). | `yPh`           |
| Hard   | `s='PyPhone'`. Print the string reversed using slicing. | `enohPyP`       |

Run the coach:
```bash
python ii_Practice_Sheets/L-23_String_Indexing_Slicing.py
```
Choose `1`, `2`, or `3`. Type your line; the engine checks output.

---

## 📌 Key Takeaway
- Indexing: `s[n]` returns one character (positive or negative index).
- Slicing: `s[start:stop:step]` returns a substring.
- `s[::-1]` reverses any string.
- Slicing never raises errors — it returns empty strings for out‑of‑bounds ranges.
- Essential for parsing codes, IDs, and delimited text data.