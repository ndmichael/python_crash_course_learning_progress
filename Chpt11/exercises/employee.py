class Employee:
    def __init__(self, fname, lname, annual_salary) -> None:
        self.first_name = fname
        self.last_name = lname
        self.annual_salary = annual_salary

    def give_raise(self, bonus=5000):
        '''Give raise'''
        self.annual_salary += bonus