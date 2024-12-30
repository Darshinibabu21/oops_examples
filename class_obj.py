class dog:
    sound="bark"
    def __init__(self,name,age):
        self.name=name
        self.age=age

d=dog("tommy",5)
print(f"name is {d.name} and age is {d.age}\nsound: {d.sound}")