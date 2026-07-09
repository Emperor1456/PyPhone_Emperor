# 📘 PyPhone Emperor · Module 8  
# 📖 L‑66 – Introduction to Testing (`assert`, `unittest`) – Verifying Business Logic

---

## 🎯 OBJECTIVE  
Master automated testing to ensure your code works correctly and stays correct.  
Start with `assert` for quick sanity checks, then graduate to Python’s `unittest` framework — the standard for organising, running, and reporting tests.  
Testing is not optional: it’s the safety net of every professional business application.

---

## 🧱 BRICK 1 – Quick Checks with `assert`

The `assert` statement verifies that a condition is `True`. If it is, nothing happens. If not, it raises an `AssertionError` with an optional message.

```python
assert 1 + 1 == 2   # passes silently
```

**① Assert a simple truth (Easy practice)**
```python
assert 1 + 1 == 2
print('pass')
```
Output: `pass`. The assertion succeeds, so the program continues.

**② Assert inside a test function (Medium practice)**
```python
def test_sum():
    assert sum([1, 2, 3]) == 6

test_sum()
print('ok')
```
Output: `ok`. If the assertion failed, the program would crash before printing.

**③ Testing with `unittest` framework (Hard practice)**
```python
import unittest

class TestMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)

unittest.main(argv=[''], exit=False)
print('done')
```
Output: `done` (and a test report). `unittest` runs all methods starting with `test_` and reports results. The `argv=[''], exit=False` prevents the test runner from exiting the script.

> 💡 **INSIGHT:** `assert` is for development and debugging. `unittest` is for building a permanent, runnable test suite.

---

## 🧱 BRICK 2 – The `unittest` Framework in Detail

**④ Basic test class structure**
```python
import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative(self):
        self.assertEqual(add(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()
```
Running this file produces dots for each passing test and a summary.

**⑤ Using `setUp()` and `tearDown()`**
```python
class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount('Emperor', 100)

    def tearDown(self):
        self.account = None

    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)
```
`setUp` runs before every test; `tearDown` runs after. They keep tests isolated.

**⑥ Common assertions**
| Method | Description |
|--------|-------------|
| `assertEqual(a, b)` | `a == b` |
| `assertTrue(x)` | `bool(x) is True` |
| `assertFalse(x)` | `bool(x) is False` |
| `assertIn(a, b)` | `a in b` |
| `assertRaises(Error, callable)` | callable raises Error |

> ⚠️ **WARNING:** Tests must be **independent** and **repeatable**. Never rely on test order or shared mutable state between tests.

> 💡 **ADVANCED TIP:** Use `pytest` for a more concise syntax when you outgrow `unittest`. It runs `unittest` tests natively.

---

## 💡 Real‑world Usage

**Banking – test withdrawal logic**
```python
class TestAccount(unittest.TestCase):
    def test_withdraw_sufficient(self):
        acc = Account(100)
        acc.withdraw(30)
        self.assertEqual(acc.balance, 70)

    def test_withdraw_insufficient(self):
        acc = Account(50)
        with self.assertRaises(ValueError):
            acc.withdraw(100)
```

**E‑commerce – test discount calculation**
```python
def apply_discount(price, pct):
    return price * (1 - pct/100)

assert apply_discount(100, 20) == 80
assert apply_discount(50, 0) == 50
```

**Logistics – test package weight validation**
```python
class TestPackage(unittest.TestCase):
    def test_valid_weight(self):
        p = Package(10)
        self.assertEqual(p.weight, 10)

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            Package(-5)
```

**HR – test employee creation**
```python
def test_employee():
    e = Employee('Emperor', 'Engineering')
    assert e.name == 'Emperor'
    assert e.dept == 'Engineering'

test_employee()
print('All HR tests passed')
```

---

## 🔍 Practice Preview

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | Use `assert` to verify `1+1==2`. If it passes, print `'pass'`. | `pass` |
| Medium | Define a function `test_sum` that uses `assert` to check that `sum([1,2,3])` equals `6`. Call the function and print `'ok'` after. | `ok` |
| Hard   | Create a `unittest.TestCase` subclass with a method that checks `self.assertEqual(2+2,4)`. Run it using `unittest.main(argv=[''],exit=False)` and print `'done'` after. | `done` |

Run the coach:
```bash
python ii_Practice_Sheets/L-66_Testing.py
```

---

## 📌 Key Takeaway
- `assert condition` is a quick, developer‑focused check.
- `unittest.TestCase` organises tests into classes; methods start with `test_`.
- Use `setUp`/`tearDown` for shared test setup and cleanup.
- Tests give you confidence that changes don’t break existing functionality.
- Automated testing is a non‑negotiable part of professional software development.