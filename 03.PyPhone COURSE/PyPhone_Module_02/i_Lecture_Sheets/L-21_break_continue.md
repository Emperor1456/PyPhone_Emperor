# 📘 PyPhone Emperor · Module 2  
# 📖 L‑21 – `break` and `continue` (Precision Loop Control)

---

## 🎯 OBJECTIVE  
Master `break` and `continue` to control loop flow in business processes.  
`break` exits the loop instantly when a target is found or a limit reached.  
`continue` skips the rest of the current iteration and moves to the next.  
Together they give you surgical control over loops — essential for search,  
filtering, early termination, and batch processing.

---

## 🧱 BRICK 1 – `break`: Stop the Loop on Condition

`break` immediately ends the loop.  
The program continues with the first statement after the loop.

```python
for item in sequence:
    if condition:
        break   # loop ends here
    # other code
```

**① Search for a specific transaction ID**
```python
transactions = [1, 2, 3, 4]
for x in transactions:
    if x == 3:
        print('Found')
        break
```
As soon as `x` equals 3, the loop stops.  
Only `'Found'` is printed, not 4 or anything else.  
This is the exact logic of the Easy practice task.

**② Fraud detection – stop processing on red flag**
```python
amounts = [120, 55, 430, 99, 2100]
for amt in amounts:
    if amt > 2000:
        print(f"Alert: High value transaction ${amt}")
        break
    print(f"Processing ${amt}")
```
When 2100 is encountered, the loop exits, skipping the remaining amounts.

**③ Inventory restock alert – find first low stock item**
```python
stock_levels = [35, 42, 8, 27, 50]
for qty in stock_levels:
    if qty < 10:
        print(f"Reorder needed: only {qty} left!")
        break
```
The loop stops at the first product below 10, saving time.

> 💡 **INSIGHT:** `break` is perfect for search‑and‑exit tasks.  
> You don’t waste cycles processing data after your goal is reached.

> ⚠️ **WARNING:** Ensure the loop condition or the `break` itself  
> is reachable. A poorly placed `break` can make a loop useless,  
> while a missing `break` may lead to an infinite loop.

---

## 🧱 BRICK 2 – `continue`: Skip an Iteration

`continue` jumps back to the top of the loop,  
ignoring the rest of the current iteration’s code.

```python
for item in sequence:
    if skip_condition:
        continue   # jump to next item
    # process item
```

**④ Print only odd numbers – filter even ones**
```python
for i in range(1, 7):
    if i % 2 == 0:
        continue
    print(i)
```
Output:
```
1
3
5
```
Even numbers (2,4,6) trigger `continue`, so `print(i)` is skipped.  
This matches the Medium practice task exactly.

**⑤ Process only active customer accounts**
```python
accounts = ['active', 'inactive', 'active', 'suspended']
for status in accounts:
    if status != 'active':
        continue
    print("Sending statement...")
```
Statements are sent only to `'active'` customers; all others are skipped.

**⑥ Skip negative values in sales report**
```python
sales = [200, -5, 340, -20, 150]
total = 0
for sale in sales:
    if sale < 0:
        continue   # ignore returns/errors
    total += sale
print(total)   # 690
```
Negative entries are skipped, building a clean total.

> 💡 **ADVANCED TIP – `break` and `continue` together in a complex loop:**  
> You can mix both in one loop. For example, accumulate payments until  
> a target balance is reached (`break`), but skip zero‑amount entries (`continue`).

```python
payments = [100, 0, 200, 0, 350]
target = 500
collected = 0
for pay in payments:
    if pay == 0:
        continue   # skip zero payments
    collected += pay
    if collected >= target:
        break
print(collected)   # 300 (100+200; next would exceed but loop already exited)
```

**⑦ Hard task – sum numbers until a threshold (combined approach)**
```python
res = 0
i = 1
while i <= 10:
    res += i
    if res > 30:
        break
    i += 1
print(res)
```
- Add numbers 1,2,3…  
- After adding 1..8, sum becomes 36 (>30), loop breaks.  
- Prints `36`, exactly the Hard practice expected output.  
- Notice: `i` increment must come before or inside the loop;  
  careful placement ensures correctness.

> ⚠️ **WARNING:** With `while`, be extra cautious with `continue` —  
> it can skip the increment step and create an infinite loop.  
> Always test small loops first.

---

## 💡 Real‑world Usage

**Banking – scan for suspicious transactions and stop**
```python
transactions = [45, 120, 999, 3000]
for tx in transactions:
    if tx > 2000:
        print("Fraud alert – stopping batch")
        break
    print(f"Approved: ${tx}")
```

**E‑commerce – skip out‑of‑stock items in order list**
```python
order_items = ['shirt', 'socks', 'hat']
stock = {'shirt': 0, 'socks': 5, 'hat': 3}
for item in order_items:
    if stock.get(item, 0) == 0:
        continue
    print(f"Packing {item}")
```
Only 'socks' and 'hat' are packed; 'shirt' is skipped.

**Logistics – stop loading when weight limit reached**
```python
cargo = [50, 60, 80, 30]
max_weight = 150
loaded = 0
for w in cargo:
    if loaded + w > max_weight:
        break
    loaded += w
    print(f"Loaded {w}kg, total {loaded}kg")
print(f"Shipment total: {loaded}kg")
```

**HR – list only employees with performance >= 80**
```python
scores = [76, 82, 59, 91, 68]
for s in scores:
    if s < 80:
        continue
    print(f"Bonus eligible: score {s}")
```

**Reporting – generate summary for weekdays, skip weekends**
```python
import datetime
start = datetime.date(2026, 6, 1)
for day_offset in range(7):
    d = start + datetime.timedelta(days=day_offset)
    if d.weekday() >= 5:   # Saturday=5, Sunday=6
        continue
    print(f"Report for {d}")
```

---

## 🔍 Practice Preview
You will write three loops that use `break` and `continue` for real business tasks.

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | Search for 3 in `[1,2,3,4]`. Break when found and print `'Found'`. | `Found`         |
| Medium | Print odd numbers from 1 to 6. Use `continue` to skip evens.        | `1`<br>`3`<br>`5` |
| Hard   | Sum numbers 1 to 10 using a `while` loop. Stop when the sum exceeds 30 with `break`. Print the sum. | `36`            |

Run the coach:
```bash
python ii_Practice_Sheets/L-21_break_continue.py
```
Choose `1`, `2`, or `3`. Type the loop; the engine checks your output.

---

## 📌 Key Takeaway
- `break` ends the loop immediately — use for early exit on a found condition.
- `continue` skips the rest of the current iteration — use for filtering.
- Both work with `for` and `while` loops.
- `break` stops the whole loop; `continue` only skips one round.
- In `while` loops, ensure `continue` doesn’t skip the update that changes the condition.
- Combine them for powerful, efficient loops in transaction processing, validation, and search.