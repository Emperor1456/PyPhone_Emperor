# L40 Solution – pathlib

## 🟢 Easy 1 – Create Path Object
```python
from pathlib import Path
p = Path('test.txt')
print(p.name)
```

## 🟢 Easy 2 – Check File Existence
```python
from pathlib import Path
print(Path('test.txt').exists())
```

## 🟡 Medium 1 – Read Text with Path
```python
from pathlib import Path
content = Path('test.txt').read_text()
print(content.strip())
```

## 🟡 Medium 2 – Write Text with Path
```python
from pathlib import Path
Path('output.txt').write_text('PyPhone')
print(Path('output.txt').read_text().strip())
```

## 🔴 Hard 1 – Create Directory
```python
from pathlib import Path
Path('temp_dir').mkdir(exist_ok=True)
print('created')
```

## 🔴 Hard 2 – Glob for Python Files
```python
from pathlib import Path
count = len(list(Path('.').glob('*.py')))
print(count)
```