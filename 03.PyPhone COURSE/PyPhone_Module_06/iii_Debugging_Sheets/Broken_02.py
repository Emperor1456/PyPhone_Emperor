# 🐛 BROKEN – Module 06, Lesson 48 (Exceptions)
# Using a bare except that catches even KeyboardInterrupt, bad practice.
try:
    x = 1 / 0
except:
    print("An error occurred")   # ❌ too broad
