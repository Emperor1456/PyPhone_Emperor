# L58 Solution – Project Architecture & Design

## 🟢 Easy 1 – Requirements List
```python
features = ['Add contact', 'List contacts', 'Search', 'Update', 'Delete']
print(features)
```

## 🟢 Easy 2 – Project Structure
```python
files = ['main.py', 'database.py', 'models.py', 'tests.py', 'requirements.txt']
print(files)
```

## 🟡 Medium 1 – Database Schema Design
```python
print('CREATE TABLE contacts (')
print('    id INTEGER PRIMARY KEY AUTOINCREMENT,')
print('    name TEXT NOT NULL,')
print('    phone TEXT NOT NULL UNIQUE,')
print('    email TEXT,')
print("    group_name TEXT DEFAULT 'General',")
print("    created_at TEXT DEFAULT (datetime('now'))")
print(');')
```

## 🟡 Medium 2 – CLI Interface Design
```python
print('python main.py add <name> <phone> [email] [group]')
print('python main.py list')
print('python main.py search <query>')
print('python main.py update <id> <new_phone>')
print('python main.py delete <id>')
```

## 🔴 Hard 1 – Module Responsibility Map
```python
desc = {
    'main.py': 'CLI entry point',
    'database.py': 'DB connection and schema',
    'models.py': 'CRUD operations',
    'tests.py': 'Unit tests'
}
print(desc)
```

## 🔴 Hard 2 – Design a Test Plan
```python
tests = [
    'test_add_contact',
    'test_list_contacts',
    'test_search_found',
    'test_search_not_found',
    'test_update_phone',
    'test_delete_contact'
]
print(tests)
```