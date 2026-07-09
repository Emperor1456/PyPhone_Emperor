# 📘 PyPhone Emperor · Module 2  
# 📖 L‑19 – The `while` Loop (Repetition for Business Processes)

---

## 🎯 OBJECTIVE  
Master the `while` loop to repeat a code block as long as a condition holds true.  
Use it when the number of repetitions isn’t known in advance — for instance,  
processing transactions until a cutoff, validating input, or accumulating totals.  
The loop must eventually make the condition false, or the program freezes.

---

## 🧱 BRICK 1 – Basic `while` Mechanics

```python
while condition:
    # block runs repeatedly while condition is True
```

The condition is checked **before every iteration**.  
If it’s `True`, the body runs; if `False`, the loop ends.

**① Summation accumulator – daily sales total**
```python
total = 0
i = 1
while i <= 4:
    total += i
    i += 1
print(total)
```
- `i` starts at 1.  
- Loop runs for i=1,2,3,4 → total becomes 1+2+3+4 = 10.  
- When i becomes 5, `5 <= 4` is `False` → loop stops.  
- Prints `10`.

**② Countdown with a business timer**
```python
timer = 3
while timer > 0:
    print(f"Processing batch in {timer}...")
    timer -= 1
print("Batch completed.")
```
Output:  
Processing batch in 3...  
Processing batch in 2...  
Processing batch in 1...  
Batch completed.

**③ Input validation – minimum transaction amount**
```python
amount = 0
while amount <= 0:
    amount = float(input("Enter positive amount: "))
print(f"Transaction approved: ${amount}")
```
The loop forces the user to enter a positive number.

> 💡 **INSIGHT:** A `while` loop is like an `if` that repeats.  
> The body **must** change something that eventually makes the condition false.

> ⚠️ **WARNING:** Forgetting the increment (`i += 1` or `timer -= 1`) creates an infinite loop.  
> Use Ctrl+C to stop a runaway program.

---

## 🧱 BRICK 2 – Business Algorithms with `while`

**④ Factorial calculation – product of all numbers from n down to 1**
```python
n = 4
prod = 1
while n > 0:
    prod *= n
    n -= 1
print(prod)
```
- 4 * 3 * 2 * 1 = 24.  
- `n` decreases each iteration until it reaches 0.

**⑤ Growth tracking – doubling an investment until threshold**
```python
x = 1
count = 0
while x <= 20:
    x *= 2
    count += 1
print(count)
```
- 1 → 2 → 4 → 8 → 16 → 32 (exceeds 20 after 5 doublings).  
- `count` records how many times the loop ran → 5.

**⑥ Processing a queue of pending orders**
```python
orders_left = 5
while orders_left > 0:
    print(f"Fulfilling order. {orders_left} remaining.")
    orders_left -= 1
print("All orders shipped.")
```
This pattern is used in batch job processing.

**⑦ Sentinel‑controlled loop – user quits with -1**
```python
total = 0
num = int(input("Enter amount (-1 to finish): "))
while num != -1:
    total += num
    num = int(input("Enter amount (-1 to finish): "))
print(f"Total: ${total}")
```
The sentinel value `-1` stops the loop.

> 💡 **ADVANCED TIP – `while True` with `break`:**  
> You can create a loop that runs indefinitely and exit manually:
> ```python
> while True:
>     cmd = input("Command: ")
>     if cmd == "quit":
>         break
>     print(f"Executing {cmd}")
> ```
> This is common in interactive menus and CLI tools.

---

## 💡 Real‑world Usage

**Banking – compound interest over months**
```python
balance = 1000
months = 0
while balance < 1500:
    balance *= 1.005   # 0.5% monthly interest
    months += 1
print(f"Reached ${balance:.2f} after {months} months")
```

**Inventory – restock alert**
```python
stock = 20
while stock > 5:
    print(f"Stock OK: {stock}")
    stock -= 1
print("Reorder now!")
```

**Logistics – loading a truck until weight limit**
```python
total_weight = 0
while total_weight + 50 <= 500:
    total_weight += 50
    print(f"Added 50kg, total: {total_weight}kg")
print("Truck full.")
```

**HR – processing employee timesheets**
```python
employees = 3
while employees > 0:
    hours = float(input("Enter hours: "))
    print(f"Pay: ${hours * 20}")
    employees -= 1
print("Payroll complete.")
```

---

## 🔍 Practice Preview
You will write three `while`‑driven mini‑programs that reflect real business calculations.

| Level  | Task                                                                 | Expected Output |
|--------|----------------------------------------------------------------------|-----------------|
| Easy   | Sum numbers from 1 to 4 using a `while` loop. Print the total.       | `10`            |
| Medium | Compute factorial of 4 using `while`. Print the result.              | `24`            |
| Hard   | Count how many times you can double 1 before exceeding 20. Print the count. | `5`             |

Run the coach:
```bash
python ii_Practice_Sheets/L-19_while_loop.py
```
Choose `1`, `2`, or `3`. Type the loop; the engine checks your output.

---

## 📌 Key Takeaway
- `while` repeats a block as long as its condition is `True`.
- Always update a variable inside the loop to eventually exit.
- Use for accumulators, validators, sentinel patterns, and growth tracking.
- `while True` + `break` is the standard for interactive menus.
- Infinite loops freeze programs — test carefully and save often.