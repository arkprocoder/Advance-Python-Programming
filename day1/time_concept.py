import time

initial=time.time()
print("seconds",seconds)
print("program is in sleep mode")
time.sleep(10)
print("program is not in sleep mode")
print(time.asctime())

print(time.localtime())

j=0
while(j<50):
    print("run while loop")
    j=j+1
print("while loop ran in ",time.time()-initial,"seconds")

# for loop
initial1=time.time()
for i in range(50):
    print("this is for loop")

print("for loop ran in ",time.time()-initial1,"seconds")


def num(n):
    a=l+12
    print(a)
l=12
num(5)