# 📘 PyPhone Emperor v3.0 · Module 4
# 📖 L‑22 – Sets – Uniqueness, Membership & Operations

---

## 🎯 OBJECTIVE — What You Will Master

> Sets: the fastest way to handle unique items and membership tests.

- 🧹 **Uniqueness** – automatic deduplication
- ⚡ **Membership** – O(1) average `in` check
- 🧪 **Set creation** – `{}` or `set()`
- ✏️ **Modify** – `add()`, `remove()`, `discard()`

---

## 🧱 CREATING SETS

```python
fruits = {"apple", "banana", "cherry"}
unique_nums = set([1, 2, 2, 3, 3])  # {1,2,3}
empty = set()                         # {} is empty dict!
```

Duplicates are silently dropped.

---

## 🧱 MEMBERSHIP TESTING

```python
print("apple" in fruits)   # True
print("grape" in fruits)   # False
```

Much faster than a list for large collections.

---

## 🧱 ADDING & REMOVING

```python
fruits.add("date")
fruits.update(["elderberry", "fig"])
fruits.remove("banana")      # KeyError if missing
fruits.discard("mango")      # no error if missing
```

> ⚠️ **WARNING:** Sets are unordered; indexing/slicing is not supported.

---

## 💡 Real‑world Usage

**Banking – unique transaction types**
```python
txns = ["deposit","withdrawal","deposit"]
unique = set(txns)   # {'deposit','withdrawal'}
```

**E‑commerce – valid promo codes**
```python
valid = {"SAVE10","SAVE20"}
if user_code in valid:
    print("Valid")
```

**Logistics – visited hubs**
```python
hubs = set()
hubs.add("A"); hubs.add("B")
print("A" in hubs)   # True
```

---

## 🔍 Practice Preview

| Level | Task | What You’ll Write |
|-------|------|-------------------|
| Easy | Create a set from a list with duplicates and print it. | `s=set([1,2,2,3]); print(s)` |
| Medium | Check if a specific value exists in the set and print the boolean. | `print(3 in s)` |
| Hard | Add an element, then remove another element safely with `discard`. | `s.add(4); s.discard(2); print(s)` |

Run the coach:
```bash
python ii_Practice_Sheets/L22_Sets_Uniqueness_Membership_Operations.py
```

---

## 📌 Key Takeaway
- Sets store unique elements; perfect for deduplication.
- Membership test `in` is extremely fast.
- Use `add()`, `remove()`, `discard()` to modify.

*For Emperor.*