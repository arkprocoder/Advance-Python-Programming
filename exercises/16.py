'''
16.

Write a Python program to Determine Whether the Given String Is a Palindrome or Not
'''

n=input("Enter the number/string to check palindrome or not \n")
if(str(n)==str(n)[::-1]):
 print(f"{n} is palindrome")
else:
 print(f"{n} is not palindrome")
