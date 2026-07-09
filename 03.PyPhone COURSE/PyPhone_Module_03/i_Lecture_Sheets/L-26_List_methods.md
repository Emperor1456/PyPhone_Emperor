# 📘 PyPhone Emperor · Module 3  
# 📖 L‑26 – List Methods (Add, Remove, Sort Business Data)

---

## 🎯 OBJECTIVE  
Master Python’s built‑in list methods to add, remove, and order elements.  
These are the core operations for managing shopping carts, inventory records,  
transaction logs, and any collection that grows, shrinks, or changes order over time.

---

## 🧱 BRICK 1 – Adding Elements to Lists

Add items with `.append()`, `.insert()`, and `.extend()`.

**① Append a single item to the end**
```python
items = [1, 2, 3]
items.append(4)
print(items)   # [1, 2, 3, 4]
```
Think: adding a new product to a price list,  
or logging a new transaction as it occurs.

**② Insert an item at a specific position**
```python
queue = ['A', 'B', 'D']
queue.insert(2, 'C')      # insert 'C' at index 2
print(queue)              # ['A', 'B', 'C', 'D']
```
Use for priority orders or inserting missing values  
at the correct place in a sequence.

**③ Extend with multiple items from another list**
```python
batch1 = ['order1', 'order2']
batch2 = ['order3', 'order4']
batch1.extend(batch2)
print(batch1)   # ['order1', 'order2', 'order3', 'order4']
```
Perfect for merging two daily sales lists or  
combining multiple supplier deliveries.

> 💡 **INSIGHT:** `.append()` adds exactly one element;  
> `.extend()` unpacks an iterable and adds each element individually.  
> Don’t confuse them — `list.append([1,2])` adds a nested list,  
> `list.extend([1,2])` adds two elements.

---

## 🧱 BRICK 2 – Removing Elements and Sorting

Remove with `.remove()`, `.pop()`, and `.clear()`.  
Reorder with `.sort()` and `.reverse()`.

**④ Remove the first occurrence of a value**
```python
colors = ['red', 'green', 'blue', 'green']
colors.remove('green')   # removes first 'green'
print(colors)            # ['red', 'blue', 'green']
```
Useful for deleting a specific product code or a cancelled order.

**⑤ Pop (remove and return) an item by index**
```python
lst = [1, 2, 3]
popped = lst.pop()   # default index -1 (last)
print(popped)        # 3
print(lst)           # [1, 2]
```
Pop is great for processing a queue:  
handle the next customer and remove them from the waiting list.

**⑥ Pop a specific index**
```python
items = [10, 20, 30]
second = items.pop(1)   # removes element at index 1 (20)
print(second)           # 20
print(items)            # [10, 30]
```

**⑦ Clear all items**
```python
temp = [1, 2, 3]
temp.clear()
print(temp)   # []
```
Use to reset a daily cash register or empty a cart after purchase.

**⑧ Sort a list in place**
```python
lst = [3, 1, 5]
lst.sort()
print(lst)   # [1, 3, 5]
```
Sort ascending (default) or descending with `reverse=True`.

**⑨ Reverse the order without sorting**
```python
nums = [1, 2, 3]
nums.reverse()
print(nums)   # [3, 2, 1]
```

> ⚠️ **WARNING:** `.sort()` and `.reverse()` modify the original list  
> and return `None`. Never do `result = lst.sort()` — it will give `None`.

> 💡 **ADVANCED TIP – `sorted()` for a new list:**  
> Use `sorted(lst)` to get a sorted copy without changing the original.  
> This is safer when you need the original order preserved elsewhere.

---

## 💡 Real‑world Usage

**Banking – maintain a live transaction log**
```python
log = []
log.append('deposit 200')
log.append('withdraw 50')
print(log)   # ['deposit 200', 'withdraw 50']
```

**E‑commerce – manage a shopping cart**
```python
cart = ['laptop', 'mouse']
cart.append('keyboard')
cart.remove('mouse')
print(cart)   # ['laptop', 'keyboard']
```

**Logistics – sort delivery addresses alphabetically**
```python
addresses = ['Dhaka', 'Chittagong', 'Khulna']
addresses.sort()
print(addresses)   # ['Chittagong', 'Dhaka', 'Khulna']
```

**HR – pop the next candidate from a interview queue**
```python
candidates = ['CandidateA', 'CandidateB', 'CandidateC']
next_up = candidates.pop(0)   # FIFO: remove first
print(next_up)                 # CandidateA
print(candidates)              # ['CandidateB', 'CandidateC']
```

**Reporting – merge weekly sales data**
```python
week1 = [200, 150]
week2 = [300, 400]
week1.extend(week2)
print(week1)   # [200, 150, 300, 400]
```

---

## 🔍 Practice Preview
You will write three list‑method mini‑programs.

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | `items=[1,2,3]`. Append 4, then print the list. | `[1, 2, 3, 4]` |
| Medium | `lst=[3,1,5]`. Sort it and print the sorted list. | `[1, 3, 5]`    |
| Hard   | `lst=[1,2,3]`. Pop the last element, print it, then print the remaining list. | `3`<br>`[1, 2]` |

Run the coach:
```bash
python ii_Practice_Sheets/L-26_List_Methods.py
```
Choose `1`, `2`, or `3`. Type the code; the engine checks output.

---

## 📌 Key Takeaway
- `.append(item)` adds to the end; `.insert(idx, item)` adds at a specific position.
- `.extend(iterable)` merges another collection’s items.
- `.remove(value)` deletes the first match; `.pop(idx)` removes and returns.
- `.sort()` orders the list in place; `.reverse()` flips the order.
- Most list methods return `None` — they change the list directly, so don’t assign.