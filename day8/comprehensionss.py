list Comprehensions

list1 = []
for a in range(10):
    if a%2==0:
        list1.append(a)
print(list1)

using list comprehension

list1 = [a for a in range(10) if a%2==0]
print(list1)

# sets

alphabets = {a for a in ["a", "a", "b", "c", "d", "d"] }
print(alphabets)

# dicts
Normaldictory = {
  0 : "name 0",
  1 : "name 1",
  2 : "name 2",
  3 : "name 3",
  4 : "name 4",
}
print(Normaldictory)

# or
dictComprehension = {i:f"name {i}" for i in range(1,1001)}
print(dictComprehension)


dict1 = {i:f"item {i}" for i in range(1, 10001) if i%100==0}
# dict1 = {i:f"Item {i}" for i in range(5)}

dict2 = {value:key for key,value in dict1.items()}
print(dict1,"\n", dict2)

dresseslist = [dress for dress in ["dress1", "dress2","dress1",
                               "dress2","dress1", "dress2"]]
dressesset = {dress for dress in ["dress1", "dress2","dress1",
                               "dress2","dress1", "dress2"]}
print(type(dresseslist))
print(type(dressesset))
print(dresseslist)
print(dressesset)


def generators(n):
    for i in range(n):
        yield i

a = generators(5)
print(a.__next__())
print(a.__next__())
print(a.__next__())

# or
gener = (i for i in range(5))
a = gener
print(a.__next__())
print(a.__next__())
print(a.__next__())

evens = (i for i in range(100) if i%2==0)
print(evens.__next__())

for item in evens:
    print(item)