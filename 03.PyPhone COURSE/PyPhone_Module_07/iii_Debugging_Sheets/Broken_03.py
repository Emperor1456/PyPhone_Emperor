# 🐛 BROKEN – Module 07, Lesson 58 (Property Decorators)
# Using @property incorrectly without a getter, or trying to assign to a property.
class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius

c = Circle(5)
c.diameter = 20   # ❌ AttributeError: can't set attribute
