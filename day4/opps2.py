class Friends:
    stars=5
    
    
tej=Friends()
hema=Friends()
# two object for class Friends is created

tej.name="Tejaswini"
tej.gender="Female"
tej.age=22
tej.salary=5000
tej.stars=10

hema.name="Hema"
hema.gender="Female"
hema.age=22

print(f"this is a classstars {Friends.stars}")
print(f"this is tejaswini stars {tej.stars}")
print(f"this is hema stars {hema.stars}")
print(hema.__dict__)
tej.stars="10"
print(f"this is tejaswini stars {tej.stars}")
print(tej.__dict__)
print(Friends.__dict__)

