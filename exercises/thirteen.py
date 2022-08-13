'''
13. Differentiate between (CO2, K4)
a. Lists and Tuples
b. copy() and deepcopy()

'''


'''

Sr  Key	                     List	                               Tuple

1	Type	             List is mutable.	                       Tuple is immutable. 
 
2	Iteration	         List iteration is slower and
                          is time consuming.	                    Tuple iteration is faster.

3	Appropriate for	     List is useful for insertion              Tuple is useful for readonly    
                             and deletion operations. 

4   Memory Consumption	 List consumes more memory.                Tuples consumes less memory   

5 	Methods              List provides many in-built methods.       Tuples have less in-built methods.

6. Error prone          List operations are more error prone.       Tuples operations are safe.

'''
'''
# importing copy module
import copy
  
# initializing list 1 
li1 = [1, 2, [3,5], 4]
  
  
# using copy for shallow copy  
li2 = copy.copy(li1) 
  
# using deepcopy for deepcopy  
li3 = copy.deepcopy(li1) 

print(li1)
print(li2)
print(li3)
'''
# Python code to demonstrate copy operations
  
# importing "copy" for copy operations
import copy
  
# initializing list 1
li1 = [1, 2, [3,5], 4]
  
# using deepcopy to deep copy 
li2 = copy.deepcopy(li1)
  
# original elements of list
print ("The original elements before deep copying")
for i in range(0,len(li1)):
    print (li1[i],end=" ")
  
print("\r")
  
# adding and element to new list
li2[2][0] = 7
  
# Change is reflected in l2 
print ("The new list of elements after deep copying ")
for i in range(0,len( li1)):
    print (li2[i],end=" ")
  
print("\r")
  
# Change is NOT reflected in original list
# as it is a deep copy
print ("The original elements after deep copying")
for i in range(0,len( li1)):
    print (li1[i],end=" ")

# In the above example, the change made in the list did not effect in other lists, indicating the list is deep copied.

'''
# Python code to demonstrate copy operations

# importing "copy" for copy operations
import copy

# initializing list 1
li1 = [1, 2, [3,5], 4]

# using copy to shallow copy
li2 = copy.copy(li1)

# original elements of list
print ("The original elements before shallow copying")
for i in range(0,len(li1)):
	print (li1[i],end=" ")

print("\r")

# adding and element to new list
li2[2][0] = 7

# checking if change is reflected
print ("The original elements after shallow copying")
for i in range(0,len( li1)):
	print (li1[i],end=" ")


'''