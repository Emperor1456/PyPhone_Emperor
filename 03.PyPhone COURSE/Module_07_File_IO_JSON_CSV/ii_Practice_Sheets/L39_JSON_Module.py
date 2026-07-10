import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "📖  Parse JSON String\n\n"
        "Parse the JSON string '{\"key\":\"value\"}' into a dict and print it.\n\n"
        "Expected output: {'key': 'value'}"
    ),
    expected_output="{'key': 'value'}",
    level=Level.EASY,
    hints=[
        "import json",
        "data = json.loads('{\"key\":\"value\"}')",
        "print(data)"
    ]
)

easy2 = Task(
    description=(
        "✍️  Convert Dict to JSON String\n\n"
        "Convert the dict {'name':'Emperor'} to a JSON string and print it.\n\n"
        "Expected output: {\"name\": \"Emperor\"}"
    ),
    expected_output='{"name": "Emperor"}',
    level=Level.EASY,
    hints=[
        "import json",
        "json_str = json.dumps({'name':'Emperor'})",
        "print(json_str)"
    ]
)

medium1 = Task(
    description=(
        "📂  Write JSON to File\n\n"
        "Write the dict {'age':18} to a file 'data.json', then read it back and print the dict.\n\n"
        "Expected output: {'age': 18}"
    ),
    expected_output="{'age': 18}",
    level=Level.MEDIUM,
    hints=[
        "import json",
        "with open('data.json', 'w') as f:",
        "    json.dump({'age':18}, f)",
        "with open('data.json', 'r') as f:",
        "    data = json.load(f)",
        "print(data)"
    ]
)

medium2 = Task(
    description=(
        "🧰  Pretty Print JSON\n\n"
        "Write a dict {'name':'Emperor','skills':['Python','SQL']} to 'pretty.json' with indent=2.\n"
        "Then read and print its content.\n\n"
        "Expected output:\n{\n  \"name\": \"Emperor\",\n  \"skills\": [\n    \"Python\",\n    \"SQL\"\n  ]\n}"
    ),
    expected_output='{\n  "name": "Emperor",\n  "skills": [\n    "Python",\n    "SQL"\n  ]\n}',
    level=Level.MEDIUM,
    hints=[
        "import json",
        "d = {'name':'Emperor','skills':['Python','SQL']}",
        "with open('pretty.json', 'w') as f:",
        "    json.dump(d, f, indent=2)",
        "print(open('pretty.json').read().strip())"
    ]
)

hard1 = Task(
    description=(
        "🔍  Access Nested JSON\n\n"
        "Given a JSON string: '{\"user\":{\"name\":\"Emperor\",\"age\":18}}'.\n"
        "Parse it and print the value of 'name'.\n\n"
        "Expected output: Emperor"
    ),
    expected_output="Emperor",
    level=Level.HARD,
    hints=[
        "import json",
        "data = json.loads('{\"user\":{\"name\":\"Emperor\",\"age\":18}}')",
        "print(data['user']['name'])"
    ]
)

hard2 = Task(
    description=(
        "📊  JSON Array – Sum Ages\n\n"
        "Given a JSON string: '[{\"name\":\"A\",\"age\":30},{\"name\":\"B\",\"age\":25}]'.\n"
        "Parse it, sum the ages, and print the total.\n\n"
        "Expected output: 55"
    ),
    expected_output="55",
    level=Level.HARD,
    hints=[
        "import json",
        "data = json.loads('[{\"name\":\"A\",\"age\":30},{\"name\":\"B\",\"age\":25}]')",
        "total = sum(item['age'] for item in data)",
        "print(total)"
    ]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L39.json")
