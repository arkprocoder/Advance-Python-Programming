import time

def ria(python_batch_g):
    
    def python_batch():
        print("Starting")
        time.sleep(3)
        print("Pardhu is come first for class")
        python_batch_g()
        print("Final line will print after 5 second")
        time.sleep(5)
        print("Venkatesh comes last")
        
    return python_batch

@ria
def python_batch_g():
    print("Hema & Tejaswini comes second")

python_batch_g()

def sums(deco):
    a=5
    b=10
    print(f"sum is {a+b}")
    deco()
    print("i amoutside a decorator function")
    
    return deco

@sums
def deco():
    print("i  am a decorator function")

deco()