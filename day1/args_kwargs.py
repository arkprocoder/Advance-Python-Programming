def funargs(normal,*args):
    print(type(args))
    print(normal)
    for i in args:
        print(i)
normal="This is normal value"
funargs(normal,"ANEES","PARDHU","KRISHNA","TEJASWENI","HEMA","Venkatesh")

def funargs(*args,normal):
    print(type(args))
    print(normal)
    for i in args:
        print(i)
normal="This is normal value"
funargs("ANEES","PARDHU","KRISHNA","TEJASWENI","HEMA","Venkatesh",normal)

def func_arg_kwarg(normal,*args, **kwargs):
    print(normal)
    print("\nnow args will prints")
    for n in args:
        print(f"Name is {n}")
    print("\nNow kwargs will print")
    for name,des in kwargs.items():
        print(f"{name} is {des}")


names=["ANEES","PARDHU","KRISHNA","TEJASWENI","HEMA","VENKATESH"]
title_ria="Python programming batch"
kw={
    "ANEES":"Developer",
    "PARDHU":"Data Scientist",
    "KRISHNA":"Tester",
    "TEJASWENI":"Programmer",
    "HEMA":"Coder",
    "VENKATESH":"Skipper",
    "ARK":"WEB DEVL"
}

func_arg_kwarg(title_ria,*names,**kw)