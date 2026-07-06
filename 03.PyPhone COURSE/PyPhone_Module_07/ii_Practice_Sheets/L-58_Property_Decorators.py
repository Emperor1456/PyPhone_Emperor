import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'Circle' in g and callable(g['Circle']) and 'c' in g and isinstance(g['c'], g['Circle']) and g['c'].radius==5
easy=Task("Define class `Circle` with `__init__(self,radius)` and a `@property` method `diameter` returning 2*radius. Create instance `c` with radius=5.", verify_easy, Level.EASY, hints=["class Circle:\n    def __init__(self,radius):\n        self.radius=radius\n    @property\n    def diameter(self):\n        return 2*self.radius","c=Circle(5)"])
def verify_medium(g): return 'c' in g and g['c'].diameter==10
medium=Task("Access `c.diameter` and verify it returns 10.", verify_medium, Level.MEDIUM, hints=["print(c.diameter)"])
def verify_hard(g): return 'Temperature' in g and callable(g['Temperature']) and 't' in g and isinstance(g['t'], g['Temperature']) and g['t'].fahrenheit==32
hard=Task("Define class `Temperature` with `__init__(self,celsius)`. Add a `@property` `fahrenheit` returning celsius*9/5+32. Create `t` with celsius=0, then access fahrenheit.", verify_hard, Level.HARD, hints=["class Temperature:\n    def __init__(self,celsius):\n        self.celsius=celsius\n    @property\n    def fahrenheit(self):\n        return self.celsius*9/5+32","t=Temperature(0)","print(t.fahrenheit)"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
