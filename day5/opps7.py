class Besties:
    stars=5
    def __init__(self,name,age,look,height,hobby):
        self.name=name
        self.age=age
        self.look=look
        self.height=height
        self.hobby=hobby

    def bestieDetails(self):
        return f"MY bestie name is {self.name}\nAge is {self.age}\nLook is {self.look}\nHeight is {self.height}\nHobbies are {self.hobby}\nNo of stars {self.stars}"


class CloseFriends(Besties):

    # stars="Infinity"
    def __init__(self,name,age,look,height,hobby,likes):
        self.name=name
        self.age=age
        self.look=look
        self.height=height
        self.hobby=hobby
        self.likes=likes

    def closeFriendDetails(self):
        return f"MY Close friend name is {self.name}\nAge is {self.age}\nLook is {self.look}\nHeight is {self.height}\nHobbies are {self.hobby}\nNo of stars {self.stars}\nLikes {self.likes}\n"
    def bestieDetails(self):
        
        return f"MY bestie name is {self.name}\nAge is {self.age}\nLook is {self.look}\nHeight is {self.height}\nHobbies are {self.hobby}\nNo of stars {self.stars}"
Aadi=Besties("Aadithyaa",21,"Cool","Medium","Eating")
print(Aadi.bestieDetails())

# print(Aadi.closeFriendDetails())
# we cant access the child classes method in parent class


Am=CloseFriends("Amrutha",21,"Preety","Medium short",["Cooking","Singing"],"Pastry")

print(Am.bestieDetails())
print("\n")
print("____________________________________")
print(Am.closeFriendDetails())