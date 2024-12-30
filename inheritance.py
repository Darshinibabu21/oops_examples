class employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f"name: {self.name}\nage: {self.age}")

class developer(employee):  #single inheritance
    def details(self):
        print("the salary for developer is 50,000")

class tester(employee):   #hierarchical inheritance
    def work(self):
        print("work timings are 9am - 6pm")

class intern(developer):   #multilevel inheritance
    def role(self):
        print("role is app developer")

class location:
    def place(self):
        print("locations: chennai,bangalore and madurai")

class engineer(employee,location):   #multiple inheritance
    def info(self):
        print(f"{self.name} is currently working in chennai")

a=developer("ram",34)
a.display()
a.details()

b=tester("rani",25)
b.work()
b.display()

c=intern("naveen",21)
c.role()
c.details()
c.display()

d=engineer("kavya",31)
d.info()
d.display()
d.place()
