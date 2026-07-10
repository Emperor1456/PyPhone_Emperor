# L49 Solution – Modules & import (math, random, etc.)

## 🟢 Easy 1 – Import Math and Print Pi
```python
import math
print(math.pi)
```

## 🟢 Easy 2 – Random Integer
```python
import random
random.seed(42)
print(random.randint(1, 10))
```

## 🟡 Medium 1 – Current Date and Time
```python
from datetime import datetime
print(datetime.now().year)
```

## 🟡 Medium 2 – List Files in Current Directory
```python
import os
print(sorted(os.listdir('.')))
```

## 🔴 Hard 1 – Custom Module Import
```python
import mycalc
print(mycalc.add(3, 4))
```

## 🔴 Hard 2 – Import Specific Function
```python
from math import sqrt, ceil
print(sqrt(16))
print(ceil(3.2))
```