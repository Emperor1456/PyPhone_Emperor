import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'my_decorator' in g and callable(g['my_decorator'])
easy=Task("Define a decorator function `my_decorator(func)` that prints 'Before' and 'After' around the function call. Define a dummy function and decorate it (just the decorator, no execution needed).", verify_easy, Level.EASY, hints=["def my_decorator(func):\n    def wrapper():\n        print('Before')\n        func()\n        print('After')\n    return wrapper"])
def verify_medium(g): return 'greet' in g and callable(g['greet']) and hasattr(g['greet'], '__wrapped__')
medium=Task("Use `@my_decorator` on a function `greet` that prints 'Hello'. Then call it.", verify_medium, Level.MEDIUM, hints=["@my_decorator\ndef greet():\n    print('Hello')","greet()"])
def verify_hard(g): return 'bold' in g and callable(g['bold']) and callable(g['bold'](lambda x: x)) and 'result' in g and g['result']=='<b>Hi</b>'
hard=Task("Write a decorator `bold` that wraps the return value of a string-returning function in <b>..</b>. Apply it to a function that returns 'Hi' and store result in 'result'.", verify_hard, Level.HARD, hints=["def bold(func):\n    def wrapper():\n        return f'<b>{func()}</b>'\n    return wrapper","@bold\ndef say():\n    return 'Hi'","result=say()"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
