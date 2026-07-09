# 📘 PyPhone Emperor · Module 4  
# 📖 L‑33 – `*args` & `**kwargs` (Variable Arguments)

---

## 🎯 OBJECTIVE  
Master `*args` and `**kwargs` to write functions that accept any number of inputs.  
`*args` collects extra positional arguments into a tuple; `**kwargs` collects extra keyword arguments into a dictionary.  
These are essential for flexible APIs, logging wrappers, and building functions that adapt to changing business needs.

---

## 🧱 BRICK 1 – `*args` (Variable Positional Arguments)

Prefix a parameter with a single `*` to collect any number of positional arguments into a tuple.

```python
def func(*args):
    # args is a tuple of all extra arguments
```

**① Summing any number of values**
```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))   # 10
```
The built‑in `sum()` works directly on the tuple.  
This is the Easy practice task — a flexible sales aggregator that handles any number of daily totals.

**② Combining fixed and variable parameters**
```python
def report(title, *values):
    total = sum(values)
    return f"{title}: {total}"

print(report('Q1 Sales', 200, 150, 320))   # 'Q1 Sales: 670'
```

**③ Iterating through `*args`**
```python
def list_items(*args):
    for i, item in enumerate(args, 1):
        print(f"{i}. {item}")

list_items('laptop', 'mouse', 'keyboard')
```

> 💡 **INSIGHT:** `*args` is a tuple — you can index it, slice it, iterate over it, and pass it to other functions.

---

## 🧱 BRICK 2 – `**kwargs` (Variable Keyword Arguments)

Prefix a parameter with `**` to collect keyword arguments into a dictionary.

```python
def func(**kwargs):
    # kwargs is a dict of all keyword arguments
```

**④ Displaying user info**
```python
def print_info(**kwargs):
    parts = []
    for k, v in kwargs.items():
        parts.append(f'{k}: {v}')
    return ', '.join(parts)

result = print_info(name='Emperor', age=18)
print(result)   # 'name: Emperor, age: 18'
```
This is the Medium practice task — a generic info formatter that adapts to any key‑value pairs.

**⑤ Combining `*args` and `**kwargs`**
```python
def mixed(*args, **kwargs):
    if not kwargs:
        return sum(args)
    else:
        return str(kwargs)

print(mixed(1, 2, 3))              # 6
print(mixed(name='Emperor'))       # {'name': 'Emperor'}
```
This matches the Hard practice task: the function changes behavior based on whether keyword arguments are present.

**⑥ Passing collected arguments to another function**
```python
def log_event(event_type, **details):
    print(f"[{event_type}]", details)

log_event('LOGIN', user='Emperor', ip='192.168.1.1')
```

> ⚠️ **WARNING:** The order must be: regular parameters, `*args`, `**kwargs`.  
> Python enforces this — breaking the order is a syntax error.

> 💡 **ADVANCED TIP:** Use `*args` and `**kwargs` to build **decorators** and **wrappers** —  
> functions that add behavior to other functions without modifying their signatures.  
> This is the foundation of Companion's plugin system.

---

## 💡 Real‑world Usage

**Banking – sum deposits of unknown count**
```python
def total_deposits(*amounts):
    return sum(amounts)

print(total_deposits(100, 200, 50, 300))   # 650
```

**E‑commerce – build product filter string**
```python
def filter_products(**criteria):
    return ' & '.join(f'{k}={v}' for k, v in criteria.items())

print(filter_products(category='electronics', brand='PyPhone'))
```

**Logistics – log shipment details**
```python
def log_shipment(tracking_id, **details):
    print(f"Shipment {tracking_id}: {details}")

log_shipment('TRK123', weight='12kg', status='in transit')
```

---

## 🔍 Practice Preview

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | Define `sum_all(*args)` returning sum of all arguments. Call with 1,2,3,4 and print. | `10` |
| Medium | Define `print_info(**kwargs)` returning `'key: value'` pairs joined by comma+space. Call with `name='Emperor', age=18` and print. | `name: Emperor, age: 18` |
| Hard   | Define `mixed(*args, **kwargs)` returning sum of args if no kwargs, else `str(kwargs)`. Call with 1,2,3 then with name='Emperor'; print each on separate line. | `6`<br>`{'name': 'Emperor'}` |

Run the coach:
```bash
python ii_Practice_Sheets/L-33_args_kwargs.py
```

---

## 📌 Key Takeaway
- `*args` collects extra positional arguments into a tuple.
- `**kwargs` collects extra keyword arguments into a dict.
- Use them for flexible functions that don't know the number of inputs in advance.
- Order: regular params → `*args` → `**kwargs`.
- Essential for wrappers, loggers, and extensible APIs.