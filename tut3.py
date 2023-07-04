class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{self.first}.{self.last}@gmail.com'

    def full_Name(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = self.pay*Employee.raise_amt


# INHERITANCE - Inherit from parent class
class Developer(Employee):

    raise_amt = 1.05

    # with single inheritance - using super is more maintainable, but with multiple inheritance we can use class name
    def __init__(self, first, last, pay, programming_language):
        super().__init__(first, last, pay)
        self.programming_language = programming_language


# Another subclass


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    # Add Employees

    def add_emp(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    # Remove Employeess

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    # Print Employees
    def printEmp(self):
        count = 0
        for emp in self.employees:
            count += 1
            print(f'-->{count}', emp.full_Name())


emp1 = Developer('User', "Test", 15000, 'Python')
emp2 = Developer('User2', "Test", 15000, 'Java')
emp3 = Employee('New User', "test", 20000)


manager1 = Manager("Sue", "smith", 90000, [emp1])
print(manager1.email)

manager1.add_emp(emp2)
manager1.remove_emp(emp1)
manager1.printEmp()


# print(emp1.full_Name())
# print(emp1.programming_language)
# print(emp1.email)
# print(emp2.first)
# print(help(Developer))

# There are two sub-classes in Python - isInstance or isSubClass() which tells whether a class/Object is an instance or subClass of an object or not
