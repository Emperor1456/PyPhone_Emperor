# L60 Solution – Testing, Documentation & Packaging

## 🟢 Easy 1 – Write a Docstring
```python
def add_contact(name, phone):
    """Add a new contact to the database."""
    return True

print(add_contact.__doc__)
```

## 🟢 Easy 2 – Write a Simple Test with assert
```python
def double(x):
    return 2 * x

assert double(3) == 6
print('pass')
```

## 🟡 Medium 1 – Unittest Test Case
```python
import unittest

class TestContactBook(unittest.TestCase):
    def test_add(self):
        self.assertTrue(True)

unittest.main(argv=[''], exit=False)
print('done')
```

## 🟡 Medium 2 – Create a README.md Outline
```python
sections = ['# Project Title', '## Features', '## Installation', '## Usage', '## Testing']
print(sections)
```

## 🔴 Hard 1 – Generate requirements.txt
```python
print('pip freeze > requirements.txt')
print('sqlite3 (built-in)')
```

## 🔴 Hard 2 – Test Setup and Teardown
```python
import unittest

class TestDB(unittest.TestCase):
    def setUp(self):
        print('setup')
    def test_example(self):
        print('test')

suite = unittest.TestLoader().loadTestsFromTestCase(TestDB)
unittest.TextTestRunner(verbosity=0).run(suite)
```