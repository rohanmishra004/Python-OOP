# Python OOP
# methods - functions assocaited with class

class Employee:
    num_of_emps = 0
    # Class Variable - when we access class varible we access them through class itself or an instance of class
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
        Employee.num_of_emps += 1

    # Method - Functions inside class which are attached to an object, Each method inside class , by default takes instance as the first argument

    def fullName(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay*Employee.raise_amt)

    # Class Method - here we receive class as the first argument instead of the instance

    @classmethod
    def set_raise_amt(cls, amt):
        cls.raise_amt = amt


        # This is an instance of class and we can create multiple instance of class
        # This way is much more simpler and clearer to declare varibles
emp1 = Employee("Corey", "Schafer", 50000)

emp2 = Employee("Test", "User", 45000)

# print(Employee.fullName(emp1))
# print(emp2.fullName())
# # print(emp1)
# print(emp2)

# These instances are different and are stored in seperate place in memory


# INSTANCE VARIABLES - Contain data that is unique to each instance of class

# This process of writing each instance seperately is very tedious, so we directly declare it within the class


# CLASS VARIABLES - That are shared amoung all instance of class, they are same for all instance

print(Employee.num_of_emps)
# This automatically takes Employee Class as the first argument and 1.05 is the second argument
Employee.set_raise_amt(1.05)
print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
