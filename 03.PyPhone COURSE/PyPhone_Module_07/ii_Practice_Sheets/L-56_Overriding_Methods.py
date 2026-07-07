import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Define `Parent` with method `show` returning 'Parent'. Define `Child(Parent)` overriding `show` to return 'Child'. Create instance `c` and print `c.show()`.",
    expected_output="Child",
    level=Level.EASY,
    hints=["class Parent:\n    def show(self):\n        return 'Parent'","class Child(Parent):\n    def show(self):\n        return 'Child'","c=Child()","print(c.show())"]
)

medium = Task(
    description="Create `GrandChild(Child)` without overriding. Print `show()` – should return 'Child'.",
    expected_output="Child",
    level=Level.MEDIUM,
    hints=["class GrandChild(Child):\n    pass","gc=GrandChild()","print(gc.show())"]
)

hard = Task(
    description="Override `show` in `GrandChild` to return 'GrandChild'. Print the result.",
    expected_output="GrandChild",
    level=Level.HARD,
    hints=["class GrandChild(Child):\n    def show(self):\n        return 'GrandChild'","gc=GrandChild()","print(gc.show())"]
)

def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
