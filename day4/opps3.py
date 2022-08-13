class Employee:
    company ="AIROBOTICA SERVICES PVT LTD"

    def __init__(self,emp_name,emp_salary,emp_role):
        self.name=emp_name
        self.salary=emp_salary
        self.role=emp_role
        
    def greet(self):
        
            return f"HEllo {self.name}"
        
    def EmployeDetails(self):
                
        return f"Company is {self.company}\nEmployee is {self.name}\nSalary is {self.salary}\nRole is {self.role}"

  
tejeswini=Employee("Tejaswini",50000,"Software Engineer")
hema=Employee("Hema",60000,"Hardware Engineer")
pardu=Employee("Pardhu",50000,"Engineer")
venkatesh=Employee("venkatesh",70000,"Mechanical Engineer")

print(tejeswini)
print(tejeswini.name,tejeswini.salary,tejeswini.role)
print("\n")
print(tejeswini.EmployeDetails())
print("\n")
print(tejeswini.greet())
print(hema.EmployeDetails())
print("\n")
print(pardu.EmployeDetails())
print("\n")
print(venkatesh.EmployeDetails())