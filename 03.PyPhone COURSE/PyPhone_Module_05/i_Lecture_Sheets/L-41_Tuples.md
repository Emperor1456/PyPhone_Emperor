# 📘 PyPhone Emperor · Module 5  
# 📖 L‑41 – Tuples – Immutable Sequences (Fixed Business Data)

---

## 🎯 OBJECTIVE  
Master **tuples** — ordered, immutable sequences. Use them for fixed data that should not change: coordinates, configuration constants, database records, and multiple return values from functions.

---

## 🧱 BRICK 1 – Creating and Indexing Tuples

A tuple is defined with parentheses `()` and comma‑separated elements.  
For a single element, include a trailing comma.

**① Basic tuple creation (Easy practice)**
```python
t = (1, 2, 3)
print(t)   # (1, 2, 3)
```

**② Access elements by index (Medium practice)**
```python
t = (1, 2, 3)
print(t[0])    # 1
print(t[-1])   # 3
```
Indexing works exactly like lists.

**③ Concatenating tuples (Hard practice)**
```python
t1 = (1, 2, 3)
t2 = (4, 5)
combined = t1 + t2
print(combined)   # (1, 2, 3, 4, 5)
```
Concatenation creates a new tuple; original tuples remain unchanged.

**④ Unpacking tuples**
```python
point = (5, 8)
x, y = point
print(x, y)   # 5 8
```

> 💡 **INSIGHT:** Tuples are immutable — you cannot change, add, or remove elements after creation. This makes them perfect for data that must stay constant, like settings or fixed lookup values.

---

## 🧱 BRICK 2 – Why Tuples Matter in Business Systems

**⑤ Returning multiple values from a function**
```python
def min_max(data):
    return min(data), max(data)   # returns a tuple

low, high = min_max([4, 1, 9, 3])
print(low, high)   # 1 9
```

**⑥ Dictionary keys**
Tuples can serve as dictionary keys because they are hashable (immutable). Lists cannot.
```python
locations = {
    (40.7128, -74.0060): 'New York',
    (51.5074, -0.1278): 'London'
}
print(locations[(40.7128, -74.0060)])   # 'New York'
```

**⑦ Fixed product dimensions**
```python
laptop_size = (1920, 1080)
print(f"Resolution: {laptop_size[0]}x{laptop_size[1]}")
```

> ⚠️ **WARNING:** A single‑element tuple requires a trailing comma: `(42,)` vs `(42)` which is just the integer 42.

> 💡 **ADVANCED TIP – Named tuples (`collections.namedtuple`):**  
> For more readable code, `namedtuple` gives field names to tuple elements, ideal for lightweight record types.

---

## 💡 Real‑world Usage

**Banking – fixed interest rates**
```python
interest_rates = (0.05, 0.10, 0.15)  # cannot be altered by accident
```

**E‑commerce – product specifications**
```python
product = ('Laptop', 'Electronics', 999.99)
print(product[1])   # 'Electronics'
```

**Logistics – GPS coordinates**
```python
warehouse = (23.8103, 90.4125)  # Dhaka coordinates
```

**HR – employee status codes**
```python
statuses = ('active', 'inactive', 'terminated')
```

**Reporting – fixed column headers**
```python
headers = ('ID', 'Name', 'Sales')
print(', '.join(headers))
```

---

## 🔍 Practice Preview

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | Create a tuple `(1,2,3)` and print it. | `(1, 2, 3)` |
| Medium | `t=(1,2,3)`. Print the first and last element on separate lines. | `1`<br>`3` |
| Hard   | `t1=(1,2,3)`, `t2=(4,5)`. Concatenate and print the result. | `(1, 2, 3, 4, 5)` |

Run the coach:
```bash
python ii_Practice_Sheets/L-41_Tuples.py
```

---

## 📌 Key Takeaway
- Tuples are ordered, immutable sequences — use for fixed data.
- Access via indexing and slicing; combine with `+`.
- Unpack directly into variables.
- Tuple immutability guarantees data integrity, making them safe keys and constants.
- Companion will use tuples for immutable memory fragments and embedded lookup tables.