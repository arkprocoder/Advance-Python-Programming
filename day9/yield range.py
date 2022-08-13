for i in range(55464585553145431545454687):
    print(i)

def genNum(n):
    for i in range(n):
        yield i
seq=genNum(41464864848)
print(seq)
# for j in seq:
#     print(j)
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())

num="12345456"
itervalue=iter(num)
print(itervalue.__next__())
print(itervalue.__next__())
print(itervalue.__next__())
print(itervalue.__next__())
print(itervalue.__next__())