# 📘 PyPhone Emperor · Module 3  
# 📖 L‑27 – List Slicing & Comprehensions (Data Transformation)

---

## 🎯 OBJECTIVE  
Master advanced list slicing for extracting portions of business data, and **list comprehensions** for transforming and filtering lists in a single, readable line.  
These are the tools for generating daily summaries, filtering high‑value transactions, and converting raw data into reports.

---

## 🧱 BRICK 1 – Advanced Slicing and Slice Assignment

Slicing extracts a sub‑list using `list[start:stop]`.  
`start` is inclusive, `stop` is exclusive.

**① Extract a sub‑list of sales from a weekly record**
```python
nums = [1, 2, 3, 4, 5]
middle = nums[1:4]      # indices 1,2,3 → [2, 3, 4]
print(middle)            # [2, 3, 4]
```
This is the Easy practice task — directly applied to extracting a range of transaction amounts.

**② Replace a slice with new values**
```python
sales = [100, 200, 300, 400]
sales[1:3] = [250, 350]    # replace indices 1 and 2
print(sales)               # [100, 250, 350, 400]
```

**③ Insert with an empty slice**
```python
data = [10, 20, 30]
data[1:1] = [15]           # insert at index 1
print(data)                # [10, 15, 20, 30]
```

**④ Delete a slice by assigning an empty list**
```python
data[2:4] = []             # remove indices 2 and 3
print(data)                # [10, 15]
```

> 💡 **INSIGHT:** Slicing never raises an error — if the range is invalid, you get an empty list.  
> It’s safer than direct indexing when you don’t know the exact length.

---

## 🧱 BRICK 2 – List Comprehensions (Transformation & Filtering)

A list comprehension builds a new list from an existing one,  
applying an expression and optional filter in one clean line.

**Basic syntax:**
```python
[expression for item in iterable if condition]
```

**⑤ Square each number (Medium practice task)**
```python
nums = [1, 2, 3, 4]
squares = [x * x for x in nums]
print(squares)   # [1, 4, 9, 16]
```
This transforms raw quantities into derived values — like calculating tax from net prices.

**⑥ Filter only even numbers (Hard practice task)**
```python
evens = [x for x in [1, 2, 3, 4, 5, 6] if x % 2 == 0]
print(evens)    # [2, 4, 6]
```
Use this to extract active orders, approved transactions, or items above a threshold.

**⑦ Convert product codes to uppercase**
```python
codes = ['a1', 'b2', 'c3']
upper_codes = [code.upper() for code in codes]
print(upper_codes)   # ['A1', 'B2', 'C3']
```

**⑧ Filter high‑value transactions**
```python
amounts = [120, 340, 80, 990]
large = [a for a in amounts if a > 200]
print(large)   # [340, 990]
```

> 💡 **ADVANCED TIP – Comprehension vs. `for` loop:**  
> Comprehensions are faster and more compact, but don’t over‑nest them.  
> If the logic needs multiple steps, a regular `for` loop is clearer.  
> Use `[x for x in ... if ...]` for simple filters, and a loop for complex business rules.

> ⚠️ **WARNING:** A comprehension always builds a **new** list — the original is unchanged.  
> This is good for immutability, but large comprehensions consume memory.

---

## 💡 Real‑world Usage

**Banking – filter transactions above a reporting threshold**
```python
txs = [500, 1200, 300, 800, 2100]
reportable = [t for t in txs if t > 1000]
print(reportable)   # [1200, 2100]
```

**E‑commerce – apply a discount to all prices**
```python
prices = [100, 200, 300]
discounted = [p * 0.9 for p in prices]
print(discounted)   # [90.0, 180.0, 270.0]
```

**Logistics – extract delivery weights below a limit**
```python
weights = [15, 22, 8, 35, 12]
light = [w for w in weights if w <= 15]
print(light)   # [15, 8, 12]
```

**HR – generate email addresses from names**
```python
names = ['emperor', 'rahim', 'karim']
emails = [name + '@company.com' for name in names]
print(emails)
```

**Reporting – create a list of daily totals from hour‑by‑hour data**
```python
hours = [10, 20, 30, 40, 50, 60, 70, 80]
daily_totals = hours[2:5]   # mid‑day snapshot
print(daily_totals)         # [30, 40, 50]
```

---

## 🔍 Practice Preview
You will write three list‑transformation mini‑programs.

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | `nums=[1,2,3,4,5]`. Print sublist `[2,3,4]` using slicing. | `[2, 3, 4]` |
| Medium | `nums=[1,2,3,4]`. Create list of squares using comprehension. Print it. | `[1, 4, 9, 16]` |
| Hard   | From `[1,2,3,4,5,6]`, use comprehension to keep only evens. Print the list. | `[2, 4, 6]` |

Run the coach:
```bash
python ii_Practice_Sheets/L-27_List_Slicing_Comprehensions.py
```
Choose `1`, `2`, or `3`. Type your code; the engine checks output.

---

## 📌 Key Takeaway
- Slicing `list[start:stop]` extracts a sub‑list safely and never crashes.
- Slice assignment can replace, insert, or delete elements in place.
- List comprehensions `[expr for item in iterable if cond]` create new lists in one line.
- Use comprehensions for simple transformations and filters; prefer loops for complex logic.
- Essential for cleaning, filtering, and reformatting business datasets.