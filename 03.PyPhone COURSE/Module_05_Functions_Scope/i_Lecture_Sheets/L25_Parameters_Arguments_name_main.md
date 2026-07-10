# 📘 PyPhone Emperor v3.0 · Module 5
# 📖 L‑25 – Parameters, Arguments & `__name__ == "__main__"`

---

## 🎯 OBJECTIVE — What You Will Master

> Feed data into functions and control script execution.

- 📥 **Parameters** – placeholders in the definition
- 📤 **Arguments** – actual values passed during call
- 🔐 **`__name__ == "__main__"`** – run code only when script is executed directly
- 🧪 **Default values** – optional parameters with fallbacks

---

## 🧱 POSITIONAL & KEYWORD ARGUMENTS

```python
def introduce(name, age):
    print(f"{name} is {age} years old.")

introduce("Emperor", 18)            # positional
introduce(age=18, name="Emperor")   # keyword
```

---

## 🧱 `__name__ == "__main__"` GUARD

Allows a file to be both imported and run as a script.

```python
def main():
    print("This runs only when executed directly.")

if __name__ == "__main__":
    main()
```

---

## 🧱 DEFAULT PARAMETER VALUES

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()          # Hello, Guest!
greet("Emperor") # Hello, Emperor!
```

> ⚠️ **WARNING:** Never use mutable objects as default values (e.g., `def f(lst=[])`). Use `None` and create inside.

---

## 💡 Real‑world Usage

**Banking – transfer with optional fee**
```python
def transfer(amount, fee=0.0):
    return amount - fee
```

**E‑commerce – calculate discount**
```python
def apply_discount(price, percent=0):
    return price * (1 - percent/100)
```

**Logistics – delivery time**
```python
def eta(distance, speed=60):
    return distance / speed
```

---

## 🔍 Practice Preview

| Level | Task | What You’ll Write |
|-------|------|-------------------|
| Easy | Define `add(a,b)` returning `a+b`. Call with 3,5. | `def add(a,b): return a+b` |
| Medium | Define `full_name(first,last)` returning "first last". Call with "Emperor","PyPhone". | `def full_name(f,l): return f+" "+l` |
| Hard | Use `if __name__ == "__main__":` to call a test function that prints "Test". | Standard guard pattern |

Run the coach:
```bash
python ii_Practice_Sheets/L25_Parameters_Arguments_name_main.py
```

---

## 📌 Key Takeaway
- Parameters define the interface; arguments supply data.
- The `__name__` guard makes your scripts import‑safe.
- Default values make parameters optional.

*For Emperor.*