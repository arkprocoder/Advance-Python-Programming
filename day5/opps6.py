# a="RIA/INSTITUTE/abc"
# b=a.split("/")
# print(b)  
class Employee:
    company ="AIROBOTICA SERVICES PVT LTD"

    def __init__(self,emp_name,emp_salary,emp_role):
        self.name=emp_name
        self.salary=emp_salary
        self.role=emp_role
    
    def EmployeDetails(self):
        return f"Company is {self.company}\nEmployee is {self.name}\nSalary is {self.salary}\nRole is {self.role}"

    @classmethod
    def change_company(cls,newcompany):
        cls.company=newcompany

    @classmethod
    def message(cls,greeting):
        # context=greeting.split("-")
        # print(context)
        # return cls(context[0],context[1],context[2])
        return cls(*greeting.split("-"))

    @staticmethod
    def greet(name):
        print(f"{name}  is the Best Employee")



tejeswini=Employee("Tejaswini",50000,"Software Engineer")
hema=Employee("Hema",60000,"Hardware Engineer")
pardu=Employee("Pardhu",50000,"Engineer")
venkatesh=Employee("venkatesh",70000,"Mechanical Engineer")

print(tejeswini.EmployeDetails())
print("\n")
print("After chanage of company")
print("*********************************88")
tejeswini.change_company("RIA INSITITUE")
Employee.greet("ROHAN")
hema.greet("Hema")
venkatesh.greet("Venkatesh")
