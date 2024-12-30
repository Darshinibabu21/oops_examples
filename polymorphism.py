class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")



dog = Dog()
cat = Cat()
animal=Animal()

animal.speak()
dog.speak()  
cat.speak()

#compile time polymorphism
class calc:
    def add(self,a,b=0,c=0):
        return a+b+c

c=calc() 
print(c.add(5))
print(c.add(2,77))
print(c.add(1,2,3))