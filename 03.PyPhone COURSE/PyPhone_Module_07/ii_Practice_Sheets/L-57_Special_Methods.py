import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Define `Book` with `__init__(title,author)` and `__str__` returning 'title by author'. Create `b` for '1984','Orwell' and print `str(b)`.",
    expected_output="1984 by Orwell",
    level=Level.EASY,
    hints=["class Book:\n    def __init__(self,title,author):\n        self.title=title\n        self.author=author\n    def __str__(self):\n        return f'{self.title} by {self.author}'","b=Book('1984','Orwell')","print(str(b))"]
)

medium = Task(
    description="Add `__len__` to `Book` that returns 0. Print `len(b)`.",
    expected_output="0",
    level=Level.MEDIUM,
    hints=["class Book:\n    ...\n    def __len__(self):\n        return 0","print(len(b))"]
)

hard = Task(
    description="Define `Vector` with x,y and `__add__` to add two vectors. Create v1=(2,3), v2=(4,5), print (v1+v2).x and (v1+v2).y on separate lines.",
    expected_output="6\n8",
    level=Level.HARD,
    hints=["class Vector:\n    def __init__(self,x,y):\n        self.x=x\n        self.y=y\n    def __add__(self,other):\n        return Vector(self.x+other.x, self.y+other.y)","v1=Vector(2,3); v2=Vector(4,5); v3=v1+v2","print(v3.x)","print(v3.y)"]
)

def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
