# 📘 PyPhone Emperor · Module 3  
# 🗃️ Comprehensive Note – Strings & Lists

---

## 🎯 Scope
This note covers every essential operation on strings and lists from Module 3.  
It is a single‑page reference for indexing, slicing, string methods, list creation, list methods, list comprehensions, and iteration.  
All code fits a phone screen; no sideways scrolling.

---

## 🧱 1. String Indexing
Access a single character using its position (index).  
Indices start at **0** for the first character.  
Negative indices count from the end (`-1` is the last character).

```python
word = "Python"
print(word[0])    # P
print(word[2])    # t
print(word[-1])   # n
```

---

## ✂️ 2. String Slicing
Extract a substring with `[start:stop:step]`.  
- `start` – index to begin (inclusive, default 0).  
- `stop` – index to end (exclusive, default length).  
- `step` – stride (default 1).

```python
text = "Hello, World!"
print(text[0:5])      # Hello
print(text[7:])       # World!
print(text[:5])       # Hello
print(text[::2])      # Hlo ol!
```

**Reverse a string:**  
```python
print(text[::-1])     # !dlroW ,olleH
```

---

## 🧪 3. Essential String Methods
Strings are **immutable**; methods return new strings.

| Method        | Action                                    |
|---------------|-------------------------------------------|
| `.upper()`    | All uppercase                             |
| `.lower()`    | All lowercase                             |
| `.split(sep)` | Breaks string into list by separator      |
| `.join(list)` | Glues list elements together with string  |
| `.replace(old, new)` | Replaces all occurrences of old with new |
| `.strip()`    | Removes leading/trailing whitespace       |
| `.find(sub)`  | Returns index of sub, or -1               |
| `.count(sub)` | Counts non‑overlapping occurrences        |
| `.startswith(prefix)` | True if starts with prefix        |
| `.endswith(suffix)`   | True if ends with suffix          |

**Examples:**
```python
msg = "  hello world  "
print(msg.strip().upper())         # HELLO WORLD

data = "apple,banana,grape"
fruits = data.split(",")           # ['apple','banana','grape']
print(" | ".join(fruits))          # apple | banana | grape

path = "C:\\Users\\OldName"
new_path = path.replace("OldName", "Emperor")
print(new_path)                    # C:\Users\Emperor
```

---

## 📋 4. Lists – Creation & Indexing
A **list** is a mutable, ordered collection.  
Written with square brackets `[]`, items separated by commas.

```python
empty = []
nums = [10, 20, 30]
mixed = [1, "two", 3.0, True]
matrix = [[1,2],[3,4]]
```

**Indexing (zero‑based):**
```python
colors = ["red", "green", "blue"]
print(colors[0])      # red
print(colors[-1])     # blue
colors[1] = "yellow"  # allowed (lists are mutable)
```

**Slicing lists** works exactly like string slicing:
```python
nums = [0,1,2,3,4,5]
print(nums[1:4])      # [1,2,3]
print(nums[::-1])     # [5,4,3,2,1,0]
```

---

## 🔧 5. List Methods
Most list methods modify the list **in place** and return `None`.

| Method             | Action                                       |
|--------------------|----------------------------------------------|
| `.append(item)`    | Add item to the end                          |
| `.insert(idx, item)` | Insert item at given index                 |
| `.extend(iterable)` | Add all elements from iterable              |
| `.remove(item)`    | Remove first occurrence of item              |
| `.pop(idx)`        | Remove and return item at idx (default last) |
| `.clear()`         | Remove all items                             |
| `.sort()`          | Sort in ascending order (in place)           |
| `.reverse()`       | Reverse order in place                       |

**Examples:**
```python
tasks = ["write code"]
tasks.append("test")
tasks.insert(0, "plan")
print(tasks)         # ['plan','write code','test']

tasks.remove("test")
last = tasks.pop()   # 'write code'
tasks.clear()        # []
```

---

## 🧙 6. List Comprehensions
Create a new list by applying an expression to each item of an iterable, optionally filtering.

```python
squares = [x**2 for x in range(10)]
# [0,1,4,9,16,25,36,49,64,81]

evens = [x for x in range(20) if x % 2 == 0]
# [0,2,4,6,8,10,12,14,16,18]

words = ["hello", "world"]
upper = [w.upper() for w in words]
# ['HELLO','WORLD']
```

---

## 🔁 7. Iterating Through Lists
Use a `for` loop to process each element.

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

**With index:**  
```python
for i in range(len(fruits)):
    print(i, fruits[i])
```

**With `enumerate`:**  
```python
for idx, fruit in enumerate(fruits):
    print(idx, fruit)
```

---

## 💡 Quick Reference
```python
# Strings
word = "Python"
word[0]              # 'P'
word[-1]             # 'n'
word[1:4]            # 'yth'
word[::-1]           # 'nohtyP'

msg = "hello world"
msg.upper()          # "HELLO WORLD"
msg.split()          # ['hello','world']
" ".join(["a","b"])  # "a b"
msg.replace("world","Emperor")  # "hello Emperor"

# Lists
nums = [1,2,3]
nums.append(4)       # [1,2,3,4]
nums.pop()           # 4, list becomes [1,2,3]
nums.insert(0,0)     # [0,1,2,3]
len(nums)            # 4

# List comprehension
[x**2 for x in range(5)]   # [0,1,4,9,16]

# Iteration
for n in [10,20,30]:
    print(n)
```

---

## 📌 Key Takeaway
- Strings are immutable; indexing and slicing create new strings.
- Lists are mutable; methods like `.append()` and `.pop()` change them in place.
- List comprehensions offer a concise way to build lists.
- `for` loops, `range()`, and `enumerate()` are your primary tools for iteration.

*Study this sheet. Recall it from memory. Then practice.*