# 📘 PyPhone Emperor v3.0 · Module 5
# 📖 L‑30 – Lambda Functions, `map()`, `filter()`, `sorted(key=)`

---

## 🎯 OBJECTIVE — What You Will Master

> Anonymous one‑liner functions and functional programming tools.

- 🐑 **Lambda** – `lambda args: expression`
- 🗺️ **`map()`** – apply a function to every element
- 🔍 **`filter()`** – keep elements that satisfy a predicate
- 📊 **`sorted(key=)`** – sort using a custom key function

---

## 🧱 LAMBDA FUNCTIONS

```python
square = lambda x: x**2
print(square(5))   # 25
```

Lambdas are expressions; they can be used inline.

```python
print((lambda x, y: x + y)(10, 5))   # 15
```

---

## 🧱 `map()` – TRANSFORM

```python
nums = [1, 2, 3]
squared = list(map(lambda x: x**2, nums))
print(squared)   # [1, 4, 9]
```

---

## 🧱 `filter()` – SELECT

```python
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)   # [2]
```

---

## 🧱 `sorted(key=)` – CUSTOM SORT

```python
words = ["banana", "cherry", "apple"]
by_length = sorted(words, key=lambda w: len(w))
print(by_length)   # ['apple', 'cherry', 'banana']
```

> ⚠️ **WARNING:** Lambdas should remain simple; for complex logic use a named function.

---

## 💡 Real‑world Usage

**Banking – filter large transactions**
```python
txns = [120, 600, 80]
large = list(filter(lambda t: t > 100, txns))
```

**E‑commerce – apply discount to prices**
```python
prices = [100, 200]
discounted = list(map(lambda p: p*0.9, prices))
```

**Logistics – sort by weight**
```python
packages = [(12, "A"), (8, "B")]
packages.sort(key=lambda p: p[0])
```

---

## 🔍 Practice Preview

| Level | Task | What You’ll Write |
|-------|------|-------------------|
| Easy | Create lambda doubling a number, call with 5. | `double=lambda x: x*2; print(double(5))` |
| Medium | Create lambda adding two numbers, call with 3,5. | `add=lambda a,b: a+b; print(add(3,5))` |
| Hard | Sort words by second character using lambda key. | `sorted(words, key=lambda w: w[1])` |

Run the coach:
```bash
python ii_Practice_Sheets/L30_Lambda_map_filter_sorted.py
```

---

## 📌 Key Takeaway
- Lambda: compact anonymous functions.
- `map()` and `filter()` transform/select without loops.
- `sorted(key=)` customizes ordering.

*For Emperor.*