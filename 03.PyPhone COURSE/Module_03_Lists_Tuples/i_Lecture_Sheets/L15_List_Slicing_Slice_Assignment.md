# 📘 PyPhone Emperor v3.0 · Module 3
# 📖 L‑15 – List Slicing & Slice Assignment

---

## 🎯 OBJECTIVE — What You Will Master

> Advanced list slicing for extraction and in‑place modification.

- ✂️ **Slicing** – extract any contiguous segment
- 🔄 **Slice assignment** – replace a segment with new values
- ➕ **Insert/Delete** – using empty slice assignment
- 🧪 **Real‑world** – batch updates, log trimming

---

## 🧱 EXTRACTING SUB‑LISTS

```python
nums = [1, 2, 3, 4, 5]
print(nums[1:4])      # [2, 3, 4]
print(nums[2:])       # [3, 4, 5]
print(nums[:3])       # [1, 2, 3]
```

---

## 🧱 SLICE ASSIGNMENT

Replace any segment, even with a list of different length.

```python
data = [0, 1, 2, 3, 4]
data[1:4] = [10, 20]      # replace indices 1-3 with two items
print(data)               # [0, 10, 20, 4]
```

**Insert with empty slice:**
```python
data[2:2] = [100]         # insert without removing
print(data)               # [0, 10, 100, 20, 4]
```

**Delete with slice assignment:**
```python
data[1:3] = []             # remove elements at indices 1,2
print(data)                # [0, 20, 4]
```

---

## 💡 Real‑world Usage

**Banking – replace recent transactions**
```python
tx = [10, 20, 30, 40]
tx[1:3] = [25, 35]   # correct two entries
```

**E‑commerce – update product list**
```python
products = ["A", "B", "C", "D"]
products[0:2] = ["X", "Y"]   # replace first two
```

**Logistics – insert a stop**
```python
route = ["A", "B", "D"]
route[2:2] = ["C"]    # insert at position 2
```

---

## 🔍 Practice Preview

| Level | Task | What You’ll Write |
|-------|------|-------------------|
| Easy | Print sublist `[2,3,4]` from `[1,2,3,4,5]`. | `print(nums[1:4])` |
| Medium | Replace middle two items in `[1,2,3,4]` with `[8,9]` and print. | `lst[1:3]=[8,9]; print(lst)` |
| Hard | Delete the second and third items using slice assignment and print. | `lst[1:3]=[]; print(lst)` |

Run the coach:
```bash
python ii_Practice_Sheets/L15_List_Slicing_Slice_Assignment.py
```

---

## 📌 Key Takeaway
- Slicing extracts sub‑lists safely.
- Slice assignment modifies the list in place.
- Empty slices can insert or delete elements elegantly.

*For Emperor.*