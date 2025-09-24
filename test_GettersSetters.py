import unittest
from GettersSetters import Student

class TestStudentSetAge(unittest.TestCase):
    def test_set_age_with_integer(self):
        s = Student("Test", 20)
        s.set_age(25)
        # Accessing the private variable using name mangling
        self.assertEqual(s._Student__age, 25)

    def test_set_age_with_non_integer(self):
        s = Student("Test", 20)
        with self.assertLogs() as log:
            s.set_age("twenty")
        # Age should remain unchanged
        self.assertEqual(s._Student__age, 20)

    def test_set_age_with_negative_integer(self):
        s = Student("Test", 20)
        s.set_age(-5)
        self.assertEqual(s._Student__age, -5)

if __name__ == "__main__":
    unittest.main()