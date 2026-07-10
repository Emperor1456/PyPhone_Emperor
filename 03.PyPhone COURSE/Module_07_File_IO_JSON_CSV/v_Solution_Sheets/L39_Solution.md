# L39 Solution – JSON

## 🟢 Easy 1 – Parse JSON String
```python
import json
data = json.loads('{"key":"value"}')
print(data)
```

## 🟢 Easy 2 – Convert Dict to JSON String
```python
import json
json_str = json.dumps({'name':'Emperor'})
print(json_str)
```

## 🟡 Medium 1 – Write JSON to File
```python
import json
with open('data.json', 'w') as f:
    json.dump({'age':18}, f)
with open('data.json', 'r') as f:
    data = json.load(f)
print(data)
```

## 🟡 Medium 2 – Pretty Print JSON
```python
import json
d = {'name':'Emperor','skills':['Python','SQL']}
with open('pretty.json', 'w') as f:
    json.dump(d, f, indent=2)
print(open('pretty.json').read().strip())
```

## 🔴 Hard 1 – Access Nested JSON
```python
import json
data = json.loads('{"user":{"name":"Emperor","age":18}}')
print(data['user']['name'])
```

## 🔴 Hard 2 – JSON Array – Sum Ages
```python
import json
data = json.loads('[{"name":"A","age":30},{"name":"B","age":25}]')
total = sum(item['age'] for item in data)
print(total)
```