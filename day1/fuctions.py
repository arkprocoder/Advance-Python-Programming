# 1)factorial ofnumber
num=int(input("Enter number :\n"))
factorial=1
if num<0:
    print("factorial does not exits")
elif num==0:
    print("factorial of zero is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print(f"the fact of {num} is {factorial}")   

def function_name(arg):
    # body of fuction

    pass



def greet(str,gender):
    print(f"hello how are you {str} {gender}")

greet("ANEES",gender="male")
greet("ANEES","male")

def calculation(a,b):
    return a+b,a-b

addition,substr=calculation(50,30)
# print(type())
print(f"add of two num {addition}")
print(f"sub of two num {substr}")

def showEmployee(name,sal=10000):
    print(f"name is {name} and salary is {sal}")


showEmployee("ark")
showEmployee("ark",5000)

def outerFun(a,b):
    print("step 1 ")
    def innerFun(a,b):
        print("step-3")
        return a+b
    print("step 2 ")   
    add=innerFun(a,b)
    print("step-4")
    print(f"Inner function returned this value {add}")
    return add+5

result=outerFun(5,10)
print(result)