import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'Dog' in g and callable(g['Dog']) and 'd' in g and isinstance(g['d'], g['Dog'])
easy=Task("Define a class `Dog` with a method `bark` that prints 'Woof!'. Then create an instance `d` and assign it.", verify_easy, Level.EASY, hints=["class Dog:\n    def bark(self):\n        print('Woof!')","d=Dog()"])
def verify_medium(g): return 'Cat' in g and callable(g['Cat']) and 'c' in g and isinstance(g['c'], g['Cat']) and hasattr(g['c'], 'name')
medium=Task("Define class `Cat` with an `__init__` that sets `self.name`. Create instance `c` with name 'Whiskers'.", verify_medium, Level.MEDIUM, hints=["class Cat:\n    def __init__(self,name):\n        self.name=name","c=Cat('Whiskers')"])
def verify_hard(g): return 'Book' in g and callable(g['Book']) and 'b' in g and isinstance(g['b'], g['Book']) and g['b'].title=='1984' and g['b'].author=='Orwell'
hard=Task("Define class `Book` with `__init__(self,title,author)`. Create instance `b` with title '1984' and author 'Orwell'.", verify_hard, Level.HARD, hints=["class Book:\n    def __init__(self,title,author):\n        self.title=title\n        self.author=author","b=Book('1984','Orwell')"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
