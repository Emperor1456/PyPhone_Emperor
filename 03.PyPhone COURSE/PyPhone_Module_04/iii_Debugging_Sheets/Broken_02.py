# 🐛 BROKEN – Module 04, Lesson 34 (Scope)
# The function tries to modify a global variable without 'global' keyword.
x = 10
def change():
    x = x + 1   # ❌ UnboundLocalError: local variable 'x' referenced before assignment
change()
