# 📘 PyPhone Emperor · Module 2
# 📖 L‑20 – `for` Loop

---

## 🎯 OBJECTIVE
Learn to iterate over a sequence (like a range of numbers,
a string, or a list) using the **`for`** loop.
The `for` loop executes a block of code once for each item
in the sequence, making repetitive tasks clean and predictable.

---

## 🧱 BRICK 1 – Iterating with `range()`

`range(start, stop, step)` generates a sequence of integers.
It’s the most common companion to `for` when you know exactly
how many times to repeat something.

```python
for variable in range(start, stop):
    # block runs for each number from start to stop-1
```

**Example:**
```python
for i in range(1, 6):
    print(i)
```
Output:
```
1
2
3
4
5
```

**Variations:**
- `range(5)` → 0, 1, 2, 3, 4
- `range(2, 10, 2)` → 2, 4, 6, 8

> 💡 **INSIGHT:** `range()` does not include the stop value.
> `range(1,5)` gives 1,2,3,4.

---

## 🧱 BRICK 2 – Iterating Over Strings and Other Sequences

A `for` loop can directly visit each character of a string,
or each element of any iterable (lists, tuples, sets, etc.,
which you’ll study later).

**String iteration:**
```python
for char in "Python":
    print(char)
```
Output:
```
P
y
t
h
o
n
```

**Summing numbers in a fixed sequence:**
```python
total = 0
for num in [10, 20, 30, 40]:
    total += num
print("Total:", total)
```

---

## 📌 Key Takeaway
- `for` iterates over a sequence item by item.
- `range(n)` gives `n` repetitions.
- Use `for` when you know the number of iterations in advance.
- The loop variable takes a new value each pass.