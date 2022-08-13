'''
4.
Define a Python function with suitable parameters to generate first N Fibonacci numbers. 
The first two Fibonacci numbers are 0 and 1 and the Fibonacci sequence is defined as a 
function F as Fn = Fn-1 + Fn-2. Write a Python program which accepts a value for N 
(where N >0) as input and pass this value to the function. Display suitable error message 
if the condition for input value is not followed

'''

def fabonacci(n):
    num1=0
    num2=1
    count=0
    while(count<n):
        print(num1,end=" ")
        temp=num1+num2
        num1=num2
        num2=temp
        count+=1



n=int(input("Enter the Fibonacci number: \n "))

if(n>=0):
    fabonacci(n)
else:
    print("Invalid Input enter the numbers")