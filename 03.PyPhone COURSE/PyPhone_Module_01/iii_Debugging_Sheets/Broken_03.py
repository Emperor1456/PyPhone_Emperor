# 🐛 BROKEN – Module 01, Lesson 11 (Bitwise)
# This script attempts to combine bitwise operations but has wrong operator and logic.

x = 5 & 3   # correct (result 1)
y = 5 | 3   # correct (result 7)
# The next line uses a non‑existent operator
z = x ! y   # ❌ Python does not have '!'; should use ^ for XOR
print(x, y, z)
