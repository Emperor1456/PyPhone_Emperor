import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Define `Circle` with `__init__(radius)` and `@property` `diameter` returning 2*radius. Create `c` with radius=5 and print `c.diameter`.",
    expected_output="10",
    level=Level.EASY,
    hints=["class Circle:\n    def __init__(self,radius):\n        self.radius=radius\n    @property\n    def diameter(self):\n        return 2*self.radius","c=Circle(5)","print(c.diameter)"]
)

medium = Task(
    description="Define `Temperature` with `__init__(celsius)` and `@property` `fahrenheit` returning celsius*9/5+32. Create `t` with celsius=0 and print `t.fahrenheit`.",
    expected_output="32.0",
    level=Level.MEDIUM,
    hints=["class Temperature:\n    def __init__(self,celsius):\n        self.celsius=celsius\n    @property\n    def fahrenheit(self):\n        return self.celsius*9/5+32","t=Temperature(0)","print(t.fahrenheit)"]
)

hard = Task(
    description="Using same Temperature class, create instance with celsius=100 and print fahrenheit.",
    expected_output="212.0",
    level=Level.HARD,
    hints=["t=Temperature(100)","print(t.fahrenheit)"]
)

def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
