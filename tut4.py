# SPECIAL METHODS -- With the help of special methods we can  modify the special behavior of these functions , example - __repr and __str__

# __repr__ - in the below example we can provide it a custom output to generate a representative state of the object

# __str__ - in the below example we can provide it generate a custome output when called on an instance

class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{self.first}.{self.last}@company.com'

    def fullName(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = self.pay*Employee.raise_amt

    def __repr__(self):
        return f'Employee({self.first} {self.last} {self.pay})'

    def __str__(self):
        return f'{self.fullName()}, {self.email}'

    def __add__(self, other):
        return self.pay+other.pay

        # There are special methods for maths
# print(1+2)  # this adds to element if values are integers
# this concatenates the two values if they are string , we can also write this code ourselves
# print('1'+'1')


emp3 = Employee('New User', "test", 20000)
emp4 = Employee('New2User', "test", 20000)
print(emp3 + emp4)
print(repr(emp3))
print(emp3)
