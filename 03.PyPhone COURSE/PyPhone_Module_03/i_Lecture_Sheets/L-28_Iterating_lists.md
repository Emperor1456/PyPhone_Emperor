# 📘 PyPhone Emperor · Module 3
# 📖 L‑28 – Iterating Through Lists

---

## 🎯 OBJECTIVE
Learn to loop through every element of a list using
the `for` loop. This is the fundamental pattern for
processing collections — reading data, filtering,
transforming, and aggregating values.

---

## 🧱 BRICK 1 – Basic List Iteration

A `for` loop visits each item in a list, one by one,
in order. The loop variable takes the value of the
current element on each pass.

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```
Output:
```
apple
banana
cherry
```

### Iterating with `range()` and `len()`
If you need the **index** while looping, combine
`range()` with `len()`:

```python
colors = ["red", "green", "blue"]
for i in range(len(colors)):
    print(f"Index {i}: {colors[i]}")
```
Output:
```
Index 0: red
Index 1: green
Index 2: blue
```

---

## 🧱 BRICK 2 – Real‑world Patterns

**① Summing values**
```python
sales = [150, 89, 320, 45]
total = 0
for amount in sales:
    total += amount
print("Total sales:", total)
```

**② Filtering with a condition**
```python
scores = [55, 72, 40, 91, 33]
passing = []
for score in scores:
    if score >= 50:
        passing.append(score)
print("Passing scores:", passing)
```

**③ Modifying in place (with indexes)**
```python
prices = [10, 20, 30]
for i in range(len(prices)):
    prices[i] *= 1.1     # apply 10% tax
print(prices)            # [11.0, 22.0, 33.0]
```

> 💡 **INSIGHT:** Use `for item in list` when you only
> need the values. Use `for i in range(len(list))` when
> you need to modify the list or need the index.

**④ Using `enumerate()` for both index and value**
```python
tasks = ["design", "code", "test"]
for idx, task in enumerate(tasks):
    print(f"{idx}: {task}")
```

> ⚠️ **WARNING:** Never remove items from a list while
> iterating over it directly — the indexes shift and
> elements get skipped. Iterate over a copy or use a
> list comprehension.

---

## 📌 Key Takeaway
- `for item in list` iterates values directly.
- `range(len(list))` gives access to indexes.
- `enumerate()` provides both index and value cleanly.
- Use iteration for summing, filtering, and transforming data.