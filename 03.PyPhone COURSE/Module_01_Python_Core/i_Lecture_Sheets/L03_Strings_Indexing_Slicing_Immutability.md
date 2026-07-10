# 📘 PyPhone Emperor v3.0 · Module 1
# 📖 L‑03 – Strings: Indexing, Slicing & Immutability

---

## 🎯 OBJECTIVE — What You Will Master

> After this lesson, text will bend to your will.

- 🔤 String creation – single, double, triple quotes
- 🧮 Indexing – every character has a position
- ✂️ Slicing – extract any substring with precision
- 🛡️ Immutability – why strings never change
- 🔁 Common patterns – reverse, skip, copy, mask

---

## 🧱 STRINGS ARE SEQUENCES

A string is an ordered sequence of Unicode characters.
Every character has a fixed index, starting from 0.

```python
word = "Python"
print(word[0])      # P
print(word[2])      # t
print(word[-1])     # n
```

Positive indices count from the left.
Negative indices count from the right (-1 = last).

| Index | 0 | 1 | 2 | 3 | 4 | 5 |
|-------|---|---|---|---|---|---|
| Char  | P | y | t | h | o | n |
| Neg   | -6| -5| -4| -3| -2| -1|

Accessing an invalid index raises `IndexError`.
Use `len()` to get the number of characters.

---

## 🧱 SLICING – THE SUBSTRING TOOL

Syntax: `string[start:stop:step]`

- `start` – inclusive (default 0)
- `stop`  – exclusive (default end)
- `step`  – stride (default 1)

```python
text = "Hello, Emperor"
print(text[0:5])      # Hello
print(text[7:])       # Emperor
print(text[:5])       # Hello
print(text[::2])      # Hlo m eo
print(text[::-1])     # rorepmE ,olleH
```

Omitting `start` begins at 0. Omitting `stop` goes to end.
Negative step reverses direction.

> ⚠️ **WARNING:** Slicing never raises `IndexError`.
> Out‑of‑range slice returns an empty string.

---

## 🧱 IMMUTABILITY – STRINGS NEVER CHANGE

Once created, a string cannot be modified in place.
```python
s = "Hello"
s[0] = "J"   # TypeError! 'str' object does not support item assignment
```

To "change" a string, build a new one:
```python
s = "Hello"
s = "J" + s[1:]   # "Jello"
```

> 💡 **INSIGHT:** Immutability makes strings safe as dictionary keys,
> fast to hash, and never accidentally modified across function calls.

---

## 🧱 COMMON SLICE PATTERNS

- **Copy:** `s[:]`
- **Reverse:** `s[::-1]`
- **Every nth char:** `s[::2]`
- **Remove first/last:** `s[1:]`, `s[:-1]`

```python
order_id = "ORD-123-XYZ"
category = order_id[4:7]     # "123"
reversed_id = order_id[::-1] # "ZYX-321-DRO"
```

---

## 💡 Real‑world Usage

**Banking – mask account number**
```python
acct = "1234567890123456"
masked = "****" + acct[-4:]
print(masked)   # ****3456
```

**E‑commerce – extract SKU components**
```python
sku = "ELEC-PHONE-BLK"
department = sku[:4]       # ELEC
color = sku[-3:]           # BLK
print(department, color)
```

**Logistics – parse tracking prefix**
```python
tracking = "UPS-1Z999AA1012345678"
carrier = tracking[:3]    # UPS
print(carrier)
```

**HR – email domain extraction**
```python
email = "emperor@pyphone.com"
domain = email[email.find("@")+1:]
print(domain)   # pyphone.com
```

---

## 🔍 Practice Preview
You will:
- Access specific characters from product codes.
- Extract substrings using slicing.
- Reverse order IDs for checksum generation.
- Demonstrate immutability by building a corrected string.

Run the coach:
```bash
python ii_Practice_Sheets/L03_Strings_Indexing_Slicing_Immutability.py
```

---

## 📌 Key Takeaway
- Strings are sequences with fixed indices.
- Slicing `[start:stop:step]` extracts substrings.
- Strings are immutable – operations create new strings.
- Master slicing, and you master text processing.

*For Emperor.*