# 📘 PyPhone Emperor · Module 5
# 📖 L‑38 – Accessing & Modifying Dictionaries

---

## 🎯 OBJECTIVE
Go deeper into reading and updating dictionaries.
Learn to add, modify, and remove key‑value pairs,
and understand how to work safely with keys that
may or may not exist.

---

## 🧱 BRICK 1 – Adding and Updating

You can add a new key‑value pair or update an
existing one with square brackets.

```python
person = {"name": "Emperor", "age": 18}

person["city"] = "Dhaka"       # add
person["age"] = 19             # update
print(person)
# {'name': 'Emperor', 'age': 19, 'city': 'Dhaka'}
```

**Update multiple keys at once with `.update()`:**
```python
person.update({"age": 20, "country": "BD"})
print(person)
# {'name': 'Emperor', 'age': 20, 'city': 'Dhaka', 'country': 'BD'}
```

> 💡 **INSIGHT:** `.update()` merges another dict into
> the original. Existing keys are overwritten.

---

## 🧱 BRICK 2 – Removing and Checking Keys

### Removing
- `del dict[key]` — removes a key (raises KeyError if missing)
- `.pop(key, default)` — removes and returns the value
- `.popitem()` — removes and returns the last inserted pair
- `.clear()` — empties the dictionary

```python
age = person.pop("age")       # returns 20
last = person.popitem()       # ('country', 'BD')
person.clear()                # {}
```

### Checking existence
```python
if "name" in person:
    print("Name exists")
```

### Modifying values safely
```python
# Increment a counter, defaulting to 0 if missing
word_count = {}
word = "python"
word_count[word] = word_count.get(word, 0) + 1
```

> ⚠️ **WARNING:** `del` and `.pop()` raise errors if the
> key is missing. Use `in` or `.get()` when unsure.

---

## 📌 Key Takeaway
- `dict[key] = value` adds or updates.
- `.update()` merges another dict.
- `.pop()` removes and returns; `del` just removes.
- Use `in` to check existence, `.get()` for safe access.