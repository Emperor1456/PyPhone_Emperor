# 🐛 BROKEN – Module 06, Lesson 50 (finally/else)
# The else block is incorrectly indented (should be after except, not inside try).
try:
    x = 1
else:
    print("No error")   # ❌ SyntaxError
