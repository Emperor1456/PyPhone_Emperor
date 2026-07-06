# 🐛 BROKEN – Module 03, Lesson 26 (List Methods)
# This script attempts to sort a list but forgets to assign the result.
lst = [3,1,5]
sorted(lst)   # ❌ sorted() returns a new list, but we didn't store it
print(lst)    # prints [3,1,5] (unchanged)
