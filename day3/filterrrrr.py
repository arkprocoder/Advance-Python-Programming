b=[1,2,3,4,5,9,8]
a=[2,5,4]
c=list(filter(lambda x: x not in a ,b))
print(c)

def greater_num(n):
    return n>3
    
result=list(filter(greater_num,b))
print(result)