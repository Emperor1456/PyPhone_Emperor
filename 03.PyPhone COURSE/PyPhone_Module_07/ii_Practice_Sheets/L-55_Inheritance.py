import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'Animal' in g and callable(g['Animal']) and 'Dog' in g and callable(g['Dog']) and issubclass(g['Dog'], g['Animal'])
easy=Task("Define base class `Animal` with method `speak` returning '?'. Define subclass `Dog` that overrides `speak` to return 'Woof'. Create `d=Dog()`.", verify_easy, Level.EASY, hints=["class Animal:\n    def speak(self):\n        return '?'","class Dog(Animal):\n    def speak(self):\n        return 'Woof'","d=Dog()"])
def verify_medium(g): return 'd' in g and g['d'].speak()=='Woof'
medium=Task("Call `d.speak()` and verify it returns 'Woof'.", verify_medium, Level.MEDIUM, hints=["result=d.speak()","print(result)"])
def verify_hard(g): return 'Cat' in g and callable(g['Cat']) and issubclass(g['Cat'], g['Animal']) and 'c' in g and isinstance(g['c'], g['Cat']) and g['c'].speak()=='Meow'
hard=Task("Add another subclass `Cat` that overrides `speak` to return 'Meow'. Create instance `c`.", verify_hard, Level.HARD, hints=["class Cat(Animal):\n    def speak(self):\n        return 'Meow'","c=Cat()"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
