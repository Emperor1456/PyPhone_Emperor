# 📘 PyPhone Emperor · Module 3
# 📖 L‑26 – List Methods

---

## 🎯 OBJECTIVE
Learn the most important built‑in **list methods** —
functions that add, remove, and rearrange elements
inside a list. Mastering these methods lets you
manipulate collections of data with precision.

---

## 🧱 BRICK 1 – Adding Elements

### `.append(item)` – add to the end
```python
tasks = ["write code", "test"]
tasks.append("deploy")
print(tasks)   # ['write code', 'test', 'deploy']
```

### `.insert(index, item)` – add at a specific position
```python
tasks.insert(1, "review")
print(tasks)   # ['write code', 'review', 'test', 'deploy']
```

### `.extend(iterable)` – add multiple items at once
```python
tasks.extend(["monitor", "report"])
print(tasks)   # ['write code', 'review', 'test', 'deploy', 'monitor', 'report']
```

> 💡 **INSIGHT:** `.append()` adds a single element;
> `.extend()` adds each element from another list.

---

## 🧱 BRICK 2 – Removing and Sorting

### Removing elements
- `.remove(value)` – removes the **first** occurrence
- `.pop(index)` – removes and returns the element at index (default last)
- `.clear()` – empties the entire list

```python
items = ["a", "b", "c", "b"]
items.remove("b")     # removes first "b"
print(items)          # ['a', 'c', 'b']

last = items.pop()    # removes and returns 'b'
print(last)           # b
print(items)          # ['a', 'c']
```

### Sorting
- `.sort()` – sorts the list in place (ascending by default)
- `.sort(reverse=True)` – descending
- `.reverse()` – reverses the order in place

```python
nums = [3, 1, 4, 1, 5]
nums.sort()
print(nums)            # [1, 1, 3, 4, 5]
nums.reverse()
print(nums)            # [5, 4, 3, 1, 1]
```

> ⚠️ **WARNING:** `.sort()` and `.reverse()` modify the
> original list and return `None`. Don’t assign the result!

---

## 📌 Key Takeaway
- `.append()`, `.insert()`, `.extend()` add items.
- `.remove()`, `.pop()`, `.clear()` delete items.
- `.sort()` and `.reverse()` reorder the list in place.
- Most list methods return `None` — they change the list directly.