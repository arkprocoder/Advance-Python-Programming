# Super() & Overiding Methods
class A:
    messge="this is class A message"
    def __init__(self):
        self.title="Class A Title"
        self.instance="Class A Instance"

class B(A):
    messge="this is class B message"
    def __init__(self):
        # pass
        self.title="Class B Title"
        self.instance="Class B Instance"
        super().__init__()
        

a=A()
b=B()
# print(a.messge,a.instance,a.title)
print(b.messge,b.instance,b.title)
    