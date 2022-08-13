'''
2. What are Comparison and Boolean operators? List all the Comparison and Boolean 
operators in Python and explain the use of these operators with suitable examples
'''

# Comparision Operators --> <, >, <= ,>=, ==,  !=,
# example:

get_input=int(input("Enter your age : \n"))

if(get_input<18):
    print("You cant vote go and have a cup of tea")

elif(get_input==18):

    print("If you have an voter id you can go and vote")

elif(get_input>=18 and  get_input<=100):
    print("If you have an voter id you can go and vote")

else:
    print("Get out")


# Boolean Operators --> True, False

a=True  #a=1
b=False #b=0

if(a == b):
    print(True)
else:
    print(False)
   