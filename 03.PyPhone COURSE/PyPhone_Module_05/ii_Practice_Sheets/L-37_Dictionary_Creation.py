import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Create a dict with keys 'name':'Emperor','age':18. Print it.",
    expected_output="{'name': 'Emperor', 'age': 18}",
    level=Level.EASY,
    hints=["d={'name':'Emperor','age':18}", "print(d)"]
)

medium = Task(
    description="Create dict using dict(brand='Samsung',model='Galaxy'). Print it.",
    expected_output="{'brand': 'Samsung', 'model': 'Galaxy'}",
    level=Level.MEDIUM,
    hints=["info=dict(brand='Samsung',model='Galaxy')", "print(info)"]
)

hard = Task(
    description="Create nested dict: person={'name':'Emperor','age':18}, and outer dict with 'person':person, 'city':'Dhaka'. Print outer.",
    expected_output="{'person': {'name': 'Emperor', 'age': 18}, 'city': 'Dhaka'}",
    level=Level.HARD,
    hints=["person={'name':'Emperor','age':18}", "outer={'person':person,'city':'Dhaka'}", "print(outer)"]
)

def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
