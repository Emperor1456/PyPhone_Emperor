import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'Book' in g and callable(g['Book']) and 'b' in g and isinstance(g['b'], g['Book']) and str(g['b'])=='1984 by Orwell'
easy=Task("Define class `Book` with `__init__(title,author)` and `__str__` returning 'title by author'. Create instance `b` with '1984','Orwell'.", verify_easy, Level.EASY, hints=["class Book:\n    def __init__(self,title,author):\n        self.title=title\n        self.author=author\n    def __str__(self):\n        return f'{self.title} by {self.author}'","b=Book('1984','Orwell')"])
def verify_medium(g): return 'b' in g and len(g['b'])==0
medium=Task("Add a `__len__` method that returns 0 (or page count). Use len(b) and verify 0.", verify_medium, Level.MEDIUM, hints=["class Book:\n    ...\n    def __len__(self):\n        return 0","len(b)"])
def verify_hard(g): return 'Vector' in g and callable(g['Vector']) and 'v1' in g and 'v2' in g and (g['v1'] + g['v2']).x==6 and (g['v1'] + g['v2']).y==8
hard=Task("Define class `Vector` with x,y. Implement `__add__` to add two vectors. Create v1=(2,3), v2=(4,5), then add them.", verify_hard, Level.HARD, hints=["class Vector:\n    def __init__(self,x,y):\n        self.x=x\n        self.y=y\n    def __add__(self,other):\n        return Vector(self.x+other.x, self.y+other.y)","v1=Vector(2,3)","v2=Vector(4,5)","v3=v1+v2"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
