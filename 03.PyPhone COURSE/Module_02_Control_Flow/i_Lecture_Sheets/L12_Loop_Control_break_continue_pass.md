# 📘 PyPhone Emperor v3.0 · Module 2
# 📖 L‑12 – Loop Control – `break`, `continue`, `pass`

---

## 🎯 OBJECTIVE — What You Will Master

> Command your loops with surgical precision.

- 🛑 **`break`** – exit the loop immediately
- ⏩ **`continue`** – skip the rest of this iteration, go to the next
- 🧪 **`pass`** – do nothing, a placeholder
- 🧠 **Use‑cases** – early search termination, filtering, stubs

---

## 🧱 `break` – STOP THE LOOP NOW

When `break` executes, the loop ends instantly.

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)   # prints 1 2 3 4
```

**Business – find first high‑value transaction**
```python
amounts = [120, 55, 430, 2100]
for amt in amounts:
    if amt > 2000:
        print(f"Alert: {amt}")
        break
```

---

## 🧱 `continue` – SKIP THIS ONE

`continue` jumps to the next iteration, ignoring the rest of the loop body.

```python
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(i)   # prints 1 3 5
```

**Business – process only active accounts**
```python
accounts = ["active", "inactive", "active"]
for status in accounts:
    if status != "active":
        continue
    print("Sending statement")
```

---

## 🧱 `pass` – NOTHING TO SEE HERE

`pass` is a no‑op – it does nothing. Use it when a statement is syntactically required but you haven’t implemented the logic yet.

```python
if condition:
    pass   # TODO: implement later
```

**Business – placeholder for future feature**
```python
def future_feature():
    pass   # Will be added in next sprint
```

> ⚠️ **WARNING:** `pass` can hide incomplete logic; always add a `# TODO` comment.

---

## 💡 Real‑world Usage

**Banking – skip zero‑value transactions**
```python
txs = [100, 0, 200, 0, 50]
for tx in txs:
    if tx == 0:
        continue
    print(f"Processing ${tx}")
```

**E‑commerce – stop processing on error**
```python
orders = ["OK", "OK", "FAIL", "OK"]
for status in orders:
    if status == "FAIL":
        print("Stopping batch")
        break
    print("Order processed")
```

**Logistics – placeholder for international shipping**
```python
def international_shipping():
    pass   # coming soon
```

---

## 🔍 Practice Preview

| Level | Task | What You’ll Write |
|-------|------|-------------------|
| Easy | Search for 3 in `[1,2,3,4]`, break when found, print "Found". | `for x in [1,2,3,4]: if x==3: print("Found"); break` |
| Medium | Print odd numbers from 1 to 6 using `continue`. | `for i in range(1,7): if i%2==0: continue; print(i)` |
| Hard | Sum numbers 1 to 10 with `while`, break when sum exceeds 30. | `res=0; i=1; while i<=10: res+=i; if res>30: break; i+=1` |

Run the coach:
```bash
python ii_Practice_Sheets/L12_Loop_Control_break_continue_pass.py
```

---

## 📌 Key Takeaway
- `break` exits the loop completely.
- `continue` skips to the next iteration.
- `pass` is a placeholder for future code.

*For Emperor.*