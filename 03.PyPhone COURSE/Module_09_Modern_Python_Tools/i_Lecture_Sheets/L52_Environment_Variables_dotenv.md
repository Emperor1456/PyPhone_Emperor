# 📘 PyPhone Emperor v3.0 · Module 9
# 📖 L‑52 – Environment Variables & `.env` Files

---

## 🎯 OBJECTIVE — What You Will Master

> Keep secrets out of your code – the secure way to configure applications.

- 🔐 **Environment variables** – values set outside the code
- 📄 **`.env` files** – store variables locally (never commit to Git)
- 🧪 **`os.getenv()`** – read environment variables safely
- 🛠️ **`python-dotenv`** – load `.env` files automatically

---

## 🧱 READING ENVIRONMENT VARIABLES

```python
import os
api_key = os.getenv("API_KEY", "default_value")
print(api_key)
```

In Termux, set an environment variable:
```bash
export API_KEY="my_secret_key"
python script.py
```

---

## 🧱 USING `.env` FILES

Install `python-dotenv`:
```bash
pip install python-dotenv
```

Create a `.env` file:
```
API_KEY=my_secret_key
DATABASE_URL=sqlite:///local.db
```

Load it in Python:
```python
from dotenv import load_dotenv
import os

load_dotenv()  # loads .env from current directory
print(os.getenv("API_KEY"))
```

> ⚠️ **WARNING:** Add `.env` to your `.gitignore` immediately. Never commit secrets to version control.

---

## 💡 Real‑world Usage

**Banking – database credentials**
```python
import os
db_url = os.getenv("DATABASE_URL")
```

**E‑commerce – payment gateway key**
```python
stripe_key = os.getenv("STRIPE_SECRET_KEY")
```

**Logistics – API token**
```python
token = os.getenv("SHIPPING_API_TOKEN")
```

---

## 🔍 Practice Preview

| Level | Task |
|-------|------|
| Easy | Print an environment variable with a default fallback. |
| Medium | Load a `.env` file and print a variable from it. |
| Hard | Write a function that returns a config dict from environment variables. |

Run the coach:
```bash
python ii_Practice_Sheets/L52_Environment_Variables_dotenv.py
```

---

## 📌 Key Takeaway
- Environment variables keep configuration out of code.
- `.env` files are for local development; never commit them.
- Use `os.getenv()` with a default for safe access.

*For Emperor.*