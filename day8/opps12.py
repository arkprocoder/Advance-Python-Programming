#  Operator Overloading & Dunder Methods
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole,num):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.num = num

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.num / other.num


    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    # def __str__(self):
    #     return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

emp1 =Employee("ARKPROCODER", 20, "DEVELOPER",10)
emp2 =Employee("ROHAN",10, "DESIGNER",2)
print(emp1)
print(repr(emp2))
print(str(emp1))
print(emp1+emp2)
print(emp1/emp2)
print(repr(emp1))
print(emp2)
