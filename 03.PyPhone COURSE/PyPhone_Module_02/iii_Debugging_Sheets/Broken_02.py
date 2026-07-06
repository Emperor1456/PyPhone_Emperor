# 🐛 BROKEN – Module 02, Lesson 19 (while loop)
# This while loop will run forever because i is never incremented.
i = 0
total = 0
while i < 5:
    total += i   # ❌ i never changes -> infinite loop
