# 🐛 BROKEN – Module 08, Lesson 61 (Decorators)
# The decorator forgets to return the wrapper function.
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    # ❌ missing return wrapper

@my_decorator
def hello():
    print("Hello")
hello()   # TypeError: 'NoneType' object is not callable
