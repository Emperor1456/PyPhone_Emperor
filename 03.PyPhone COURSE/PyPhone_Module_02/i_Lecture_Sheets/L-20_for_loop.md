# 📘 PyPhone Emperor · Module 2  
# 📖 L‑20 – The `for` Loop (Iteration for Business Sequences)

---

## 🎯 OBJECTIVE  
Master the `for` loop to iterate over sequences — ranges, lists, strings — with a fixed number of repetitions.  
Use it to sum invoice line items, build transaction codes, generate reports from datasets, and process batches.  
Cleaner and safer than `while` when you know exactly how many elements you have.

---

## 🧱 BRICK 1 – Looping Over Numbers with `range()` and Simple Lists

```python
for variable in sequence:
    # block runs once for each item in the sequence
```

**① Summing a fixed set of invoice amounts**
```python
items = [1, 2, 3, 4, 5]
total = 0
for x in items:
    total += x
print(total)   # 15
```
`x` takes each value in the list; the loop adds them up.

**② Tallying daily sales using `range`**
```python
daily_sales = 0
for day in range(1, 6):      # 1,2,3,4,5
    sale = 100
    daily_sales += sale
print(daily_sales)            # 500
```
`range(1,6)` gives five iterations – one for each business day.

**③ Generating a receipt number sequence**
```python
for i in range(1001, 1006):
    print(f"Receipt #{i}")
```
Output: Receipt #1001, #1002, #1003, #1004, #1005.  
`range(start, stop)` runs from start to stop-1.

> 💡 **INSIGHT:** `range()` is efficient — it doesn't create a huge list,  
> just generates the next number on the fly. Perfect for large loops.

---

## 🧱 BRICK 2 – Iterating Over Characters, Strings, and Building Lists

A `for` loop can directly walk through any iterable:  
strings, tuples, lists, and more.

**④ Assembling a product code from individual characters**
```python
letters = ['h', 'e', 'l', 'l', 'o']
result = ''
for ch in letters:
    result += ch
print(result)   # 'hello'
```
Each character is appended to `result`.  
This pattern reconstructs codes, serial numbers, or message strings.

**⑤ Building a list of even transaction IDs for batch processing**
```python
even_ids = []
for i in range(1, 11):
    if i % 2 == 0:
        even_ids.append(i)
print(even_ids)   # [2, 4, 6, 8, 10]
```
- `range(1,11)` → 1 to 10.  
- Only even numbers are added to the list via `.append()`.  
- The final list is printed exactly as the practice expects: `[2, 4, 6, 8, 10]`.

**⑥ Extracting order codes from a formatted string**
```python
order_codes = "A1-B2-C3"
for code in order_codes.split('-'):
    print(f"Processing {code}")
```
`.split('-')` returns `['A1', 'B2', 'C3']`.  
The loop dispatches each code.

> 💡 **ADVANCED TIP – List comprehensions (preview):**  
> The even‑id loop above can be written in one line:  
> `even_ids = [i for i in range(1,11) if i % 2 == 0]`.  
> This compact form is a Python hallmark. You’ll master it later.

> ⚠️ **WARNING:** Don’t modify a list while iterating over it — results can be unpredictable.  
> Build a new list instead, as in example ⑤.

---

## 💡 Real‑world Usage

**Banking – sum of monthly fees**
```python
fees = [5, 5, 5, 5, 10]
total_fees = 0
for fee in fees:
    total_fees += fee
print(f"Total fees: ${total_fees}")
```

**E‑commerce – generating SKU strings**
```python
prefix = "SKU-"
codes = ['A1', 'B2', 'C3']
for code in codes:
    print(prefix + code)
```

**Logistics – loading a shipment with fixed item counts**
```python
item_weights = [12, 8, 15, 10]
total_weight = 0
for w in item_weights:
    total_weight += w
print(f"Total weight: {total_weight}kg")
```

**HR – checking employee access levels**
```python
employees = ['Emperor', 'Rahim', 'Karim']
for emp in employees:
    print(f"Granting access to {emp}")
```

**Reporting – generating daily summaries**
```python
week_sales = [200, 350, 280, 410, 390]
for day, amount in enumerate(week_sales, start=1):
    print(f"Day {day}: ${amount}")
```

---

## 🔍 Practice Preview
You will write three `for`‑loop scripts that solve typical business tasks.

| Level  | Task                                                                 | Expected Output    |
|--------|----------------------------------------------------------------------|--------------------|
| Easy   | Sum numbers in list `[1,2,3,4,5]` using a `for` loop. Print the sum. | `15`               |
| Medium | Concatenate characters `['h','e','l','l','o']` into a string. Print it. | `hello`            |
| Hard   | Generate list of even numbers from 1 to 10 using `for` and `range`. Print the list. | `[2, 4, 6, 8, 10]` |

Run the coach:
```bash
python ii_Practice_Sheets/L-20_for_loop.py
```
Choose `1`, `2`, or `3`. Type your loop; the engine checks output.

---

## 📌 Key Takeaway
- `for` iterates over every item in a sequence (range, list, string, etc.).
- Use `range(start, stop)` when you need a specific number of iterations.
- Build up results (sums, strings, lists) inside the loop body.
- `for` is ideal when the number of items is known — safer than `while` for fixed collections.
- Append to lists with `.append()` to create dynamic datasets.