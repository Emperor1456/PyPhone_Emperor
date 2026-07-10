# L51 Solution – requests – HTTP & APIs

## 🟢 Easy 1 – Import requests
```python
import requests
print('requests ready')
```

## 🟢 Easy 2 – GET Request Status Code
```python
import requests
r = requests.get('https://httpbin.org/status/200')
print(r.status_code)
```

## 🟡 Medium 1 – GET JSON Response
```python
import requests
r = requests.get('https://httpbin.org/json')
data = r.json()
print(data['slideshow']['title'])
```

## 🟡 Medium 2 – POST Request with JSON
```python
import requests
r = requests.post('https://httpbin.org/post', json={'name':'Emperor'})
print(r.json()['json'])
```

## 🔴 Hard 1 – Handle Request Error
```python
import requests
try:
    requests.get('https://invalid.example.com', timeout=3)
except:
    print('Connection failed')
```

## 🔴 Hard 2 – Send Headers
```python
import requests
headers = {'X-Emperor': 'PyPhone'}
r = requests.get('https://httpbin.org/headers', headers=headers)
print(r.json()['headers']['X-Emperor'])
```