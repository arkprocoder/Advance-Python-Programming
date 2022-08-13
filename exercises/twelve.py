'''
12. Define a Python function with suitable parameters to generate prime numbers between 
two integer values. Write a Python program which accepts two integer values m and n 
(note: m>0, n>0 and m < n) as inputs and pass these values to the function. Suitable error 
messages should be displayed if the conditions for input values are not followed.
EX:1 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
'''
first = int(input("Enter the first number:"))
second = int(input("Enter the Second Number:"))
for i in range(first, second):
    for j in range(2, i//2):
        if i % j == 0:
            break
    else:
        print("Prime Number", i)