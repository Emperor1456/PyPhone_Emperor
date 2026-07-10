import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from debug_engine import run_debug

BROKEN = """\
class ContactBook:
    def __init__(self):
        self.contacts = []
    def add(self, name, phone):
        self.contacts.append({"name": name, "phone": phone})
    def list_contacts(self):
        return self.contacts

app = ContactBook()
app.add("Emperor", "123")
print(app.list_contacts)"""

EXPECTED = "[{'name': 'Emperor', 'phone': '123'}]"
HINTS = [
    "list_contacts is a method, not a property.",
    "You need to call it with parentheses.",
    "Change 'app.list_contacts' to 'app.list_contacts()'."
]

if __name__ == "__main__":
    run_debug("L58: Project Architecture", BROKEN, EXPECTED, HINTS)
