print("__name__ in main1.py is set to ", __name__)

def add(num1,num2):
    return num1+num2

print("the name is ",__name__)

def greet(str):
    print(f"hello {str}")


if __name__ == '__main__':
    res=add(10,20)
    print(f"the result is printing inside name and main block {res}")
    greet("anees")

