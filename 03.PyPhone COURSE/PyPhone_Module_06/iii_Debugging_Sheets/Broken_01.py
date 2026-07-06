# 🐛 BROKEN – Module 06, Lesson 44 (Reading Files)
# Tries to read a file that doesn't exist without error handling.
f = open('nonexistent.txt','r')
content = f.read()
f.close()
# ❌ FileNotFoundError
