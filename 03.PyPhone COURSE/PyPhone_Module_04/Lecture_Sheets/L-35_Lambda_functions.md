# 📘 PyPhone Emperor · Module 4
# 📖 L‑35 – Lambda Functions

---

## 🎯 OBJECTIVE
Learn to write small, anonymous functions in a single
line using the **`lambda`** keyword. Lambda functions
are ideal for short, throwaway operations — especially
as arguments to higher‑order functions like `map()`,
`filter()`, and `sorted()`.

---

## 🧱 BRICK 1 – Syntax and Simple Use

```python
lambda arguments: expression
```

- No `def`, no name, no `return` keyword.
- The expression is evaluated and returned automatically.
- Can take any number of arguments but only **one** expression.

```python
square = lambda x: x ** 2
print(square(5))   # 25
print(square(9))   # 81
```

You can use it directly without assigning to a variable:

```python
print((lambda x, y: x + y)(10, 5))   # 15
```

> 💡 **INSIGHT:** Lambdas are **expressions**, not statements.
> You can use them anywhere a function object is expected.

---

## 🧱 BRICK 2 – Lambdas in Practice

**① With `map()` – apply to every element**
```python
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, nums))
print(squared)   # [1, 4, 9, 16]
```

**② With `filter()` – select elements**
```python
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)     # [2, 4]
```

**③ With `sorted()` – custom sort key**
```python
pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_pairs = sorted(pairs, key=lambda pair: pair[0])
print(sorted_pairs)   # [(1,'one'), (2,'two'), (3,'three')]
```

> ⚠️ **WARNING:** Lambdas are meant for simple logic.
> If the operation is complex or spans multiple lines,
> use a regular `def` function — readability matters.

---

## 📌 Key Takeaway
- `lambda` creates an anonymous function in one line.
- No `return` needed; the expression is the return value.
- Perfect for `map`, `filter`, `sorted`, and other functions
  that accept callables.
- Keep lambdas short and simple.