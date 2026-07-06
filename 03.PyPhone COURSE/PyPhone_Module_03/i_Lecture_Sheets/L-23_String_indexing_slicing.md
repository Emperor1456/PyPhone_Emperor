# 📘 PyPhone Emperor · Module 3
# 📖 L‑23 – String Indexing & Slicing

---

## 🎯 OBJECTIVE
Learn to access individual characters inside a string
using **indexing**, and extract substrings using **slicing**.
Strings are ordered sequences, and every character has a
position — starting from 0. Mastering indexing and slicing
is essential for text processing, data parsing, and
everyday Python.

---

## 🧱 BRICK 1 – Indexing (Single Character)

An **index** is a number that points to a position inside
the string. Python uses **zero‑based indexing** — the first
character is at index `0`.

```python
word = "Python"
print(word[0])    # P
print(word[1])    # y
print(word[5])    # n
```

**Negative indexing** counts from the end:
```python
print(word[-1])   # n  (last character)
print(word[-2])   # o  (second‑to‑last)
```

> ⚠️ **WARNING:** Accessing an index that does not exist
> (e.g., `word[6]`) raises an `IndexError`. Always stay
> within `0` to `len(word)-1` (or negative equivalents).

---

## 🧱 BRICK 2 – Slicing (Substrings)

A **slice** extracts a range of characters using the
syntax `string[start:stop:step]`.

- `start` – index to begin (inclusive, default 0)
- `stop`  – index to end (exclusive, default length)
- `step`  – step size (default 1)

```python
text = "Hello, World!"
print(text[0:5])      # Hello (indices 0,1,2,3,4)
print(text[7:12])     # World
print(text[:5])       # Hello (start defaults to 0)
print(text[7:])       # World! (stop defaults to end)
print(text[::2])      # Hlo ol! (every second char)
print(text[::-1])     # !dlroW ,olleH (reverse)
```

**Negative slice indices:**
```python
print(text[-6:-1])    # World (from -6 up to but not -1)
print(text[-5:])      # orld! (from -5 to end)
```

> 💡 **INSIGHT:** `[::-1]` is the classic Python one‑liner to
> reverse a string.

---

## 📌 Key Takeaway
- Indexing: `string[pos]` returns one character.
- Slicing: `string[start:stop:step]` returns a substring.
- Negative indices count from the end.
- Slicing never raises an error; out‑of‑range is silently truncated.