import sys, os
sys.path.append("../..")
from practice_engine import Task, Level, run_sequence

MODULE_DIR = os.path.dirname(__file__)

easy1 = Task(
    description=(
        "🌐  Import requests\n\n"
        "Import the requests module and print 'requests ready'.\n\n"
        "Expected output: requests ready"
    ),
    expected_output="requests ready",
    level=Level.EASY,
    hints=["import requests", "print('requests ready')"]
)

easy2 = Task(
    description=(
        "📡  GET Request Status Code\n\n"
        "Send a GET request to https://httpbin.org/status/200 and print its status code.\n\n"
        "Expected output: 200"
    ),
    expected_output="200",
    level=Level.EASY,
    hints=["import requests", "r = requests.get('https://httpbin.org/status/200')", "print(r.status_code)"]
)

medium1 = Task(
    description=(
        "📊  GET JSON Response\n\n"
        "Send a GET request to https://httpbin.org/json, parse the JSON response,\n"
        "and print the title from the slideshow (it's 'Sample Slide Show').\n\n"
        "Expected output: Sample Slide Show"
    ),
    expected_output="Sample Slide Show",
    level=Level.MEDIUM,
    hints=["import requests", "r = requests.get('https://httpbin.org/json')", "data = r.json()", "print(data['slideshow']['title'])"]
)

medium2 = Task(
    description=(
        "📬  POST Request with JSON\n\n"
        "Send a POST request to https://httpbin.org/post with json={'name':'Emperor'}.\n"
        "Print the JSON response's 'json' field.\n\n"
        "Expected output: {'name': 'Emperor'}"
    ),
    expected_output="{'name': 'Emperor'}",
    level=Level.MEDIUM,
    hints=["import requests", "r = requests.post('https://httpbin.org/post', json={'name':'Emperor'})", "print(r.json()['json'])"]
)

hard1 = Task(
    description=(
        "🛡️  Handle Request Error\n\n"
        "Try to send a GET request to an invalid URL (https://invalid.example.com).\n"
        "Catch the exception and print 'Connection failed'.\n\n"
        "Expected output: Connection failed"
    ),
    expected_output="Connection failed",
    level=Level.HARD,
    hints=["import requests", "try:", "    requests.get('https://invalid.example.com', timeout=3)", "except:", "    print('Connection failed')"]
)

hard2 = Task(
    description=(
        "📋  Send Headers\n\n"
        "Send a GET request to https://httpbin.org/headers with a custom header\n"
        "'X-Emperor': 'PyPhone'. Print the value of that header from the response JSON.\n\n"
        "Expected output: PyPhone"
    ),
    expected_output="PyPhone",
    level=Level.HARD,
    hints=["import requests", "headers = {'X-Emperor': 'PyPhone'}", "r = requests.get('https://httpbin.org/headers', headers=headers)", "print(r.json()['headers']['X-Emperor'])"]
)

if __name__=="__main__":
    run_sequence([easy1, easy2, medium1, medium2, hard1, hard2],
                 save_path=MODULE_DIR,
                 progress_name=".progress_L51.json")
