'''
10. Write a Python Program to Find the Factorial of a Number
'''


# Recursion wwork flow 
# FACTORIAL(4)
# 4!
# [4 * Facto(4-1)]
# [4 *[3* Facto(2)]
# [4 *[3 * 2] Facto(1)]
# [4 *[3 * 2] * 1]

def Facto(n):
    if n==0 or n==1:
        return 1
    else:
        return n*Facto(n-1)

fact=int(input("Enter the number to find a factorial..:\n"))
result=Facto(fact)
print(f"Result of a factorial of {fact} is : {result}")