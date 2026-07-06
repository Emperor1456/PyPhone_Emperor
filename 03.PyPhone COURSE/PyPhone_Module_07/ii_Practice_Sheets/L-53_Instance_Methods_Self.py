import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'Dog' in g and callable(g['Dog']) and 'd' in g and isinstance(g['d'], g['Dog']) and g['d'].name=='Rex'
easy=Task("Define class `Dog` with `__init__` setting `self.name`, and method `speak` returning 'Woof! I am ' + name. Create instance `d` with name 'Rex'.", verify_easy, Level.EASY, hints=["class Dog:\n    def __init__(self,name):\n        self.name=name\n    def speak(self):\n        return 'Woof! I am '+self.name","d=Dog('Rex')"])
def verify_medium(g): return 'd' in g and g['d'].speak()=='Woof! I am Rex'
medium=Task("Using the above class, call `d.speak()` and verify it returns the correct string (store result? No, we'll just check existence). Actually verify that speak method exists and works.", verify_medium, Level.MEDIUM, hints=["result=d.speak()","print(result)"])
def verify_hard(g): return 'Counter' in g and callable(g['Counter']) and 'c' in g and isinstance(g['c'], g['Counter']) and g['c'].count==0 and hasattr(g['c'], 'increment')
hard=Task("Define class `Counter` with `__init__` setting `self.count=0`, and method `increment(self)` that increments count by 1. Create instance `c`.", verify_hard, Level.HARD, hints=["class Counter:\n    def __init__(self):\n        self.count=0\n    def increment(self):\n        self.count+=1","c=Counter()"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
