class Employee:
    def __init__(self,first,last,pay):
        self.first= first
        self.last= last
        self.pay= pay
        self.email= first+'.'+last+'@abc.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)



emp1 = Employee('Birender','Singh',120000)
emp2 = Employee('Surender','Singh',150000)


print(emp1.first)
print(emp2.email)
print(emp1.fullname())

print(Employee.fullname(emp1))
print(Employee.fullname(emp2))
