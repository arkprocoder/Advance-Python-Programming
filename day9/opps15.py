class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        self.email=f"{fname}.{lname}@gmail.com"
        
    def persondetails(self):
        return f"This person is {self.fname} {self.lname}"
    
    
    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email is not set please set using setter"
        return f"{self.fname}.{self.lname}@gmail.com"
    
    @email.setter
    def email(self,string):
        print("i am setting new property")
        names=string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]
    
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None
        
        
    
indian=Person("RCB","Supporter")    
print(indian.email)
indian.fname="rajasthan"
indian.lname="royals"
print(indian.email)
print("\n object introspection")
print(dir(indian))
print(id(indian))
print(id("anees"))

import inspect
print(inspect.getmembers(indian))
        