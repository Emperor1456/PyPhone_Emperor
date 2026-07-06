# 📘 PyPhone Emperor · Module 8  
# 📖 L‑66 – Introduction to Testing (`assert`, `unittest`)

---

## 🎯 OBJECTIVE
Learn to verify that your code works correctly using
**automated tests**. You’ll start with simple `assert`
statements for quick sanity checks, then graduate to
Python’s built‑in `unittest` framework — the industry
standard for writing repeatable, organised test suites.

---

## 🧱 BRICK 1 – The `assert` Statement

`assert` is a simple debugging tool. It checks whether
a condition is `True`. If it is, nothing happens.
If it’s `False`, Python raises an `AssertionError`
with an optional message.

```python
def double(n):
    return n * 2

assert double(3) == 6                # passes silently
assert double(0) == 0                # passes
assert double(-2) == -4, "Failed on negative input"
```

Use `assert` for:
- Quick tests during development.
- Documenting assumptions in your code.
- Catching bugs early.

Do **not** use `assert` for:
- Validating user input (assertions can be disabled).
- Error handling in production — they crash the program.

> 💡 **INSIGHT:** You can disable all asserts globally by
> running Python with the `-O` (optimise) flag. That’s why
> assertions are for development, not production logic.

---

## 🧱 BRICK 2 – Introduction to `unittest`

The `unittest` module organises tests into classes.
Each test is a method whose name starts with `test_`.
The framework calls each test independently and reports
which passed and which failed.

### Basic test structure:
```python
import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    def test_mixed(self):
        self.assertEqual(add(-1, 1), 0)

if __name__ == "__main__":
    unittest.main()
```

Running this file prints a dot for each passing test:
```
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

### Common assertion methods:
| Method                      | Checks                        |
|-----------------------------|-------------------------------|
| `assertEqual(a, b)`         | `a == b`                      |
| `assertNotEqual(a, b)`      | `a != b`                      |
| `assertTrue(x)`             | `bool(x) is True`             |
| `assertFalse(x)`            | `bool(x) is False`            |
| `assertIn(a, b)`            | `a in b`                      |
| `assertRaises(Error, func)` | func raises the given Error   |

### Testing with `setUp()` and `tearDown()`:
```python
class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("Emperor", 100)

    def tearDown(self):
        self.account = None

    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)
```

`setUp` runs **before each test**; `tearDown` runs **after**.
They keep tests isolated from each other.

> ⚠️ **WARNING:** Tests must be independent. One test should
> never rely on another test having run first.

---

## 📌 Key Takeaway
- `assert` is a quick, developer‑oriented check.
- `unittest` organises tests into classes and reports results.
- Test methods start with `test_` and use `self.assertEqual(...)`.
- `setUp`/`tearDown` manage shared test resources.
- Testing is not optional — it’s part of professional coding.