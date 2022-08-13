items=[1,2,3,4]
a=list(map((lambda x:x**3),items))
print(a)
print(type(a))

def square(a):
    return a*a

def cube(a):
    return a*a*a

def circle(a):
    return 3.14*a*a

func=[square,cube,circle]
num=[1,2,3,4,5]

for i in num:
    a=list(map((lambda x:x(i)),func))
    print(a)
