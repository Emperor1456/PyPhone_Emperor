# 📘 PyPhone Emperor v3.0 · Module 2
# 📖 L‑10 – `while` Loops – Sentinel‑Controlled Repetition

---

## 🎯 OBJECTIVE — What You Will Master

> Keep repeating until a condition fails – the backbone of interactive tools and data input.

- 🔁 **`while` loop** – repeat as long as a condition is `True`
- 🧹 **Sentinel value** – a special value that stops the loop
- ⚡ **Infinite loops & `break`** – how to safely stop
- 🧪 **Input validation** – keep asking until the data is correct

---

## 🧱 THE `while` LOOP

```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

The loop runs as long as `count <= 5`.  
If you forget `count += 1`, the loop runs forever → hit `Ctrl+C`.

**Business example – inventory restock countdown**
```python
items_left = 5
while items_left > 0:
    print(f"Packing item… {items_left} remaining")
    items_left -= 1
print("Shipment ready")
```

---

## 🧱 SENTINEL‑CONTROLLED LOOP

A sentinel value signals the end of input.

```python
total = 0
price = float(input("Price (-1 to stop): "))
while price != -1:
    total += price
    price = float(input("Price (-1 to stop): "))
print(f"Total: ${total:.2f}")
```

**Business example – enter sales until 0**
```python
sales = []
sale = input("Sale amount (0 to finish): ")
while sale != "0":
    sales.append(float(sale))
    sale = input("Sale amount (0 to finish): ")
print(f"Total sales: {sum(sales):.2f}")
```

> ⚠️ **WARNING:** Always ensure the sentinel is of the correct type. If you compare a string to an integer, the loop may never stop.

---

## 🧱 `while True` WITH `break`

Sometimes the end condition is not at the beginning – use `while True` and `break`.

```python
while True:
    cmd = input("Command: ").lower()
    if cmd == "quit":
        break
    print(f"Executing {cmd}")
```

---

## 💡 Real‑world Usage

**Banking – withdraw until sufficient balance**
```python
balance = 500
while balance > 0:
    amount = float(input("Withdraw: "))
    if amount > balance:
        print("Insufficient")
        continue
    balance -= amount
print("Account empty")
```

**E‑commerce – add items to cart until 'done'**
```python
cart = []
while True:
    item = input("Item (type 'done' to finish): ")
    if item == "done":
        break
    cart.append(item)
print(f"Cart: {cart}")
```

**Logistics – load parcels until weight limit**
```python
max_weight = 50
loaded = 0
while loaded + 10 <= max_weight:
    loaded += 10
    print(f"Loaded 10kg, total {loaded}kg")
print("Truck full")
```

---

## 🔍 Practice Preview

| Level | Task | What You’ll Write |
|-------|------|-------------------|
| Easy | Sum numbers from 1 to 4 using `while`. | `total=0; i=1; while i<=4: …` |
| Medium | Compute factorial of 4 using `while`. | `n=4; prod=1; while n>0: …` |
| Hard | Count how many times you can double 1 before exceeding 20. | `x=1; count=0; while x<=20: x*=2; count+=1` |

Run the coach:
```bash
python ii_Practice_Sheets/L10_while_Loops_Sentinel_Repetition.py
```

---

## 📌 Key Takeaway
- `while` repeats while a condition is `True`.
- Always update the variable that controls the condition.
- Sentinel loops use a special value to stop.
- `while True` + `break` handles arbitrary termination.

*For Emperor.*