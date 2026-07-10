# L35 Solution – Debugging with pdb & Logging

## 🟢 Easy 1 – Use assert
```python
assert 1+1 == 2
print('pass')
```

## 🟢 Easy 2 – Basic Logging
```python
import logging
print('logging ready')
```

## 🟡 Medium 1 – Test with assert function
```python
def test_sum():
    assert sum([1,2,3]) == 6
test_sum()
print('ok')
```

## 🟡 Medium 2 – Using pdb.set_trace (simulation)
```python
print('breakpoint set')
```

## 🔴 Hard 1 – Unittest Simulation
```python
import unittest
class TestMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2+2, 4)
unittest.main(argv=[''], exit=False)
print('done')
```

## 🔴 Hard 2 – Logging Levels
```python
import logging
logging.basicConfig(level=logging.WARNING)
logging.warning('Low disk space')
```