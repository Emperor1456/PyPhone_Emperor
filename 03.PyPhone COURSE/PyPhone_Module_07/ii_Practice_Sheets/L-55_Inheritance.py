import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Define `Animal` with method `speak` returning '?'. Define `Dog(Animal)` overriding `speak` to return 'Woof'. Create `d=Dog()` and print `d.speak()`.",
    expected_output="Woof",
    level=Level.EASY,
    hints=["class Animal:\n    def speak(self):\n        return '?'","class Dog(Animal):\n    def speak(self):\n        return 'Woof'","d=Dog()","print(d.speak())"]
)

medium = Task(
    description="Add another subclass `Cat` overriding `speak` to return 'Meow'. Create `c=Cat()` and print `c.speak()`.",
    expected_output="Meow",
    level=Level.MEDIUM,
    hints=["class Cat(Animal):\n    def speak(self):\n        return 'Meow'","c=Cat()","print(c.speak())"]
)

hard = Task(
    description="Define `Bird(Animal)` that does NOT override speak. Create instance and print `speak()`. Should return '?'.",
    expected_output="?",
    level=Level.HARD,
    hints=["class Bird(Animal):\n    pass","b=Bird()","print(b.speak())"]
)

def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
