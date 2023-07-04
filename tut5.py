class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def full_name(self):
        return f'{self.first} {self.last}'

    # In ordet to access this email as an attribute, we can use a property decorator above this method
    @property
    def email(self):
        return f'{self.first}.{self.last}@company.com'

    # once we add the @prop decorator we can use this method as an attribute

    # @SETTERS - this can modify the
    @full_name.setter
    def full_name(self, name):
        # this will update the first and last name
        first, last = name.split(' ')
        self.first = first
        self.last = last


emp1 = Employee('NewUser', "Test", 40000)

# here email and fullname depends on the instance


emp1.first = 'Jim'  # this only updates the fullname funtion but the intial constructor will still show the email as previous one , to solve this issue in other languages we use getters and setters
# but in python we can use property decorators which help us to define a method but we can access it as a method
print(emp1.full_name)
print(emp1.email)


emp1.full_name = 'John New'
print(emp1.full_name)

# we can to this similarly to any method and we can use it a parameter
