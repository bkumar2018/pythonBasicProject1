class Employee:

    num_of_emp = 0
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first= first
        self.last= last
        self.pay= pay
        self.email= first+'.'+last+'@abc.com'
        
        Employee.num_of_emp += 1
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount 

    @classmethod
    def from_string(cls, emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or  day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    raise_amount=1.10

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        #Employee.__init__(self,first,last,pay)
        self.prog_lang = prog_lang
    

class Manager(Employee):

    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)        
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--->'+ emp.fullname())





dev1 = Developer('Birender','Singh',120000,'Python')
dev2 = Developer('Surender','Singh',150000, 'Java')

print(dev1.email)
print(dev1.prog_lang)
print(dev2.email)
print(dev2.prog_lang)
# print(help(Developer))

# print(dev1.pay)
# dev1.apply_raise()
# print(dev1.pay)

mgr1 = Manager('Sue','Smith',80000,[dev1])

print(mgr1.email)
mgr1.print_emps()

mgr1.add_emp(dev2)
mgr1.print_emps()

mgr1.remove_emp(dev1)
mgr1.print_emps()


print(isinstance(mgr1,Manager))
print(isinstance(mgr1,Employee))
print(isinstance(mgr1,Developer))

print('--------------------')
print(issubclass(Developer,Employee))
print(issubclass(Manager,Employee))
print(issubclass(Manager,Developer))



