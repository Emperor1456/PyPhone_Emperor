# 📘 PyPhone Emperor v3.0 · Module 9
# 📖 L‑51 – `requests` – HTTP & APIs

---

## 🎯 OBJECTIVE — What You Will Master

> Talk to the internet – fetch data from web services.

- 🌐 **HTTP methods** – GET, POST, PUT, DELETE
- 📨 **`requests.get()`** – retrieve data from an API
- 📬 **`requests.post()`** – send data to a server
- 📊 **JSON responses** – `.json()` to parse API replies
- ⚠️ **Status codes** – check `.status_code` before processing

---

## 🧱 SIMPLE GET REQUEST

```python
import requests
response = requests.get("https://api.github.com")
print(response.status_code)  # 200
print(response.json())       # dict with API info
```

---

## 🧱 HANDLING ERRORS

```python
response = requests.get("https://api.example.com/data")
if response.status_code == 200:
    data = response.json()
else:
    print(f"Error: {response.status_code}")
```

---

## 🧱 POST REQUEST WITH DATA

```python
payload = {"name": "Emperor", "age": 18}
response = requests.post("https://httpbin.org/post", json=payload)
print(response.json())
```

---

## 💡 Real‑world Usage

**Banking – fetch exchange rates**
```python
rates = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
print(rates["rates"]["BDT"])
```

**E‑commerce – search products**
```python
results = requests.get("https://api.store.com/search", params={"q": "laptop"}).json()
```

**Logistics – track shipment**
```python
tracking = requests.get(f"https://api.ship.com/track/{tracking_id}").json()
print(tracking["status"])
```

---

## 🔍 Practice Preview

| Level | Task |
|-------|------|
| Easy | Import `requests` and print the status code of a known URL. |
| Medium | Fetch JSON from an API and print a specific key. |
| Hard | Send a POST request with JSON data and print the response. |

Run the coach:
```bash
python ii_Practice_Sheets/L51_requests_HTTP_APIs.py
```

---

## 📌 Key Takeaway
- `requests` is the standard for HTTP in Python.
- Always check `status_code` before using the data.
- `.json()` converts the response to a dictionary.

*For Emperor.*