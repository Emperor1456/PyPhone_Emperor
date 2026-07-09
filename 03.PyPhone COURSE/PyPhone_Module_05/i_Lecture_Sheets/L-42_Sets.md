# 📘 PyPhone Emperor · Module 5  
# 📖 L‑42 – Sets – Unordered Unique Elements (Deduplication & Membership)

---

## 🎯 OBJECTIVE  
Master **sets** — unordered collections of unique elements. Sets automatically remove duplicates and support lightning‑fast membership tests.  
Use them to extract unique values, validate against permitted lists, and manage tag systems in business applications.

---

## 🧱 BRICK 1 – Creating Sets and Basic Operations

**① Create a set (Easy practice)**
```python
s = {1, 2, 3}
print(s)   # {1, 2, 3}  (order may vary)
```
Curly braces define a set; elements must be immutable.

**② Add an element (Medium practice)**
```python
s = {1, 2, 3}
s.add(4)
print(s)   # {1, 2, 3, 4}
```

**③ Remove duplicates from a list (Hard practice)**
```python
lst = [1, 2, 2, 3, 3, 3]
unique = sorted(set(lst))
print(unique)   # [1, 2, 3]
```
Convert to set to remove duplicates, then back to list and sort for predictable order.

> 💡 **INSIGHT:** Sets are unordered — you cannot index them. Use `sorted()` for a predictable list order.

---

## 🧱 BRICK 2 – Fast Membership and Set Methods

**④ Membership test (very fast)**
```python
valid_codes = {'A1', 'B2', 'C3'}
if 'A1' in valid_codes:
    print('Valid code')
```

**⑤ Remove elements safely**
```python
s.discard(5)   # no error if 5 is missing
s.remove(2)    # raises KeyError if missing
```

**⑥ Update with multiple elements**
```python
s.update([7, 8, 9])   # adds all elements from the iterable
```

**⑦ Set from string characters**
```python
chars = set('hello')
print(chars)   # {'h', 'e', 'l', 'o'}
```

> ⚠️ **WARNING:** Empty set must be created with `set()`, not `{}` (which is an empty dict).  
> Sets can only contain hashable (immutable) items — no lists or dicts inside a set.

> 💡 **ADVANCED TIP – Set comprehensions:**  
> `{x for x in iterable if condition}` creates a set in one line, perfect for deduplication and filtering.

---

## 💡 Real‑world Usage

**Banking – find unique transaction types**
```python
txns = ['deposit', 'withdrawal', 'deposit', 'transfer']
unique_types = set(txns)
print(unique_types)   # {'deposit', 'transfer', 'withdrawal'}
```

**E‑commerce – filter out duplicate promo codes**
```python
codes = ['SAVE10', 'SAVE20', 'SAVE10']
active = set(codes)
print(len(active), 'unique codes')
```

**Logistics – check if shipment ID is valid**
```python
valid_ids = {'TRK-100', 'TRK-200', 'TRK-300'}
if 'TRK-100' in valid_ids:
    print('Shipment found')
```

**HR – find all unique departments**
```python
departments = ['Sales', 'Engineering', 'Sales', 'HR']
unique_depts = set(departments)
print(unique_depts)   # {'Sales', 'HR', 'Engineering'}
```

**Reporting – tag cloud from keywords**
```python
keywords = ['python', 'data', 'python', 'ai']
print(set(keywords))
```

---

## 🔍 Practice Preview

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | Create a set with elements `1,2,3` and print it. | `{1, 2, 3}` |
| Medium | Start with `s={1,2,3}`. Add `4` to the set, then print the set. | `{1, 2, 3, 4}` |
| Hard   | Given list `[1,2,2,3,3,3]`, convert to a set and back to a sorted list. Print the list. | `[1, 2, 3]` |

Run the coach:
```bash
python ii_Practice_Sheets/L-42_Sets.py
```

---

## 📌 Key Takeaway
- Sets store unique elements; duplicates are automatically discarded.
- Use `.add()`, `.remove()`, `.discard()`, and `.update()` to modify.
- Membership test with `in` is O(1) on average — extremely fast.
- Convert to set for deduplication, back to list for ordering.
- Companion will use sets for unique keyword indexing and permission checks.