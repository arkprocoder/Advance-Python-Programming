'''
Differentiate between Global and Local Variables with sample program snippets

'''

# //global variables

# def function1(n):
#     print(n,"i have printed")
    
# n=10 #global variables
# function1(n)

# # 2.

# def function2(n):
#     n=20 #local variables 
#     print(n,"i have printed  20 because local variables precedence is taken first")
    
# n=10  #global varaible
# function2(n)

# #3.

m=10 #gobal varaible

# def function3(n):
#     m=30 #local varaible
#     n=m+n #local variables 
     
#     print(n,"i have printed  40 because local variables + local varaible gets added")
    
#  #global varaible
# n=1
# function3(n)

# # 4.

# m=30 #global variable
# def function4(n):   
#     m=m+n #local variables is not getting added with global becuz we cant change it
     
#     print(m)
    
#  #global varaible
# n=1

# function4(n)

# # 5

m=30 #global variable
def function5(n):  
    m=10 #local varaible 
    m=m+n #local variables is not getting added with global becuz we cant change it
     
    print(m,"i have printed  40 because local variables precedence is taken first and i can change the values too")
    
 #global varaible
n=1

function5(n)