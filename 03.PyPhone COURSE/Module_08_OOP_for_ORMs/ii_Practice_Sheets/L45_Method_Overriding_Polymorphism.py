import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "🎭  Override Method\n\n"
        "Define `Parent` with method `show` returning 'Parent'. `Child(Parent)` overrides `show` to return 'Child'.\n"
        "Create `c = Child()` and print `c.show()`.\n\n"
        "Expected output: Child"
    ),
    expected_output="Child",
    level=Level.EASY,
    hints=[
        "class Parent:",
        "    def show(self): return 'Parent'",
        "class Child(Parent):",
        "    def show(self): return 'Child'",
        "c = Child()",
        "print(c.show())"
    ]
)

easy2 = Task(
    description=(
        "🧬  GrandChild Inherits Override\n\n"
        "Create `GrandChild(Child)` without overriding. Print `show()`.\n\n"
        "Expected output: Child"
    ),
    expected_output="Child",
    level=Level.EASY,
    hints=[
        "class Parent: def show(self): return 'Parent'",
        "class Child(Parent): def show(self): return 'Child'",
        "class GrandChild(Child): pass",
        "gc = GrandChild()",
        "print(gc.show())"
    ]
)

medium1 = Task(
    description=(
        "🔄  GrandChild Overrides Again\n\n"
        "Override `show` in GrandChild to return 'GrandChild'. Print the result.\n\n"
        "Expected output: GrandChild"
    ),
    expected_output="GrandChild",
    level=Level.MEDIUM,
    hints=[
        "class GrandChild(Child):",
        "    def show(self): return 'GrandChild'",
        "gc = GrandChild()",
        "print(gc.show())"
    ]
)

medium2 = Task(
    description=(
        "🦆  Polymorphic List\n\n"
        "Create a list of different objects (Parent(), Child(), GrandChild()). Loop and call `show()` on each, printing results.\n\n"
        "Expected output:\nParent\nChild\nGrandChild"
    ),
    expected_output="Parent\nChild\nGrandChild",
    level=Level.MEDIUM,
    hints=[
        "objs = [Parent(), Child(), GrandChild()]",
        "for obj in objs:",
        "    print(obj.show())"
    ]
)

hard1 = Task(
    description=(
        "💳  Payment Polymorphism\n\n"
        "Define classes `CreditCard` and `PayPal`, each with a `pay()` method returning 'Card payment' and 'PayPal payment'.\n"
        "Write a function `process(payment)` that prints payment.pay(). Call with both.\n\n"
        "Expected output:\nCard payment\nPayPal payment"
    ),
    expected_output="Card payment\nPayPal payment",
    level=Level.HARD,
    hints=[
        "class CreditCard:",
        "    def pay(self): return 'Card payment'",
        "class PayPal:",
        "    def pay(self): return 'PayPal payment'",
        "def process(payment): print(payment.pay())",
        "process(CreditCard())",
        "process(PayPal())"
    ]
)

hard2 = Task(
    description=(
        "🐾  Animal Sounds Polymorphism\n\n"
        "Define classes `Dog`, `Cat`, `Bird`, each with `speak()` returning 'Woof', 'Meow', 'Tweet'.\n"
        "Create list of animals, loop and print each sound.\n\n"
        "Expected output:\nWoof\nMeow\nTweet"
    ),
    expected_output="Woof\nMeow\nTweet",
    level=Level.HARD,
    hints=[
        "class Dog: def speak(self): return 'Woof'",
        "class Cat: def speak(self): return 'Meow'",
        "class Bird: def speak(self): return 'Tweet'",
        "animals = [Dog(), Cat(), Bird()]",
        "for a in animals: print(a.speak())"
    ]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L45.json")
