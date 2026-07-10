# 📘 PyPhone Emperor v3.0 · Module 3
# 📖 L‑13 – List Creation, Indexing & Mutability

---

## 🎯 OBJECTIVE — What You Will Master

> Lists are your first mutable data structure. Master them.

- 📋 **List creation** – square brackets, mixed types
- 🔢 **Indexing** – zero‑based, negative indices
- ✏️ **Mutability** – change items in place
- 📏 **`len()`** – size of the list
- 🧪 **Slicing** – extract sub‑lists

---

## 🧱 CREATING LISTS

A list is an ordered, mutable collection.

```python
fruits = ["apple", "banana", "cherry"]
mixed = [1, "two", 3.0, True]
empty = []
```

Use `len()` to get the number of items:
```python
print(len(fruits))   # 3
```

---

## 🧱 INDEXING & MUTABILITY

Lists are zero‑indexed; you can replace any element directly.

```python
colors = ["red", "green", "blue"]
print(colors[0])      # red
print(colors[-1])     # blue

colors[1] = "yellow"
print(colors)         # ['red', 'yellow', 'blue']
```

**Business – update inventory levels**
```python
stock = [150, 89, 320, 45]
stock[0] -= 10   # sold 10 of first item
print(stock)     # [140, 89, 320, 45]
```

> ⚠️ **WARNING:** Accessing an index that doesn’t exist raises `IndexError`. Use `len(list)-1` as the max valid index.

---

## 🧱 SLICING

Works exactly like string slicing – `[start:stop:step]`.

```python
nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4])      # [1, 2, 3]
print(nums[:3])       # [0, 1, 2]
print(nums[::2])      # [0, 2, 4]
print(nums[::-1])     # [5, 4, 3, 2, 1, 0]
```

---

## 💡 Real‑world Usage

**Banking – recent transactions**
```python
transactions = [-50, 200, -30, 500]
print(transactions[-1])   # latest: 500
```

**E‑commerce – featured products**
```python
products = ["Laptop", "Mouse", "Keyboard"]
print(products[:2])   # ['Laptop', 'Mouse']
```

**Logistics – stop IDs**
```python
stops = ["WH1", "HUB2", "HUB3", "DST4"]
print(len(stops))     # 4
```

---

## 🔍 Practice Preview

| Level | Task | What You’ll Write |
|-------|------|-------------------|
| Easy | Create a list of three product names and print it. | `items = ["A","B","C"]; print(items)` |
| Medium | Replace the second item in the list with a new value and print. | `items[1] = "X"; print(items)` |
| Hard | Extract the last two items using slicing and print. | `print(items[-2:])` |

Run the coach:
```bash
python ii_Practice_Sheets/L13_List_Creation_Indexing_Mutability.py
```

---

## 📌 Key Takeaway
- Lists are mutable, ordered, and indexable.
- Use `[]` for creation, `[start:stop:step]` for slicing.
- Mutability means you can change items in place.

*For Emperor.*