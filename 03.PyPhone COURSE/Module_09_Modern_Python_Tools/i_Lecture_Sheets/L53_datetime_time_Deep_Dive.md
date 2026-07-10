# 📘 PyPhone Emperor v3.0 · Module 9
# 📖 L‑53 – `datetime` & `time` Deep Dive

---

## 🎯 OBJECTIVE — What You Will Master

> Handle dates, times, and timestamps like a professional.

- 📅 `datetime` – date and time objects
- ⏰ `time` – time‑related functions (sleep, epoch)
- 🧪 `strftime()` / `strptime()` – format and parse dates
- ⚖️ `timedelta` – date arithmetic
- 🛠️ **Real‑world** – scheduling, logging, age calculations

---

## 🧱 CURRENT DATE AND TIME

```python
from datetime import datetime, date, timedelta

now = datetime.now()
print(now)                      # 2026-07-09 14:30:00
print(now.strftime("%Y-%m-%d")) # 2026-07-09
```

---

## 🧱 PARSING A DATE STRING

```python
date_str = "2026-01-15"
parsed = datetime.strptime(date_str, "%Y-%m-%d")
print(parsed.year)   # 2026
```

---

## 🧱 DATE ARITHMETIC

```python
today = date.today()
next_week = today + timedelta(weeks=1)
age = today - date(2008, 1, 1)
print(age.days)      # ~6750
```

---

## 🧱 TIME MODULE

```python
import time
print(time.time())   # Unix timestamp
time.sleep(2)        # pause for 2 seconds
```

---

## 💡 Real‑world Usage

**Banking – calculate interest period**
```python
start = date(2026, 1, 1)
end = date(2026, 12, 31)
days = (end - start).days
```

**E‑commerce – delivery estimate**
```python
order_date = datetime.now()
delivery_date = order_date + timedelta(days=3)
```

**Logistics – timestamp shipment events**
```python
event_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

---

## 🔍 Practice Preview

| Level | Task |
|-------|------|
| Easy | Print today's date in `YYYY-MM-DD` format. |
| Medium | Calculate the number of days until a future date. |
| Hard | Parse a date string, add 30 days, and print the new date. |

Run the coach:
```bash
python ii_Practice_Sheets/L53_datetime_time_Deep_Dive.py
```

---

## 📌 Key Takeaway
- `datetime` handles dates, times, and intervals.
- `strftime` formats; `strptime` parses.
- `timedelta` performs date arithmetic.

*For Emperor.*