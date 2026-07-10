import sys
from models import add_contact, list_contacts, search_contacts, update_phone, delete_contact

def print_usage():
    print("Usage:")
    print("  python main.py add <name> <phone> [email] [group]")
    print("  python main.py list")
    print("  python main.py search <query>")
    print("  python main.py update <id> <new_phone>")
    print("  python main.py delete <id>")

def main():
    if len(sys.argv) < 2:
        print_usage()
        return

    command = sys.argv[1].lower()

    if command == "add":
        if len(sys.argv) < 4:
            print("Missing arguments: name and phone required.")
            return
        name = sys.argv[2]
        phone = sys.argv[3]
        email = sys.argv[4] if len(sys.argv) > 4 else None
        group = sys.argv[5] if len(sys.argv) > 5 else "General"
        add_contact(name, phone, email, group)
        print(f"Contact '{name}' added.")

    elif command == "list":
        contacts = list_contacts()
        if not contacts:
            print("No contacts found.")
            return
        for c in contacts:
            print(f"[{c['id']}] {c['name']} - {c['phone']} ({c['group_name']})")

    elif command == "search":
        if len(sys.argv) < 3:
            print("Missing search query.")
            return
        query = sys.argv[2]
        results = search_contacts(query)
        if not results:
            print("No matching contacts.")
            return
        for c in results:
            print(f"[{c['id']}] {c['name']} - {c['phone']} ({c['group_name']})")

    elif command == "update":
        if len(sys.argv) < 4:
            print("Missing arguments: id and new phone required.")
            return
        cid = int(sys.argv[2])
        new_phone = sys.argv[3]
        success = update_phone(cid, new_phone)
        if success:
            print(f"Contact {cid} updated.")
        else:
            print(f"Contact {cid} not found.")

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Missing argument: id required.")
            return
        cid = int(sys.argv[2])
        success = delete_contact(cid)
        if success:
            print(f"Contact {cid} deleted.")
        else:
            print(f"Contact {cid} not found.")

    else:
        print(f"Unknown command: {command}")
        print_usage()

if __name__ == "__main__":
    main()