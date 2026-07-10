# L56 Solution – Asynchronous Python – async/await

## 🟢 Easy 1 – Define Async Function
```python
import asyncio

async def greet():
    print('Hello, Emperor')

asyncio.run(greet())
```

## 🟢 Easy 2 – Await Sleep
```python
import asyncio

async def delayed():
    print('Start')
    await asyncio.sleep(0.1)
    print('End')

asyncio.run(delayed())
```

## 🟡 Medium 1 – Run Two Coroutines Concurrently
```python
import asyncio

async def task_a():
    print('Task A')

async def task_b():
    print('Task B')

async def main():
    await asyncio.gather(task_a(), task_b())
    print('All done')

asyncio.run(main())
```

## 🟡 Medium 2 – Async Return Value
```python
import asyncio

async def fetch():
    return 'data'

result = asyncio.run(fetch())
print(result)
```

## 🔴 Hard 1 – Concurrent Delays
```python
import asyncio

async def task(name, delay):
    await asyncio.sleep(delay)
    print(name)

async def main():
    await asyncio.gather(
        task('Slow', 0.2),
        task('Fast', 0.1)
    )
    print('Done')

asyncio.run(main())
```

## 🔴 Hard 2 – Async with Return Values
```python
import asyncio

async def square(x):
    return x * x

async def cube(x):
    return x * x * x

async def main():
    results = await asyncio.gather(square(3), cube(3))
    print(sum(results))

asyncio.run(main())
```