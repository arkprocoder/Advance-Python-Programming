'''
8. Analyze the effect of Exception handling in Python with an example program.
'''

num1=input("enter the first number :\n")
num2=input("enter the second number :\n")
# print(num1,num2)

# try and except

try:
    print("i am inside the try block........")
    sum=int(num1)/int(num2)
    print("i have completed the task.......")
    print("the sum of two numbers is ",sum)

except Exception as e:
    print("i am inside the catch block.........")
    print("this is the problem happpened")
    print(e)
    