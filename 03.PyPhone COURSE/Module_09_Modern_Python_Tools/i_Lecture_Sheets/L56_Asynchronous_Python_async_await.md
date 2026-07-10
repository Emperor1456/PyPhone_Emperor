# 📘 PyPhone Emperor v3.0 · Module 9
# 📖 L‑56 – Asynchronous Python – `async`/`await` Basics

---

## 🎯 OBJECTIVE — What You Will Master

> Write non‑blocking code for I/O‑bound tasks.

- ⚡ **`async`/`await`** – define and call asynchronous functions
- 🏃 **`asyncio`** – the event loop that runs coroutines
- 🧪 **Why async** – handle thousands of connections without threads
- 🛠️ **`gather()`** – run multiple coroutines concurrently

---

## 🧱 DEFINING A COROUTINE

```python
import asyncio

async def greet():
    print("Hello")
    await asyncio.sleep(1)
    print("Emperor")

asyncio.run(greet())
```

`await` pauses the coroutine until the operation completes.

---

## 🧱 RUNNING MULTIPLE COROUTINES

```python
async def fetch_data(url):
    print(f"Fetching {url}...")
    await asyncio.sleep(2)  # simulate network delay
    return f"Data from {url}"

async def main():
    results = await asyncio.gather(
        fetch_data("url1"),
        fetch_data("url2"),
        fetch_data("url3")
    )
    print(results)

asyncio.run(main())
```

All three fetches run concurrently, taking ~2 seconds total instead of 6.

---

## 💡 Real‑world Usage

**Banking – process multiple transactions**
```python
async def process_tx(tx):
    await asyncio.sleep(0.1)  # simulate DB call
    return f"Processed {tx}"

async def main():
    tasks = [process_tx(i) for i in range(10)]
    results = await asyncio.gather(*tasks)
```

**E‑commerce – load product images**
```python
async def load_image(url):
    # fetch image asynchronously
    await asyncio.sleep(0.5)
    return f"Loaded {url}"
```

**Logistics – query multiple carriers**
```python
async def query_carrier(carrier, tracking):
    await asyncio.sleep(1)
    return f"{carrier}: delivered"
```

---

## 🔍 Practice Preview

| Level | Task |
|-------|------|
| Easy | Define an `async` function that prints a message. |
| Medium | Use `await asyncio.sleep()` to simulate a delay. |
| Hard | Run two coroutines concurrently with `asyncio.gather()`. |

Run the coach:
```bash
python ii_Practice_Sheets/L56_Asynchronous_Python_async_await.py
```

---

## 📌 Key Takeaway
- `async` defines a coroutine; `await` pauses it for an async operation.
- `asyncio.run()` starts the event loop.
- Use `gather()` to run multiple coroutines concurrently.

*For Emperor.*