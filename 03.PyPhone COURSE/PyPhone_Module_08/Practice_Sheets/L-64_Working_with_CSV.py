# =============================================
#  PyPhone Emperor · Module 8
#  PRACTICE L‑64  –  Working with CSV Files
#  Enterprise Coaching Engine
# =============================================
import sys, os, csv

def safe_exec(code):
    try:
        exec(code, globals())
        return None
    except Exception as e:
        return str(e)

def check_var(name, expected_type, expected_value=None):
    if name not in globals():
        return False
    val = globals()[name]
    if not isinstance(val, expected_type):
        return False
    if expected_value is not None and val != expected_value:
        return False
    return True

def task(instruction, verify_func, hint):
    print("\n" + "-"*44)
    words = instruction.split()
    line = "  📋 "
    for w in words:
        if len(line) + len(w) + 1 > 42:
            print(line)
            line = "      " + w
        else:
            if line == "  📋 ":
                line += w
            else:
                line += " " + w
    print(line)
    print("-"*44)
    while True:
        code = input("  >>> ").strip()
        if code.lower() in ("exit", "quit"):
            print("\n👋 Practice ended.")
            sys.exit(0)
        err = safe_exec(code)
        if err:
            print(f"  ❌ Python error: {err}")
            print(f"  💡 Hint: {hint}")
            continue
        try:
            if verify_func():
                print("  ✅ Correct!")
                break
            else:
                print("  ❌ Not yet. Try again.")
                print(f"  💡 Hint: {hint}")
        except Exception as e:
            print(f"  ❌ Check failed: {e}")
            print(f"  💡 Hint: {hint}")

# Create a sample CSV
SAMPLE_CSV = "sample.csv"
if not os.path.exists(SAMPLE_CSV):
    with open(SAMPLE_CSV, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Name","Age","City"])
        w.writerow(["Emperor",18,"Dhaka"])
        w.writerow(["Guest",25,"London"])

print("\n🎯 WELCOME TO L‑64 COACHING")
print("Read and write CSV files professionally.\n")

# TASK 1
task(
    "Read 'sample.csv' using csv.reader, collect all rows as a list of lists, store in `rows` (excluding header).",
    lambda: check_var('rows', list, [['Emperor','18','Dhaka'],['Guest','25','London']]),
    hint="import csv\nrows = []\nwith open('sample.csv','r') as f:\n    reader = csv.reader(f)\n    next(reader)\n    for r in reader:\n        rows.append(r)"
)

# TASK 2
task(
    "Read the same file using csv.DictReader, store all rows as a list of dicts in `dict_rows`.",
    lambda: len(globals().get('dict_rows',[])) == 2 and globals()['dict_rows'][0]['Name'] == 'Emperor',
    hint="import csv\ndict_rows = []\nwith open('sample.csv','r') as f:\n    reader = csv.DictReader(f)\n    for r in reader:\n        dict_rows.append(r)"
)

# TASK 3
task(
    "Write a new CSV 'output.csv' with header 'Product,Price' and two rows: ('Laptop','999'), ('Mouse','25'). Use csv.writer and ensure no extra blank lines.",
    lambda: os.path.exists("output.csv") and "Laptop" in open("output.csv").read(),
    hint="import csv\nwith open('output.csv','w',newline='') as f:\n    w = csv.writer(f)\n    w.writerow(['Product','Price'])\n    w.writerow(['Laptop','999'])\n    w.writerow(['Mouse','25'])"
)

# TASK 4
task(
    "Write a dictionary‑based CSV 'users.csv' with fields 'Name,Age'. Write one row: {'Name':'Emperor','Age':18}. Use csv.DictWriter with writeheader().",
    lambda: os.path.exists("users.csv") and "Emperor" in open("users.csv").read(),
    hint="import csv\nwith open('users.csv','w',newline='') as f:\n    w = csv.DictWriter(f, fieldnames=['Name','Age'])\n    w.writeheader()\n    w.writerow({'Name':'Emperor','Age':18})"
)

print("\n" + "="*44)
print("🏆 L‑64 complete – CSV handling")
print("is now your data exchange tool.")
print("="*44)