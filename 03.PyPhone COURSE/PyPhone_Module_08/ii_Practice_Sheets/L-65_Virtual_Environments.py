import sys; sys.path.append("../.."); from practice_engine import Task, Level, run_task
def verify_easy(g): return 'info' in g and isinstance(g['info'], str)
easy=Task("Write a Python script that prints the path of the current Python executable (sys.executable) into variable 'info' (just store it). But we're in Termux; just use sys.executable.", verify_easy, Level.EASY, hints=["import sys","info=sys.executable"])
def verify_medium(g): return 'venv_cmd' in g and g['venv_cmd']=='python -m venv myenv'
medium=Task("Store the command to create a virtual environment in variable 'venv_cmd'.", verify_medium, Level.MEDIUM, hints=["venv_cmd='python -m venv myenv'"])
def verify_hard(g): return 'activate_cmd' in g and g['activate_cmd']=='source myenv/bin/activate'
hard=Task("Store the activation command for the virtual environment in 'activate_cmd'.", verify_hard, Level.HARD, hints=["activate_cmd='source myenv/bin/activate'"])
def main(): c=input("1 Easy 2 Med 3 Hard "); tasks={"1":easy,"2":medium,"3":hard}; run_task(tasks.get(c,easy))
if __name__=="__main__": main()
