# 📘 PyPhone Emperor · Module 3
# 📖 L‑24 – String Methods

---

## 🎯 OBJECTIVE
Learn the most common built‑in **string methods** —
functions that operate directly on string objects
to transform, split, join, and search text.
String methods are the core toolkit for cleaning,
validating, and formatting any text data.

---

## 🧱 BRICK 1 – Case Conversion and Search

### Changing case
- `.upper()` → all characters uppercase
- `.lower()` → all characters lowercase
- `.title()` → first letter of each word uppercase

```python
msg = "hello world"
print(msg.upper())       # HELLO WORLD
print(msg.title())       # Hello World
print(msg.lower())       # hello world
```

### Searching and checking
- `.find(sub)` → index of first occurrence (or -1)
- `.count(sub)` → number of occurrences
- `.startswith(prefix)` → True/False
- `.endswith(suffix)` → True/False

```python
email = "emperor@domain.com"
print(email.find("@"))        # 7
print(email.count("o"))       # 2
print(email.endswith(".com")) # True
```

> 💡 **INSIGHT:** `.find()` returns `-1` when the
> substring is missing. It never crashes.

---

## 🧱 BRICK 2 – Splitting, Joining, and Replacing

### Split a string into a list
`.split(separator)` breaks a string into parts and
returns a list of substrings.

```python
data = "apple,banana,grape"
fruits = data.split(",")
print(fruits)   # ['apple', 'banana', 'grape']
```

If no separator is given, `.split()` splits on any
whitespace and removes empty strings.

### Join a list into a string
`separator.join(list)` does the reverse: it glues list
elements together with the separator.

```python
words = ["PyPhone", "Emperor", "Rocks"]
sentence = " ".join(words)
print(sentence)   # PyPhone Emperor Rocks
```

### Replace parts of a string
`.replace(old, new)` returns a new string with all
occurrences of `old` replaced by `new`.

```python
path = "C:\\Users\\OldName\\docs"
new_path = path.replace("OldName", "Emperor")
print(new_path)   # C:\Users\Emperor\docs
```

> ⚠️ **REMEMBER:** Strings are **immutable**. Methods
> always return a new string; they never change the
> original in place.

---

## 📌 Key Takeaway
- `.upper()`, `.lower()`, `.title()` change case.
- `.find()`, `.count()`, `.startswith()` search strings.
- `.split()` breaks a string into a list.
- `" ".join()` reassembles a list into a string.
- `.replace()` swaps substrings.