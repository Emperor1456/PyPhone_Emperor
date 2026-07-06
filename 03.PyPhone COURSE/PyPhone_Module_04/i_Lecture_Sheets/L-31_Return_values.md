# 📘 PyPhone Emperor · Module 4
# 📖 L‑31 – Return Values

---

## 🎯 OBJECTIVE
Learn how functions send data back to the caller
using the `return` statement. Return values allow
functions to compute a result and pass it to the
rest of the program — the key to building
composable, testable logic.

---

## 🧱 BRICK 1 – The `return` Statement

`return` immediately exits the function and sends
a value back to the line that called it. If there
is no `return`, the function returns `None`.

```python
def add(a, b):
    result = a + b
    return result

sum_value = add(4, 6)   # sum_value is now 10
print(sum_value)        # 10
```

You can use the returned value directly:
```python
print(add(2, 3) * 2)    # 10
```

> 💡 **INSIGHT:** A function can have multiple `return`
> statements — the first one reached ends the function.

---

## 🧱 BRICK 2 – Early Returns and Multiple Outputs

Functions can return early when a condition is met,
avoiding unnecessary computation.

```python
def safe_divide(a, b):
    if b == 0:
        return None       # early exit
    return a / b
```

Return multiple values by separating them with commas.
Python packs them into a tuple automatically.

```python
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([4, 1, 9, 3])
print(low)    # 1
print(high)   # 9
```

> ⚠️ **WARNING:** Code after a `return` is **not executed**.
> Any loop or condition that follows a `return` in the
> same block is dead code.

---

## 📌 Key Takeaway
- `return` sends a value back to the caller.
- Functions without `return` evaluate to `None`.
- Use early returns to handle edge cases cleanly.
- Multiple return values are packed into a tuple.