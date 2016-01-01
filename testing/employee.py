class Employee():
    """An Attempt to Model an Employee."""

    def __init__(self, first_name, last_name, salary):
        """Setup a new employee."""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = int(salary)

    def give_raise(self, amount = 5000):
        self.salary += amount

