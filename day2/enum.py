mylist=[[1,"rice"],[2,"dal"],[3,"harpic"]]
for index,v in mylist:
    print(index,v)\

mylist=["ark","pardhu","tejaswini","hema"]
newlist=enumerate(mylist,1)
print(newlist)
print(list(newlist))

mylist=["ark","pardhu","tejaswini","hema"]
newlist=enumerate(mylist,10)
print(newlist)
print(list(newlist))

i=1
for item in mylist:
    if i%2!=0:
        print(item)
    i+=1

# same things using enumerate
for index,item in enumerate(mylist):
    print(index,item)

for index,item in enumerate(mylist):
    if index%2==0:
        print(index,item)

    