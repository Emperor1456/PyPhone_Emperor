# 📘 PyPhone Emperor · Module 2
# 📖 L‑21 – `break` and `continue`

---

## 🎯 OBJECTIVE
Learn to control the flow inside loops using **`break`** and **`continue`**.
`break` exits the loop immediately, no matter the condition.
`continue` skips the rest of the current iteration and jumps to the next one.
Together they give you precision control over repetition.

---

## 🧱 BRICK 1 – `break`: Stop the Loop Now

`break` terminates the loop entirely. The program continues
with the first statement after the loop body.

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)
```
Output:
```
1
2
3
4
```
When `i` equals 5, the loop stops dead – 5 is never printed.

**Real‑world example – search with early exit:**
```python
names = ["Ana", "Bob", "Emperor", "Zoe"]
for name in names:
    if name == "Emperor":
        print("Found!")
        break
```
The loop stops as soon as "Emperor" is found, saving time.

> 💡 **INSIGHT:** Use `break` to escape a loop once your goal
> is achieved – no need to process the remaining items.

---

## 🧱 BRICK 2 – `continue`: Skip This Iteration

`continue` jumps back to the top of the loop for the **next**
iteration, ignoring whatever code follows it in the current pass.

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```
Output:
```
1
2
4
5
```
When `i` is 3, `continue` skips the `print(i)` line and moves to 4.

**Real‑world example – filtering:**
```python
for score in [55, 72, 40, 91, 33]:
    if score < 50:
        continue
    print(f"Passing score: {score}")
```
Only scores ≥ 50 are printed.

> ⚠️ **WARNING:** `continue` only skips the **current** iteration,
> not the whole loop. The loop still runs to completion unless
> you also use `break`.

---

## 📌 Key Takeaway
- `break` exits the loop completely.
- `continue` skips the rest of the current iteration.
- Both work with `while` and `for` loops.
- Use them for early exit and filtering inside loops.