'''
5. List and explain the syntax of all flow control statements with example

'''

# Python provides us with 3 types of Control Statements:

# Continue
# Break
# Pass

# 1. 
print("Continue example")
for char in 'Python':

    if (char == 'y'):

        continue
    print("Current character: ", char)

# 2.
print("Break example")
for char in 'Python':

    if (char == 'h'):
        break     
    print("Current character: ", char)

#3.
print("pass example")

for char in 'Python':
    if (char == 'h'):
        pass
print("Current character: ", char)