# 📘 PyPhone Emperor · Module 1  
# 📖 L‑05 – Escape Sequences (Continued)

---

## 🎯 OBJECTIVE
Complete your mastery of escape sequences.
Learn to include quotes inside strings
and to print special characters like backslashes.
This ensures your strings can hold any text
without breaking Python syntax.

---

## 🧱 BRICK 1 – Escaping Quotes Inside Strings

Python uses quotes to mark where a string begins and ends.
If you want a quote character inside the string itself,
you must either **escape** it with a backslash
or choose a different outer quote.

### Method 1: Backslash escape
Put `\` before the quote to tell Python it is part of the text,
not the end of the string.

```python
print("She said, \"Hello!\"")
# She said, "Hello!"

print('It\'s a beautiful day.')
# It's a beautiful day.
```

### Method 2: Mix the outer quotes
If the string contains double quotes, wrap it in single quotes.
If it contains single quotes, wrap it in double quotes.

```python
print('He said, "Python is great!"')
print("It's easy to learn.")
```

> 💡 **TIP:** Mixing outer quotes is cleaner when you have many quote characters inside the string.

### Escaping the backslash itself
To print one backslash, write two.

```python
print("A single backslash: \\")
# A single backslash: \
```

---

## 🧱 BRICK 2 – More Useful Escape Sequences

Beyond newline `\n` and tab `\t`, these escapes handle
special characters that are otherwise hard to type.

- `\\`   Backslash (prints `\`)
- `\"`   Double quote (prints `"`)
- `\'`   Single quote (prints `'`)

### Example with file paths
Windows paths use backslashes, so escape them.

```python
print("Path: C:\\Users\\Emperor")
# Path: C:\Users\Emperor
```

### Raw strings – turn off all escapes
Prefix with `r` to treat backslashes as literal characters.

```python
print(r"C:\new_folder\temp")
# C:\new_folder\temp   (no tab or newline)
```

Use raw strings for file paths, regex, or any text
with many backslashes.

> ⚠️ **WARNING:** A raw string cannot end with a single backslash. `r"\"` is invalid.

---

## 💡 Real‑world Usage
Enterprise logs often include file paths or quoted messages.

```python
# Log a file access
path = "C:\\Program Files\\MyApp\\config.txt"
print("Reading config from:", path)
```

---

## 🔍 Practice Preview (for later coding)
```python
# Print a quote within a quote
print("The sign said, \"Welcome to Python\".")

# Print a file path correctly
print("File location: C:\\Users\\Emperor\\docs")

# Demonstrate single and double quote escaping
print('It\'s a "double" example.')

# Raw string example
print(r"In raw string, \n is not a newline.")
```

---

## 📌 Key Takeaway
- Escape quotes with `\"` or `\'`.
- Mix outer quotes when convenient.
- `\\` prints one backslash.
- Raw strings (`r"..."`) ignore escapes.