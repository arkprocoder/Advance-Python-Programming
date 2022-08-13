# multiple Inheritence

class Bestie:
    stars=10
    def __init__(self,bname,bage,blook,bheight,bhobby):
        self.name=bname
        self.age=bage
        self.look=blook
        self.height=bheight
        self.hobby=bhobby

    def bestieDetails(self):
        return f"MY bestie name is {self.name}\nAge is {self.age}\nLook is {self.look}\nHeight is {self.height}\nHobbies are {self.hobby}\nNo of stars {self.stars}" 
   

class Memories:
    place="Bangalore Karnataka"

    def __init__(self,placename,items,taste):
        self.placename=placename
        self.items=items
        self.taste=taste

    def printMemories(self):
        return f"\nWe went to {self.place}\nResturant name is {self.placename}\nwe ate {self.items}\nthe taste as {self.taste}" 

    def message(self,name):
        return f"hello {name}"

class Racing(Bestie,Memories):
# class Racing(Memories,Bestie):
    place="NS HIGHWAY"
    def Racing(self):
        return f"\n\nWhile Coming back we has a racing at {self.place}"

rohan=Bestie("Rohan",25,"awesome","tall",["sleeping"])
rohan_memories=Memories("Corner House","Desert Ice Cream","Awesome")
# main class object below
rohan_race=Racing("Rohan",25,"awesome","tall",["sleeping,dancing"])
# rohan_race=Racing("Corner House","Desert Ice Cream","Awesome")
# print("_______________")
# print(rohan.bestieDetails())
# print("_______________")
# print(rohan_memories.printMemories())
print("_______________")
print(rohan_race.bestieDetails())

print("_______________")
print(rohan_race.message("anees"))

print("_______________")
print(rohan_race.Racing())

