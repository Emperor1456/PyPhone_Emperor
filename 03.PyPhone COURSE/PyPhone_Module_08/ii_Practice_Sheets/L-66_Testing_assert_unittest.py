import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'result' in g and g['result']=='pass'
easy=Task("Use assert to verify 1+1==2. If it passes, set result='pass'.", verify_easy, Level.EASY, hints=["assert 1+1==2","result='pass'"])
def verify_medium(g): return 'test_func' in g and callable(g['test_func'])
medium=Task("Define a function `test_func` that uses assert to check that `sum([1,2,3])` equals 6.", verify_medium, Level.MEDIUM, hints=["def test_func():\n    assert sum([1,2,3])==6"])
def verify_hard(g): return 'suite' in g and hasattr(g['suite'], '__iter__')
hard=Task("Create a unittest.TestCase subclass with a test method that checks `self.assertEqual(2+2,4)`. Store the class in 'TestClass'.", verify_hard, Level.HARD, hints=["import unittest","class TestMath(unittest.TestCase):\n    def test_addition(self):\n        self.assertEqual(2+2,4)","TestClass=TestMath"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
