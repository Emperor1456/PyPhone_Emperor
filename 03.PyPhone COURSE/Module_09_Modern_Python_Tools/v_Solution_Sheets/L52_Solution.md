# L52 Solution – Environment Variables & .env

## 🟢 Easy 1 – Read Environment Variable
```python
import os
print(os.getenv('HOME', 'not set'))
```

## 🟢 Easy 2 – Default Value for Missing Variable
```python
import os
print(os.getenv('NONEXISTENT', 'default_value'))
```

## 🟡 Medium 1 – Load .env File
```python
print('from dotenv import load_dotenv')
print('load_dotenv()')
```

## 🟡 Medium 2 – Set Environment Variable
```python
import os
os.environ['MY_VAR'] = 'emperor'
print(os.getenv('MY_VAR'))
```

## 🔴 Hard 1 – Check Multiple Variables
```python
import os
def get_config():
    host = os.getenv('DB_HOST', 'localhost')
    port = os.getenv('DB_PORT', '5432')
    return host, port
print(get_config())
```

## 🔴 Hard 2 – Secret Key Pattern
```python
import os
secret = os.getenv('SECRET_KEY')
if secret is None:
    secret = os.urandom(8).hex()
print(secret)
```