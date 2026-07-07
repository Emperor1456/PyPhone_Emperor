import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Use assert to verify 1+1==2. If it passes, print 'pass'.",
    expected_output="pass",
    level=Level.EASY,
    hints=["assert 1+1==2","print('pass')"]
)

medium = Task(
    description="Define a function `test_sum` that uses assert to check that sum([1,2,3]) equals 6. Call the function and print 'ok' after.",
    expected_output="ok",
    level=Level.MEDIUM,
    hints=["def test_sum():\n    assert sum([1,2,3])==6","test_sum()","print('ok')"]
)

hard = Task(
    description="Create a unittest.TestCase subclass with a method that checks `self.assertEqual(2+2,4)`. Run it using unittest.main(argv=[''],exit=False) and print 'done' after.",
    expected_output="done",
    level=Level.HARD,
    hints=["import unittest","class TestMath(unittest.TestCase):\n    def test_addition(self):\n        self.assertEqual(2+2,4)","unittest.main(argv=[''],exit=False)","print('done')"]
)

def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
