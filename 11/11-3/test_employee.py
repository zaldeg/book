import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.teacher = Employee('Elena', 'Mixailovna', 14000)

    def test_give_default_raise(self):
        self.teacher.give_raise()
        self.assertEqual(self.teacher.annual_salary, 19000)

    def test_give_custom_raise(self):
        self.teacher.give_raise(7000)
        self.assertEqual(self.teacher.annual_salary, 21000)

unittest.main()