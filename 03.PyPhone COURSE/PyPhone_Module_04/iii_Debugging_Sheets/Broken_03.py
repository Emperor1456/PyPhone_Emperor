# 🐛 BROKEN – Module 04, Lesson 36 (Recursion)
# The recursive function has no base case, causing infinite recursion.
def infinite(n):
    return infinite(n-1)   # ❌ RecursionError
infinite(5)
