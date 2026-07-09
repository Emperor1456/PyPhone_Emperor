# 📘 PyPhone Emperor · Module 4  
# 📖 L‑35 – Lambda Functions (Anonymous One‑Liners)

---

## 🎯 OBJECTIVE  
Master the `lambda` keyword to create small, anonymous functions in a single expression.  
Lambdas shine when you need a short function as an argument — for `map()`, `filter()`, `sorted()`,  
or anywhere a callable is expected. They are the quick‑fire tools of business data transformation.

---

## 🧱 BRICK 1 – Syntax and Basic Usage

```python
lambda arguments: expression
```
- No `def`, no name, no `return` keyword.
- The expression is evaluated and returned automatically.

**① Doubling a number**
```python
double = lambda x: x * 2
result = double(5)
print(result)   # 10
```
The lambda takes `x`, returns `x * 2`.  
Assigned to `double`, it works like a regular function.  
This is the Easy practice task.

**② Adding two numbers**
```python
add = lambda a, b: a + b
total = add(3, 5)
print(total)   # 8
```
Multiple arguments go before the colon, separated by commas.  
This matches the Medium practice task — a compact calculator for summing transaction amounts.

> 💡 **INSIGHT:** Lambdas are **expressions**, not statements.  
> You can define them inside a function call, pass them as arguments, or return them from other functions.

---

## 🧱 BRICK 2 – Lambdas in Business Data Operations

**③ Sorting with a custom key**
```python
words = ['banana', 'cherry', 'apple']
sorted_words = sorted(words, key=lambda w: w[1])
print(sorted_words)   # ['banana', 'cherry', 'apple']
```
The lambda extracts the second character of each word as the sort key.  
`'banana'[1]` = `'a'`, `'cherry'[1]` = `'h'`, `'apple'[1]` = `'p'`.  
Alphabetically: a < h < p → `'banana'`, `'cherry'`, `'apple'`.  
This is the Hard practice task.

**④ Filtering high‑value transactions**
```python
amounts = [120, 45, 300, 80]
large = list(filter(lambda x: x > 100, amounts))
print(large)   # [120, 300]
```

**⑤ Transforming prices with `map()`**
```python
prices = [10, 20, 30]
taxed = list(map(lambda p: p * 1.1, prices))
print(taxed)   # [11.0, 22.0, 33.0]
```

**⑥ Inline lambda without assignment**
```python
result = (lambda a, b: a ** b)(2, 8)
print(result)   # 256
```

> ⚠️ **WARNING:** Lambdas are meant for **simple** logic.  
> If your operation spans multiple lines or requires complex branching, use `def`.  
> Readability always beats brevity in production code.

> 💡 **ADVANCED TIP:** Lambdas are the backbone of functional programming in Python.  
> Combined with `map()`, `filter()`, and `sorted()`, they form a concise data‑processing pipeline  
> that will be essential when you build Companion's text processing and memory retrieval modules.

---

## 💡 Real‑world Usage

**Banking – sort accounts by balance**
```python
accounts = [('A1', 500), ('A2', 1200), ('A3', 300)]
sorted_accounts = sorted(accounts, key=lambda acc: acc[1], reverse=True)
print(sorted_accounts)   # [('A2', 1200), ('A1', 500), ('A3', 300)]
```

**E‑commerce – filter in‑stock items**
```python
items = [('laptop', 5), ('mouse', 0), ('keyboard', 3)]
in_stock = list(filter(lambda item: item[1] > 0, items))
print(in_stock)   # [('laptop', 5), ('keyboard', 3)]
```

**Logistics – extract package codes starting with 'A'**
```python
codes = ['A101', 'B202', 'A303', 'C404']
a_codes = list(filter(lambda c: c.startswith('A'), codes))
print(a_codes)   # ['A101', 'A303']
```

---

## 🔍 Practice Preview

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | Create a lambda that doubles a number, assign to `double`, call with 5 and print. | `10` |
| Medium | Create lambda `add` that adds two numbers, call with 3,5 and print. | `8` |
| Hard   | Sort `['banana','cherry','apple']` by the second character using a lambda as key. Print the sorted list. | `['banana', 'cherry', 'apple']` |

Run the coach:
```bash
python ii_Practice_Sheets/L-35_Lambda_Functions.py
```

---

## 📌 Key Takeaway
- `lambda` creates an anonymous function in one expression.
- No `return` needed — the expression is the return value.
- Perfect as a key for `sorted()`, a predicate for `filter()`, or a transformer for `map()`.
- Keep lambdas short; use `def` for complex logic.
- A core tool for data pipelines and functional programming.