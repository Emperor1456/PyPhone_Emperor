import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task

easy = Task(
    description="Define a decorator `bold` that wraps the return value of a function in <b>..</b>. Apply it to a function `say()` returning 'Hi'. Print the result of calling `say()`.",
    expected_output="<b>Hi</b>",
    level=Level.EASY,
    hints=["def bold(func):\n    def wrapper():\n        return f'<b>{func()}</b>'\n    return wrapper","@bold\ndef say():\n    return 'Hi'","print(say())"]
)

medium = Task(
    description="Define a decorator `uppercase` that converts the string return value to uppercase. Apply to a function `greet` returning 'hello'. Print the result.",
    expected_output="HELLO",
    level=Level.MEDIUM,
    hints=["def uppercase(func):\n    def wrapper():\n        return func().upper()\n    return wrapper","@uppercase\ndef greet():\n    return 'hello'","print(greet())"]
)

hard = Task(
    description="Stack both decorators on a function `message` returning 'hi'. The bold should be applied first (outermost). Print result. (Should be <b>HI</b>).",
    expected_output="<b>HI</b>",
    level=Level.HARD,
    hints=["@bold\n@uppercase\ndef message():\n    return 'hi'","print(message())"]
)

def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
