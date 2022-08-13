'''
17.
Write a Python program that accepts a sentence and find the number of words, digits, 
uppercase letters and lowercase letters. 

'''



sentence=input("Enter the Sentence:\n")
count_word=sentence.count(" ")
print("Number of words in a sentence is ",count_word+1)

digits=0
uppercase=0
lowercase=0
for c in sentence:
    if c.isdigit():
        digits = digits + 1  
    elif(c== c.upper() and c!=" "):
        uppercase+=1
    elif(c==c.lower() and c!=" "):
        lowercase+=1
    else:
        pass


uppercase=uppercase
print("digits",digits)
print("uppercase",uppercase)
print("lowercase",lowercase)
