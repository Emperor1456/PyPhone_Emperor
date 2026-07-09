# 📘 PyPhone Emperor · Module 3  
# 📖 L‑25 – List Creation & Indexing (Ordered Data Collections)

---

## 🎯 OBJECTIVE  
Master **list creation** and **indexing** to store and retrieve ordered business data.  
Lists hold sequences of invoice amounts, product names, or customer IDs — each element accessible by its position.  
Zero‑based indexing and negative indexing let you grab exactly what you need.

---

## 🧱 BRICK 1 – Creating Lists and Accessing Elements

A list is defined with square brackets `[]` and comma‑separated items.

```python
numbers = [1, 2, 3]
print(numbers)   # [1, 2, 3]
```

**① Create a list of daily sales figures**
```python
sales = [250, 410, 320, 180]
print(sales)       # [250, 410, 320, 180]
```

**② Access elements by index (0 = first)**
```python
prices = [10, 20, 30, 40]
first  = prices[0]   # 10
second = prices[1]   # 20
third  = prices[2]   # 30
print(third)         # 30
```

**③ Use negative indexing to get the last element**
```python
prices = [10, 20, 30, 40]
last = prices[-1]    # 40
print(last)          # 40
```

> 💡 **INSIGHT:** Lists are **ordered** and **mutable** — you can add, remove, and change items after creation.

> ⚠️ **WARNING:** Accessing an index that doesn’t exist (e.g., `prices[4]` on a list of length 4) raises an `IndexError`. Always keep within `0` to `len(list)-1` or use negative indices.

---

## 🧱 BRICK 2 – Business Scenarios for List Indexing

**④ Extract the first transaction of the day**
```python
tx_amounts = [1200, 340, 990, 4500]
first_tx = tx_amounts[0]   # 1200
print(f"Opening transaction: {first_tx}")
```

**⑤ Get the most recent sale (last element)**
```python
daily_sales = [89, 145, 320, 210]
last_sale = daily_sales[-1]   # 210
print(f"Latest sale: {last_sale}")
```

**⑥ Retrieve the third product from an inventory list**
```python
products = ['laptop', 'mouse', 'keyboard', 'monitor']
third_item = products[2]      # 'keyboard'
print(f"Third product: {third_item}")
```

**⑦ Access a nested list for matrix data**
```python
matrix = [[1, 2], [3, 4], [5, 6]]
first_row_second_col = matrix[0][1]   # 2
print(first_row_second_col)
```

> 💡 **ADVANCED TIP – `len()` for safe access:**  
> Use `len(list)` to know the size. The last valid index is `len(list) - 1`.  
> `len([10,20,30])` → 3, so indices 0,1,2 are safe.

---

## 💡 Real‑world Usage

**Banking – store monthly fees and retrieve the latest**
```python
monthly_fees = [5, 5, 5, 10]
latest_fee = monthly_fees[-1]   # 10
print(f"Current month fee: {latest_fee}")
```

**E‑commerce – fetch the first item in a wishlist**
```python
wishlist = ['phone', 'headphones', 'charger']
first_wish = wishlist[0]   # 'phone'
print(f"Top wish: {first_wish}")
```

**Logistics – get the weight of the third parcel**
```python
parcel_weights = [12.5, 8.3, 15.0, 9.7]
third_weight = parcel_weights[2]   # 15.0
print(f"Third parcel: {third_weight}kg")
```

**HR – find the second employee in a department list**
```python
team = ['Emperor', 'Rahim', 'Karim']
second_member = team[1]   # 'Rahim'
print(f"Second team member: {second_member}")
```

**Reporting – retrieve the highest temperature of the week (last day)**
```python
weekly_temps = [31, 33, 34, 32, 30, 29, 35]
weekend_temp = weekly_temps[-1]   # 35
print(f"Sunday temp: {weekend_temp}°C")
```

---

## 🔍 Practice Preview
You will write three list indexing mini‑programs.

| Level  | Task | Expected Output |
|--------|------|-----------------|
| Easy   | Create list `[1,2,3]` and print it. | `[1, 2, 3]`     |
| Medium | `lst=[10,20,30,40]`. Print the third element (index 2). | `30`            |
| Hard   | `lst=[10,20,30,40]`. Print the last element using negative indexing. | `40`            |

Run the coach:
```bash
python ii_Practice_Sheets/L-25_List_Creation_Indexing.py
```
Choose `1`, `2`, or `3`. Type your code; the engine checks output.

---

## 📌 Key Takeaway
- Lists are created with `[]`; elements separated by `,`.
- Indexing starts at 0 for the first element.
- Negative indices count from the end (`-1` is last).
- Use `len(list)` to determine the number of elements.
- Lists are mutable — you’ll learn to modify them next.