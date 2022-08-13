try:
    pass #run the code
except Exception as e:
    pass #exceute this block when try block fails
else:
    pass #executes when try blocks has no errros and except block is not used
finally:
    pass #at any cost this block will get executed

def divide(a,b):
    try:
        print(f"Division of {a} , {b} is : {a/b}")
    # except Exception as e:
    #     print(e)
    except ZeroDivisionError as e:
        print(e)
    else:
        print("Exception has not occured")
    finally:
        print("i will execute at any cost")
    
    
# divide(10,2)
divide(10,0)