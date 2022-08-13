class A:
    def daimonda(self):
        print("This is a DAIMOND of class A")
        
class B(A):
    def daimondb(self):
        print("This is a DAIMOND of class B")
        
class C(A):
    pass
    # def daimondc(self):
    #     print("This is a DAIMOND of class C")
        
class D(B,C):
    def daimond(self):
        print("This is a DAIMOND of class D")
        
a=A()
b=B()
c=C()
d=D()

a.daimond()
c.daimond()
b.daimond()
d.daimond()
d.daimondb()
d.daimondb()
d.daimonda()

#  Python Program to depict multiple inheritance
# when method is overridden in one of the classes
  
class Class1:
    def m(self):
        print("In Class1") 
        
class Class2(Class1):
    pass
    # def m(self):        
    #     print("In Class2")    
  
class Class3(Class1):
    def m(self):
        print("In Class3")    
       
class Class4(Class2, Class3):
    pass       
    # def m(self):
    #     print("In Class4")    
  
obj = Class4()
obj.m()