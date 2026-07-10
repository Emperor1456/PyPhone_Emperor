# 📘 PyPhone Emperor v3.0 · Module 5
# 📖 L‑28 – `*args`, `**kwargs` & Unpacking

---

## 🎯 OBJECTIVE — What You Will Master

> Accept any number of arguments – the key to flexible, reusable functions.

- ⭐ **`*args`** – collect positional arguments into a tuple
- ⭐ **`**kwargs`** – collect keyword arguments into a dictionary
- 🧩 **Unpacking** – spread a list/dict into arguments
- 🧪 **Real‑world** – logging, wrappers, generic processors

---

## 🧱 `*args` – VARIABLE POSITIONAL ARGUMENTS

```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))   # 6
```

`args` is a tuple inside the function.

---

## 🧱 `**kwargs` – VARIABLE KEYWORD ARGUMENTS

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Emperor", age=18)
```

`kwargs` is a dictionary.

---

## 🧱 UNPACKING WITH `*` AND `**`

```python
def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
print(add(*nums))   # unpack list

config = {"a": 1, "b": 2, "c": 3}
print(add(**config))   # unpack dict
```

---

## 💡 Real‑world Usage

**Banking – sum unknown deposits**
```python
def total_deposits(*amounts):
    return sum(amounts)
```

**E‑commerce – product filter**
```python
def filter_products(**criteria):
    return [k for k, v in criteria.items() if v]
```

**Logistics – log shipment**
```python
def log_event(event_type, **details):
    print(f"[{event_type}] {details}")
```

---

## 🔍 Practice Preview

| Level | Task | What You’ll Write |
|-------|------|-------------------|
| Easy | Define `sum_all(*args)` returning sum. Call with 1,2,3,4. | `def sum_all(*args): return sum(args)` |
| Medium | Define `print_info(**kwargs)` returning "key: value" pairs. Call with name='Emperor', age=18. | `def print_info(**kwargs): ...` |
| Hard | Define `mixed(*args, **kwargs)` returning sum of args if no kwargs, else str(kwargs). Call with 1,2,3 then name='Emperor'. | `def mixed(*args, **kwargs): ...` |

Run the coach:
```bash
python ii_Practice_Sheets/L28_args_kwargs_Unpacking.py
```

---

## 📌 Key Takeaway
- `*args` for variable positional; `**kwargs` for variable keyword.
- Unpack lists/tuples with `*`, dicts with `**`.
- Essential for wrappers and flexible APIs.

*For Emperor.*