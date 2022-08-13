# Multilevel Inheritance
class FirstYear:
    friends1=["Aishwarya","Harshith","Abhinand","Meghana"]
    def printbf1(self):
        print(f"{self.friends1} They were my friends in First Year")


class SecondYear(FirstYear):
    friends2=["Harshith","Aadithyaa","Meghana"]
    def printbf2(self):
        print(f"{self.friends2} They were my friends in Second Year")

class ThirdYear(SecondYear):
    friends3=["Harshith","Aadithyaa","Meghana","Amrutha"]
    def printbf3(self):
        print(f"{self.friends3} They were my friends in Third Year")

class FourthYear(ThirdYear):
    friends4=["Harshith","Aadithyaa","Meghana","Amrutha","Aneeka"]
    def printbf4(self):
        print(f"{self.friends4} They were my friends in Fourth Year")


first=FirstYear()
print(first.friends1)
print(first.printbf1())

second=SecondYear()
print(second.friends1)
print(second.printbf1())
print("\n")
print(second.friends2)
print(second.printbf2())

finalobj=FourthYear()
print(finalobj.friends1)
print(finalobj.friends2)
print(finalobj.friends3)
print(finalobj.friends4)
print(finalobj.printbf1())
print(finalobj.printbf2())
print(finalobj.printbf3())
print(finalobj.printbf4())