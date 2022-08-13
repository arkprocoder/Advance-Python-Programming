mylist=["pardu","tejaswini","hema"]
sep="|"
a=sep.join(mylist)
print(type(a))
print(a)

mydict={"a":1,"b":2,"c":3}
sep="_sep_"
print(sep.join(mydict))

a=[1,"ar",[1,2]]
sep=","
print(sep.join(a))