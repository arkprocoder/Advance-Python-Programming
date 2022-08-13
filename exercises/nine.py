'''
9. Analyze the statement "Local Variables Cannot Be Used in the Global Scope" with an 
example program. 
'''



m=30 #global variable
def function1(n):  
    m=10 #local varaible 
    print(m,"i am searching for local varaible if its present i will print else i will look for global variable ")
    print(n,"i am global varaible which is passed in function")
    z=1000 #local varaible
     
    
  
    
 #global varaible
n=1
function1(n)
print(z, "i search for global varaible if its not present i will give error....") #this line gives error we cant access local varaibles from the function directly