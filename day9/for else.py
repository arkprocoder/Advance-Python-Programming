mylist=["a","r","k","l"]
for i in mylist:
    print(i)
else:
    print("statement executed")
    
nonveg=["chicken","fish","mutton"]
for i in nonveg:
    if i=="tomato":
        # print(i)
        break
    # print(i)
else:
    print("item is not found")