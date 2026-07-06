# 🐛 BROKEN – Module 07, Lesson 55 (Inheritance)
# Attempting to call a method that doesn't exist in the parent class.
class Animal:
    pass
class Dog(Animal):
    def speak(self):
        print("Woof")
d = Dog()
d.bark()   # ❌ AttributeError: 'Dog' object has no attribute 'bark'
