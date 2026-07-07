import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Define class `Dog` with method `bark` that prints 'Woof!'. Create instance `d` and call `d.bark()`.",
    expected_output="Woof!",
    level=Level.EASY,
    hints=["class Dog:\n    def bark(self):\n        print('Woof!')","d=Dog()","d.bark()"]
)

medium = Task(
    description="Define class `Cat` with `__init__` setting `self.name`. Create instance `c` with name 'Whiskers' and print `c.name`.",
    expected_output="Whiskers",
    level=Level.MEDIUM,
    hints=["class Cat:\n    def __init__(self,name):\n        self.name=name","c=Cat('Whiskers')","print(c.name)"]
)

hard = Task(
    description="Define class `Book` with `__init__(self,title,author)`. Create instance `b` with title '1984' and author 'Orwell'. Print both attributes separated by a space.",
    expected_output="1984 Orwell",
    level=Level.HARD,
    hints=["class Book:\n    def __init__(self,title,author):\n        self.title=title\n        self.author=author","b=Book('1984','Orwell')","print(b.title,b.author)"]
)

def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
