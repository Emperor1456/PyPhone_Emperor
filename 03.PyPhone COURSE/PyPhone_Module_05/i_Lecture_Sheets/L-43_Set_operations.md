# 📘 PyPhone Emperor · Module 5  
# 📖 L‑43 – Set Operations (Comparing Business Data)

---

## 🎯 OBJECTIVE  
Master set operations — union, intersection, difference, symmetric difference — to compare and combine groups of business data.  
These operations are perfect for merging customer lists, finding common items, identifying exclusions, and performing fast audits.

---

## 🧱 BRICK 1 – Union and Intersection

**① Union (Easy practice) — combine sets**
```python
a = {1, 2}
b = {3, 4}
result = a | b
print(result)   # {1, 2, 3, 4}
```
Union collects all unique elements from both sets.  
Think of merging two lists of customers or SKU codes.

**② Intersection (Medium practice) — find common elements**
```python
a = {1, 2, 3}
b = {3, 4, 5}
common = a & b
print(common)   # {3}
```
Intersection returns elements present in both sets.  
Use it to find overlapping permissions, common tags, or shared inventory.

> 💡 **INSIGHT:** `a | b` and `a.union(b)` are equivalent; both accept any iterable.

---

## 🧱 BRICK 2 – Difference and Symmetric Difference

**③ Difference (Hard practice) — elements in A but not in B**
```python
a = {1, 2, 3}
b = {3, 4, 5}
diff = a - b
print(diff)   # {1, 2}
```
Use difference to see which items are exclusive to one set — like customers who bought product A but not B.

**④ Symmetric difference — elements in exactly one set**
```python
sym = a ^ b
print(sym)   # {1, 2, 4, 5}
```
Symmetric difference highlights discrepancies between two lists.

**⑤ Subset and superset checks**
```python
print({1, 2}.issubset({1, 2, 3}))     # True
print({1, 2, 3}.issuperset({1, 2}))   # True
```

**⑥ Methods accept any iterable**
```python
print(a.union([3, 5, 6]))             # {1, 2, 3, 5, 6}
print(a.intersection([2, 3, 7]))      # {2, 3}
```

> ⚠️ **WARNING:** The set on the left side must be a proper set; the right side can be any iterable (list, tuple, etc.).  
> Operations create new sets; originals remain unchanged.

> 💡 **ADVANCED TIP – Using set operations for data analysis:**  
> Combine `&` for commonalities, `-` for exclusions, and `^` for mismatches to audit data integrity between systems.

---

## 💡 Real‑world Usage

**Banking – find accounts with both checking and savings**
```python
checking = {'A1', 'A2', 'A3'}
savings = {'A2', 'A4'}
both = checking & savings   # {'A2'}
```

**E‑commerce – products in stock across two warehouses**
```python
wh1 = {'SKU-1', 'SKU-2', 'SKU-3'}
wh2 = {'SKU-2', 'SKU-4'}
common = wh1 & wh2          # {'SKU-2'}
```

**Logistics – shipments that arrived at hub but not delivered**
```python
arrived = {'T1', 'T2', 'T3'}
delivered = {'T2'}
pending = arrived - delivered   # {'T1', 'T3'}
```

**HR – employees who attended training A or B but not both**
```python
training_a = {'E1', 'E2', 'E3'}
training_b = {'E3', 'E4'}
not_both = training_a ^ training_b   # {'E1', 'E2', 'E4'}
```

**Reporting – combine monthly active users**
```python
jan = {'user1', 'user2', 'user3'}
feb = {'user2', 'user3', 'user4'}
total_active = jan | feb   # {'user1','user2','user3','user4'}
```

---

## 🔍 Practice Preview

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | `a={1,2}, b={3,4}`. Print their union. | `{1, 2, 3, 4}` |
| Medium | `a={1,2,3}, b={3,4,5}`. Print their intersection. | `{3}` |
| Hard   | `a={1,2,3}, b={3,4,5}`. Print the difference `a-b`. | `{1, 2}` |

Run the coach:
```bash
python ii_Practice_Sheets/L-43_Set_Operations.py
```

---

## 📌 Key Takeaway
- `|` / `.union()` merges without duplicates.
- `&` / `.intersection()` finds common elements.
- `-` / `.difference()` returns elements in the first set only.
- `^` / `.symmetric_difference()` returns elements in either but not both.
- Set operations are essential for data comparison, deduplication, and cross‑referencing business records.