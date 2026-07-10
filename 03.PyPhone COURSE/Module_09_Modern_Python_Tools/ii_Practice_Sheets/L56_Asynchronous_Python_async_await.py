import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "⚡  Define Async Function\n\n"
        "Write an async function `greet()` that prints 'Hello, Emperor'.\n"
        "Run it using asyncio.run(greet()).\n\n"
        "Expected output: Hello, Emperor"
    ),
    expected_output="Hello, Emperor",
    level=Level.EASY,
    hints=["import asyncio", "async def greet(): print('Hello, Emperor')", "asyncio.run(greet())"]
)

easy2 = Task(
    description=(
        "⏳  Await Sleep\n\n"
        "Write an async function `delayed()` that prints 'Start', awaits asyncio.sleep(0.1), prints 'End'.\n"
        "Run it.\n\n"
        "Expected output:\nStart\nEnd"
    ),
    expected_output="Start\nEnd",
    level=Level.EASY,
    hints=["import asyncio", "async def delayed():", "    print('Start')", "    await asyncio.sleep(0.1)", "    print('End')", "asyncio.run(delayed())"]
)

medium1 = Task(
    description=(
        "🏃  Run Two Coroutines Concurrently\n\n"
        "Define two async functions that each print a message. Run them concurrently with asyncio.gather.\n"
        "Each prints its name, then 'done' after all finish.\n"
        "Print 'All done' after gather.\n\n"
        "Expected output: (messages may interleave, but 'All done' comes last)"
    ),
    expected_output="Task A\nTask B\nAll done",
    level=Level.MEDIUM,
    hints=["import asyncio", "async def task_a(): print('Task A')", "async def task_b(): print('Task B')", "async def main():", "    await asyncio.gather(task_a(), task_b())", "    print('All done')", "asyncio.run(main())"]
)

medium2 = Task(
    description=(
        "🔁  Async Return Value\n\n"
        "Define an async function `fetch()` that returns 'data'. Collect the result using asyncio.run\n"
        "and print it.\n\n"
        "Expected output: data"
    ),
    expected_output="data",
    level=Level.MEDIUM,
    hints=["import asyncio", "async def fetch(): return 'data'", "result = asyncio.run(fetch())", "print(result)"]
)

hard1 = Task(
    description=(
        "⏱️  Concurrent Delays\n\n"
        "Define an async function that takes a name and delay. Create two tasks with delays 0.2 and 0.1,\n"
        "run concurrently, and print their names in order of completion.\n"
        "The one with 0.1s should print first, then 0.2s, then 'Done'.\n\n"
        "Expected output:\nFast\nSlow\nDone"
    ),
    expected_output="Fast\nSlow\nDone",
    level=Level.HARD,
    hints=["import asyncio", "async def task(name, delay):", "    await asyncio.sleep(delay)", "    print(name)", "async def main():", "    await asyncio.gather(task('Slow', 0.2), task('Fast', 0.1))", "    print('Done')", "asyncio.run(main())"]
)

hard2 = Task(
    description=(
        "📊  Async with Return Values\n\n"
        "Define two async functions `square(x)` returning x*x, and `cube(x)` returning x*x*x.\n"
        "Run both concurrently with gather for x=3, collect results, and print their sum.\n\n"
        "Expected output: 36"
    ),
    expected_output="36",
    level=Level.HARD,
    hints=["import asyncio", "async def square(x): return x*x", "async def cube(x): return x*x*x", "async def main():", "    results = await asyncio.gather(square(3), cube(3))", "    print(sum(results))", "asyncio.run(main())"]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L56.json")
