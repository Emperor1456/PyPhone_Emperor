# 📘 PyPhone Emperor v3.0 · Module 3
# 📖 L‑14 – List Methods – Add, Remove, Sort

---

## 🎯 OBJECTIVE — What You Will Master

> Manipulate lists with built‑in methods.

- ➕ **Adding**: `append()`, `insert()`, `extend()`
- ➖ **Removing**: `remove()`, `pop()`, `clear()`
- 🔄 **Sorting**: `sort()`, `reverse()`
- 🧪 **Business patterns** – cart management, queue processing

---

## 🧱 ADDING ELEMENTS

```python
tasks = ["write code", "test"]
tasks.append("deploy")         # end
tasks.insert(1, "review")      # at index 1
tasks.extend(["monitor", "report"])   # merge lists
print(tasks)
```

**Business – add items to cart**
```python
cart = ["laptop", "mouse"]
cart.append("keyboard")
print(cart)   # ['laptop', 'mouse', 'keyboard']
```

---

## 🧱 REMOVING ELEMENTS

```python
items = ["a", "b", "c", "b"]
items.remove("b")    # first occurrence
last = items.pop()   # last item (returns it)
print(last)          # b
items.clear()        # empty the list
```

**Business – process a queue**
```python
queue = ["customer1", "customer2", "customer3"]
next_up = queue.pop(0)   # remove first
print(f"Serving {next_up}")
```

---

## 🧱 SORTING & REVERSING

```python
nums = [3, 1, 4, 1, 5]
nums.sort()
print(nums)             # [1, 1, 3, 4, 5]
nums.reverse()
print(nums)             # [5, 4, 3, 1, 1]
```

> ⚠️ **WARNING:** `sort()` and `reverse()` modify the original list and return `None`. Don’t assign the result.

---

## 💡 Real‑world Usage

**Banking – transaction log**
```python
log = []
log.append("deposit 200")
log.append("withdraw 50")
```

**E‑commerce – sort by price**
```python
prices = [19.99, 5.99, 24.99]
prices.sort()
print(prices)
```

**HR – sort applicants**
```python
applicants = ["Rahim", "Emperor", "Karim"]
applicants.sort()
print(applicants)
```

---

## 🔍 Practice Preview

| Level | Task | What You’ll Write |
|-------|------|-------------------|
| Easy | Append 4 to `[1,2,3]` and print. | `lst.append(4); print(lst)` |
| Medium | Sort `[3,1,5]` and print. | `lst.sort(); print(lst)` |
| Hard | Pop the last element from `[1,2,3]`, print it, then print the remaining list. | `popped=lst.pop(); print(popped); print(lst)` |

Run the coach:
```bash
python ii_Practice_Sheets/L14_List_Methods_Add_Remove_Sort.py
```

---

## 📌 Key Takeaway
- `append()`, `insert()`, `extend()` add items.
- `remove()`, `pop()`, `clear()` delete items.
- `sort()` and `reverse()` reorder in place.

*For Emperor.*