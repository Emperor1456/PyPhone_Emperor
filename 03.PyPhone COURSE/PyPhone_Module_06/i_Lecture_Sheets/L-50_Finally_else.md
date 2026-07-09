# 📘 PyPhone Emperor · Module 6  
# 📖 L‑50 – `finally` & `else` in Exception Blocks (Cleanup & Success Logic)

---

## 🎯 OBJECTIVE  
Master the `else` and `finally` clauses of the `try` statement.  
Use `else` for code that runs only on success, and `finally` for cleanup that must always execute — no matter what.

---

## 🧱 BRICK 1 – `else` – Execute Only on Success

The `else` block runs **only if** the `try` block completed without any exception.

```python
try:
    x = 1   # safe operation
except:
    pass
else:
    print('else')   # this runs
```

**① Medium practice – demonstrate `else`**
```python
try:
    y = 2
except:
    pass
else:
    print('else')
```
Output: `else`.

**Why use `else`?** It separates success‑only logic from the `try` block, making it clear which code depends on the absence of errors.

---

## 🧱 BRICK 2 – `finally` – Runs Always

The `finally` block executes **no matter what**: exception or not, and even after a `return` or `break`.

```python
try:
    x = 1
finally:
    print('cleanup')   # always prints
```

**② Easy practice – demonstrate `finally`**
```python
try:
    x = 1
finally:
    print('cleanup')
```
Output: `cleanup`.

**③ Hard practice – combine all four clauses**
```python
try:
    1 / 0
except:
    flow = 'except'
else:
    flow = 'else'
finally:
    flow = 'finally'
print(flow)   # 'finally' — because finally overrides previous assignment
```
Output: `finally`. Notice that the `finally` block runs last and its assignment overwrites earlier ones.

**④ Typical resource cleanup pattern**
```python
f = None
try:
    f = open('data.txt', 'r')
    content = f.read()
except FileNotFoundError:
    print('File missing')
finally:
    if f:
        f.close()
    print('File closed')
```

> ⚠️ **WARNING:** Avoid `return` inside `finally`; it can silently override the function’s intended return value and swallow exceptions.

> 💡 **ADVANCED TIP – `with` replaces manual `finally`:**  
> For file handling and locks, `with` automatically handles cleanup, so you rarely need an explicit `finally` for those.

---

## 💡 Real‑world Usage

**Banking – ensure transaction log is closed**
```python
f = open('tx.log', 'a')
try:
    f.write('withdrawal 50\n')
except:
    print('Write failed')
finally:
    f.close()
```

**E‑commerce – report generation with cleanup**
```python
try:
    generate_report()
except Exception as e:
    print(f'Report failed: {e}')
else:
    print('Report generated successfully')
finally:
    cleanup_temp_files()
```

**Logistics – always reset the scale**
```python
try:
    weight = read_scale()
except ScaleError:
    weight = 0
else:
    print(f'Weight: {weight}kg')
finally:
    reset_scale()
```

**HR – batch processing with final summary**
```python
processed = 0
try:
    for emp in employees:
        update_record(emp)
        processed += 1
except Exception as e:
    print(f'Error at {processed}')
else:
    print(f'All {processed} records updated')
finally:
    print('Batch job ended')
```

---

## 🔍 Practice Preview

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | Use `try/finally` to print `'cleanup'` no matter what (safe operation). | `cleanup` |
| Medium | Use `try/except/else`: set a variable and print `'else'` when no exception occurs. | `else` |
| Hard   | Combine `try/except/else/finally` with a deliberate error (`1/0`). Ensure `'finally'` prints last. Print the final value. | `finally` |

Run the coach:
```bash
python ii_Practice_Sheets/L-50_finally_else.py
```

---

## 📌 Key Takeaway
- `else` runs only if no exception occurred; it separates success‑only logic.
- `finally` runs always — perfect for resource cleanup (closing files, releasing locks).
- Order: `try` → `except` → `else` → `finally`.
- Use `finally` for cleanup, not for changing return values.
- These clauses make your programs robust and professional.