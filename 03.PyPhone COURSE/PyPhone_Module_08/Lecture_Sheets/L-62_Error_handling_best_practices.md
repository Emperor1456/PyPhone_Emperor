# 📘 PyPhone Emperor · Module 8
# 📖 L‑62 – Error Handling Best Practices

---

## 🎯 OBJECTIVE
Learn to write robust, maintainable error‑handling code.
Move beyond basic `try`/`except` and adopt patterns
that keep your programs stable, informative, and
easy to debug — even in production environments.

---

## 🧱 BRICK 1 – Catch Specific Exceptions

Always catch the **most specific** exception that you
expect. Catching generic `Exception` too broadly hides
unexpected errors and makes debugging difficult.

```python
# BAD – catches everything, even bugs
try:
    value = int(user_input)
except Exception:
    value = 0

# GOOD – catches only expected errors
try:
    value = int(user_input)
except ValueError:
    value = 0
```

If you do catch a broad exception, log the original error
to help diagnose later:

```python
import logging
try:
    risky_operation()
except Exception as e:
    logging.exception("Unexpected error occurred")
```

> 💡 **INSIGHT:** Catching `BaseException` or using bare
> `except:` is almost never correct — it catches
> `KeyboardInterrupt` and `SystemExit`, preventing the
> program from stopping.

---

## 🧱 BRICK 2 – Keep `try` Blocks Small

Wrap only the exact line(s) that might raise the error.
This prevents catching exceptions from unrelated code.

```python
# BAD – entire block is wrapped
try:
    user = fetch_user(id)
    process(user)
    save(user)
except DatabaseError:
    print("DB error")

# GOOD – only the risky call is wrapped
try:
    user = fetch_user(id)
except DatabaseError:
    print("Could not fetch user")
else:
    process(user)
    save(user)
```

### Use `else` for success‑only logic and `finally` for cleanup.

**Avoid empty `except` blocks:**  
An `except` that does nothing silently swallows the error.
At minimum, log it.

```python
# BAD – silent failure
try:
    important_task()
except:
    pass

# GOOD – at least log
try:
    important_task()
except Exception as e:
    print(f"Task failed: {e}")
```

> ⚠️ **WARNING:** Never use exception handling for normal
> flow control (e.g., using `try` instead of an `if` check).
> Exceptions are for *exceptional* cases — they are slower
> than regular conditionals.

---

## 📌 Key Takeaway
- Catch specific exceptions; avoid bare `except`.
- Keep `try` blocks small around the exact risky code.
- Use `else` for code that runs only on success.
- Always log errors — silent catches hide critical bugs.