import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test for the class Employee."""

    def setUp(self):
        """
        Create an employee for use in all test methods
        """
        self.employee = Employee('Test', 'Testerson', 30000)

    def test_give_default_raise(self):
        """Test give_raise method with default value."""
        current_salary = self.employee.salary
        self.employee.give_raise()
    
        self.assertEqual(current_salary + 5000, self.employee.salary)

    def test_give_custom_raise(self):
        """Test give_raise method with custom value."""
        custom_raise = 10000
        current_salary = self.employee.salary
        self.employee.give_raise(custom_raise)

        self.assertEqual(current_salary + custom_raise, self.employee.salary)

unittest.main()
