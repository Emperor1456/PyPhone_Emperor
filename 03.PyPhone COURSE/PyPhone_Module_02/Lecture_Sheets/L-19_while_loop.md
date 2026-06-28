# 📘 PyPhone Emperor · Module 2
# 📖 L‑19 – `while` Loop

---

## 🎯 OBJECTIVE
Learn to repeat a block of code **while** a condition is `True`.
The `while` loop keeps executing until the condition becomes `False`.
This is the fundamental way to create repetition when you don’t
know in advance how many times the block should run.

---

## 🧱 BRICK 1 – Basic `while` Loop

```python
while condition:
    # block runs repeatedly as long as condition is True
```

**Example:**
```python
count = 1
while count <= 5:
    print(count)
    count += 1
```
Output:
```
1
2
3
4
5
```

The loop body must **eventually make the condition False**;
otherwise the loop runs forever (infinite loop).

> 💡 **INSIGHT:** A `while` loop is like an `if` that repeats.
> The indented block executes over and over as long as the
> condition remains true.

---

## 🧱 BRICK 2 – Real‑world Usage

**① Countdown timer**
```python
seconds = 10
while seconds > 0:
    print(f"T‑minus {seconds}")
    seconds -= 1
print("Liftoff!")
```

**② User input validation**
```python
password = ""
while len(password) < 8:
    password = input("Password (min 8 chars): ")
print("Accepted")
```

**③ Processing until a sentinel value**
```python
total = 0
num = int(input("Enter number (-1 to stop): "))
while num != -1:
    total += num
    num = int(input("Enter number (-1 to stop): "))
print("Sum:", total)
```

> ⚠️ **WARNING:** Always ensure the loop condition can become
> `False`. If `count += 1` is forgotten in the first example,
> the program hangs forever.

---

## 📌 Key Takeaway
- `while` repeats a block based on a condition.
- The block must change something that eventually makes the condition false.
- Use for counting, input validation, and sentinel‑controlled loops.
- Infinite loops freeze your program; stop with Ctrl+C.