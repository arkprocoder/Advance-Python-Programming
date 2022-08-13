import pickle
# writing the values inside a pkl file that is in binary mode
# cars=["audi","bmw","ferrari","suzuki","toyota"]
# file = "mycarsss.pkl"
# fileobj=open(file,'wb')
# pickle.dump(cars,fileobj)
# fileobj.close()

# read the values from pkl file
file="mycarsss.pkl"
fileobj=open(file,'rb')
mycars=pickle.load(fileobj)
print(mycars)
print(type(mycars))