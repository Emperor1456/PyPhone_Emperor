import sys
sys.path.append("../..")
from practice_engine import Task, Level, run_task

def verify_easy(g):
    return 'product' in g and isinstance(g['product'], str) and g['product'] == 'Monitor'

easy = Task("Create a variable 'product' with the string value 'Monitor'.", verify_easy, Level.EASY,
            hints=["product = 'Monitor'"])

def verify_medium(g):
    if 'quantity' not in g or 'price' not in g or 'total' not in g:
        return False
    q = g['quantity']
    p = g['price']
    t = g['total']
    return isinstance(q, int) and q == 3 and isinstance(p, float) and p == 249.95 and isinstance(t, float) and abs(t - (3*249.95)) < 0.001

medium = Task("Create 'quantity' = 3 (int), 'price' = 249.95 (float), then 'total' = quantity * price.", verify_medium, Level.MEDIUM,
              hints=["quantity = 3", "price = 249.95", "total = quantity * price"])

def verify_hard(g):
    return 'x' in g and isinstance(g['x'], str) and g['x'] == 'hundred'

hard = Task("Write 'x = 100' then 'x = 'hundred'' to demonstrate dynamic typing.", verify_hard, Level.HARD,
            hints=["First line: x = 100", "Second line: x = 'hundred'"])

def main():
    print("Choose: 1 Easy  2 Medium  3 Hard")
    c = input("> ").strip()
    tasks = {"1": easy, "2": medium, "3": hard}
    run_task(tasks.get(c, easy))

if __name__ == "__main__": main()
