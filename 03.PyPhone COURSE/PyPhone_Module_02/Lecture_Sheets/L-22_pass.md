# 📘 PyPhone Emperor · Module 2
# 📖 L‑22 – `pass` Statement

---

## 🎯 OBJECTIVE
Learn to use the **`pass`** statement — a null operation,
a placeholder that does nothing when executed.
It is essential when a statement is required syntactically
but you have no logic to put there yet.

---

## 🧱 BRICK 1 – What `pass` Does (and Doesn’t Do)

`pass` is a single keyword that tells Python “move along,
nothing to execute here.” It does not affect the flow of
the program in any way. It is **not** a comment — the
interpreter sees it, runs it, and immediately finishes it.

```python
if True:
    pass   # syntactically required, but nothing happens
```

Without `pass`, an empty `if` block (or `for`, `while`,
function, class, etc.) would raise an `IndentationError`.

---

## 🧱 BRICK 2 – Real‑world Usage

**① Stubbing out unfinished code**
```python
def future_feature():
    pass   # TODO: implement later
```

**② Minimal class definitions**
```python
class Placeholder:
    pass   # will add attributes and methods later
```

**③ Ignoring an exception silently (advanced)**
```python
try:
    risky_operation()
except SomeError:
    pass   # deliberately do nothing for this error
```

> ⚠️ **WARNING:** Use `pass` sparingly. An empty block is
> often a sign that you haven’t finished designing that
> part of the program.

---

## 📌 Key Takeaway
- `pass` is a do‑nothing placeholder.
- It satisfies Python’s indentation requirements.
- Use it for stubs, empty classes, or deliberately ignoring errors.