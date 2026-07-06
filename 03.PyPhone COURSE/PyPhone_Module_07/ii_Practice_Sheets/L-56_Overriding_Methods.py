import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'Parent' in g and callable(g['Parent']) and 'Child' in g and callable(g['Child']) and issubclass(g['Child'], g['Parent'])
easy=Task("Define `Parent` with method `show` returning 'Parent'. Define `Child` overriding `show` to return 'Child'. Create instance `c` of Child.", verify_easy, Level.EASY, hints=["class Parent:\n    def show(self):\n        return 'Parent'","class Child(Parent):\n    def show(self):\n        return 'Child'","c=Child()"])
def verify_medium(g): return 'c' in g and g['c'].show()=='Child'
medium=Task("Call `c.show()` and verify it returns 'Child'.", verify_medium, Level.MEDIUM, hints=["result=c.show()","print(result)"])
def verify_hard(g): return 'GrandChild' in g and callable(g['GrandChild']) and issubclass(g['GrandChild'], g['Child']) and 'gc' in g and isinstance(g['gc'], g['GrandChild']) and g['gc'].show()=='Child'
hard=Task("Create `GrandChild` inheriting from `Child` without overriding. Call `show()` on an instance, should return 'Child'.", verify_hard, Level.HARD, hints=["class GrandChild(Child):\n    pass","gc=GrandChild()","print(gc.show())"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
