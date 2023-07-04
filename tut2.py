import datetime


class Employee:

    # Class Varables - accessible to every instance
    Num_of_emps = 0
    raise_amt = 1.04
    # Contructor Method

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{self.first}.{self.last}@gmail.com'
        Employee.Num_of_emps += 1

    def raise_pay(self):
        self.pay = self.pay*Employee.raise_amt

    def printFullName(self):
        res = f'{self.first} {self.last}'
        return res

    @classmethod
    def set_raise_amt(cls, amt):
        cls.raise_amt = amt

    # normal methods pass instance of class or self as the first argument

    # @classmethod - pass class the first argument , cls - Class of Object , can be used as alternative constructor

    # Static Method - Donot pass any method automatically, behave just like regular function

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Employee('Rohan', "Mishra", 70000)
myDate = datetime.date(2023, 7, 1)
print(Employee.is_workday(myDate))
