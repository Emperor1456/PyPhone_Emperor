import unittest
import os
from database import get_connection, create_table
from models import add_contact, list_contacts, search_contacts, update_phone, delete_contact

TEST_DB = "test_contacts.db"

class TestContactBook(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if os.path.exists(TEST_DB):
            os.remove(TEST_DB)
        cls.conn = get_connection(TEST_DB)
        create_table(cls.conn)

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()
        if os.path.exists(TEST_DB):
            os.remove(TEST_DB)

    def setUp(self):
        self.conn.execute("DELETE FROM contacts")
        self.conn.commit()

    def test_add_contact(self):
        add_contact("Emperor", "+8801700000000", "emperor@pyphone.com")
        contacts = list_contacts()
        self.assertEqual(len(contacts), 1)
        self.assertEqual(contacts[0]["name"], "Emperor")

    def test_list_contacts_empty(self):
        contacts = list_contacts()
        self.assertEqual(contacts, [])

    def test_search_found(self):
        add_contact("Emperor", "+8801700000000")
        add_contact("Rahim", "+8801800000000")
        results = search_contacts("Emp")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "Emperor")

    def test_search_not_found(self):
        results = search_contacts("xyz")
        self.assertEqual(results, [])

    def test_update_phone(self):
        add_contact("Emperor", "+8801700000000")
        contacts = list_contacts()
        cid = contacts[0]["id"]
        update_phone(cid, "+8801900000000")
        updated = list_contacts()[0]
        self.assertEqual(updated["phone"], "+8801900000000")

    def test_delete_contact(self):
        add_contact("Emperor", "+8801700000000")
        contacts = list_contacts()
        cid = contacts[0]["id"]
        delete_contact(cid)
        self.assertEqual(list_contacts(), [])

if __name__ == "__main__":
    unittest.main()