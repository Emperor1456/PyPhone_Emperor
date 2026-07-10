# 📘 Module 09 – Modern Python & Tools · Revision Note

---

## L49 – Modules & `import`
- `import module` brings in an external file.
- `from module import name` imports specific items.
- Standard library: `math`, `random`, `datetime`, `os`, `sys`.

```python
import math
print(math.sqrt(25))   # 5.0
```

---

## L50 – Virtual Environments & `pip freeze`
- `python -m venv myenv` creates an isolated environment.
- Activate: `source myenv/bin/activate` (Linux/Termux).
- `pip freeze > requirements.txt` locks dependencies.
- `pip install -r requirements.txt` restores them.

---

## L51 – `requests` – HTTP & APIs
- `requests.get(url)` fetches data.
- `response.status_code` – check success (200).
- `response.json()` – parse JSON response.
- `requests.post(url, json=data)` sends data.

```python
import requests
r = requests.get("https://httpbin.org/json")
print(r.json()["slideshow"]["title"])
```

---

## L52 – Environment Variables & `.env` Files
- `os.getenv("KEY", "default")` reads environment variables.
- `.env` files store secrets locally; never commit to git.
- `python-dotenv` loads `.env` automatically.

```python
from dotenv import load_dotenv
import os
load_dotenv()
print(os.getenv("API_KEY", "not set"))
```

---

## L53 – `datetime` & `time` Deep Dive
- `datetime.now()` – current date/time.
- `strftime("%Y-%m-%d")` – format to string.
- `strptime(date_str, format)` – parse string to datetime.
- `timedelta(days=30)` – date arithmetic.

```python
from datetime import datetime, timedelta
future = datetime.now() + timedelta(days=30)
print(future.strftime("%Y-%m-%d"))
```

---

## L54 – Generator Expressions & `yield`
- Generator expression: `(x*2 for x in range(10))` – lazy.
- `yield` makes a function a generator, pausing execution.
- Memory‑efficient for large or infinite sequences.

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```

---

## L55 – Decorators – Wrapping Functions
- A decorator is a function that takes a function and returns a new one.
- `@decorator` syntax applies the wrapper.
- Use `functools.wraps` to preserve metadata.

```python
def bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper
```

---

## L56 – Asynchronous Python – `async`/`await`
- `async def` defines a coroutine.
- `await` pauses until the operation completes.
- `asyncio.run()` starts the event loop.
- `asyncio.gather()` runs multiple coroutines concurrently.

```python
import asyncio
async def greet():
    await asyncio.sleep(1)
    print("Hello")
asyncio.run(greet())
```

---

## L57 – Reusable DB Connection Helper
- `sqlite3` is Python's built‑in database.
- Wrap connection logic in a helper function or context manager.
- Parameterised queries (`?`) prevent SQL injection.

```python
import sqlite3
def get_db(path=":memory:"):
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn
```

---

*Quick Test:*  
- How to install all dependencies from `requirements.txt`?  
- List comprehension vs generator expression?  
- Why must you `await` an async function?  
- How do decorators add behaviour without modifying the original function?