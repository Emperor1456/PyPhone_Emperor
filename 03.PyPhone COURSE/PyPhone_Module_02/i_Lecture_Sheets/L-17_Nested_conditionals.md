# 📘 PyPhone Emperor · Module 2
# 📖 L‑17 – Nested Conditionals

---

## 🎯 OBJECTIVE
Learn to place `if` statements **inside** other `if` blocks.
Nesting lets you test secondary conditions only when
a primary condition is already met.
This refines decisions in multi‑step logic.

---

## 🧱 BRICK 1 – What Is a Nested Conditional?

A nested conditional is simply an `if` (or `if‑else`, `elif`)
written inside the indented block of another `if`.

```python
if outer_condition:
    # this code runs only if outer_condition is True
    if inner_condition:
        # this runs only if BOTH conditions are True
```

**Example:**
```python
is_logged_in = True
is_admin = False

if is_logged_in:
    print("Welcome back")
    if is_admin:
        print("Admin panel available")
```
Here, "Admin panel available" never prints because the inner
condition fails, even though the outer one passes.

> 💡 **INSIGHT:** The inner `if` is only reached when the outer `if`'s condition is `True`.

---

## 🧱 BRICK 2 – Multi‑Level Nesting and Readability

You can nest deeper, but beyond 2‑3 levels the code becomes
hard to follow. Prefer logical operators (`and`, `or`) or
separate functions to keep things flat when possible.

**Nested (harder to read):**
```python
if age >= 18:
    if has_license:
        if not is_banned:
            print("Can drive")
```

**Flattened with `and` (cleaner):**
```python
if age >= 18 and has_license and not is_banned:
    print("Can drive")
```

> ⚠️ **WARNING:** Deeply nested code is a source of bugs.
> Always ask: can I flatten this with `and`/`or` or a helper function?

---

## 📌 Key Takeaway
- Nesting = `if` inside `if`.
- Inner block runs only when outer condition is already `True`.
- Keep nesting shallow; use `and`/`or` to flatten when possible.
- Indent consistently — each level adds 4 spaces.