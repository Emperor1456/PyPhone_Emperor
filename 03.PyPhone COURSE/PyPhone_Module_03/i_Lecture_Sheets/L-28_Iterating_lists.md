# 📘 PyPhone Emperor · Module 3  
# 📖 L‑28 – Iterating Through Lists (Processing Business Collections)

---

## 🎯 OBJECTIVE  
Master list iteration with `for` loops to process business data:  
summing sales, building reports, converting product codes, and filtering records.  
When you need to transform, aggregate, or display every item in a list,  
a `for` loop is the most direct tool.

---

## 🧱 BRICK 1 – Basic Iteration and Accumulation

A `for` loop visits each element in a list, one by one, in order.

```python
for item in list:
    # process item
```

**① Sum all values – daily sales total**
```python
amounts = [1, 2, 3, 4, 5]
total = 0
for x in amounts:
    total += x
print(total)   # 15
```
`x` takes each amount; `total` accumulates the sum.  
This is the exact pattern for the Easy practice task.

**② Build a report string by joining words**
```python
words = ['apple', 'banana']
result = ''
for w in words:
    result += w + ' '
print(result.strip())   # 'apple banana'
```
Each fruit name is appended with a space; `.strip()` removes the final space.  
This mirrors the Medium practice task.

**③ Count items matching a condition – low‑stock alert**
```python
stock = [5, 12, 3, 8, 0]
low = 0
for qty in stock:
    if qty <= 3:
        low += 1
print(f"Low‑stock items: {low}")
```

> 💡 **INSIGHT:** Use `for item in list` when you only need the values.  
> It’s clean and Pythonic — no index management required.

---

## 🧱 BRICK 2 – Index‑based Iteration and Advanced Looping

Sometimes you need the index or you want to modify the list.  
Use `range(len(list))` or `enumerate()`.

**④ Convert letters to uppercase – using index or comprehension**
```python
chars = ['a', 'b', 'c']
# Method 1: list comprehension (compact)
upper = [ch.upper() for ch in chars]
print(upper)   # ['A', 'B', 'C']

# Method 2: explicit for loop with index
for i in range(len(chars)):
    chars[i] = chars[i].upper()
print(chars)   # ['A', 'B', 'C']
```
The Hard practice task expects you to produce the uppercase list;  
you can use either approach. The engine checks the final output.

**⑤ `enumerate()` – get both index and value**
```python
tasks = ['design', 'code', 'test']
for idx, task in enumerate(tasks):
    print(f"{idx}: {task}")
```
Output:
```
0: design
1: code
2: test
```

**⑥ Modify prices in place with index**
```python
prices = [10, 20, 30]
for i in range(len(prices)):
    prices[i] *= 1.1    # apply 10% tax
print(prices)           # [11.0, 22.0, 33.0]
```

> ⚠️ **WARNING:** Never remove items from a list while iterating directly over it.  
> The indexes shift and elements can be skipped. Either iterate over a copy  
> or build a new list with a comprehension.

> 💡 **ADVANCED TIP – `for` vs. comprehension:**  
> List comprehensions are great for simple transforms (`[x.upper() for x in list]`).  
> If the loop involves multiple steps, conditions, or side effects,  
> stick with a traditional `for` loop for readability.

---

## 💡 Real‑world Usage

**Banking – total all pending transactions**
```python
pending = [200, 150, 320]
sum_pending = 0
for tx in pending:
    sum_pending += tx
print(f"Total pending: {sum_pending}")
```

**E‑commerce – generate a product list with prices**
```python
products = ['laptop', 'mouse']
for product in products:
    print(f"{product}: $99")
```

**Logistics – count parcels above weight limit**
```python
weights = [8, 12, 15, 9, 20]
heavy_count = 0
for w in weights:
    if w > 10:
        heavy_count += 1
print(f"Heavy parcels: {heavy_count}")
```

**HR – print employee badges**
```python
names = ['Emperor', 'Rahim']
for name in names:
    print(f"Badge: {name.upper()}")
```

**Reporting – build a CSV line from fields**
```python
fields = ['2026-07-08', 'Sales', '420']
csv_line = ''
for field in fields:
    csv_line += field + ','
csv_line = csv_line.rstrip(',')
print(csv_line)   # '2026-07-08,Sales,420'
```

---

## 🔍 Practice Preview
You will write three iteration‑based mini‑programs.

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | Sum all numbers in `[1,2,3,4,5]` using a `for` loop. Print the sum. | `15` |
| Medium | Join the words `['apple','banana']` with a space using a loop. Print the result. | `apple banana` |
| Hard   | Convert `['a','b','c']` to uppercase using a loop/comprehension. Print the list. | `['A', 'B', 'C']` |

Run the coach:
```bash
python ii_Practice_Sheets/L-28_Iterating_Through_Lists.py
```
Choose `1`, `2`, or `3`. Type your loop; the engine checks output.

---

## 📌 Key Takeaway
- `for item in list` iterates values directly — ideal for summing, printing, and filtering.
- Use `range(len(list))` or `enumerate()` when you need the index.
- List comprehensions offer a compact alternative for simple transformations.
- Avoid modifying the list you’re iterating over; build a new one instead.
- Iteration is the backbone of business report generation, data cleaning, and batch processing.