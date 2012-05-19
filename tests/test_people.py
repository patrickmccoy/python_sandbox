from People import People
import unittest
import uuid

class TestPeople(unittest.TestCase):
    def setUp(self):
        self.name = 'Bob Smart'
        self.person = People(self.name)
    
    def test_get_name(self):
        self.assertEqual(self.person.get_name(), self.name)

    def test_get_first_name(self):
        self.assertEqual(self.person.get_first_name(), self.name.split(' ')[0])

    def test_get_last_name(self):
        self.assertEqual(self.person.get_last_name(), self.name.split(' ')[1])

    def test_set_name(self):
        self.name = 'Jenson Button'
        self.assertEqual(self.person.set_name(self.name), self.name)
        self.assertEqual(self.person.get_first_name(), self.name.split(' ')[0])
        self.assertEqual(self.person.get_last_name(), self.name.split(' ')[1])

    def test_set_first_name(self):
        self.name = 'Felipe'
        self.assertEqual(self.person.set_first_name(self.name), self.name)
        self.assertEqual(self.person.get_first_name(), self.name)

    def test_get_uid(self):
        self.assertIsInstance(self.person.get_id(), uuid.UUID)
        self.assertIsInstance(self.person.get_id(True), str)

if __name__ == '__main__':
    unittest.main()
