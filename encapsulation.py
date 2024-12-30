class employee:
    def __init__(self, name, salary,age):
        self.name = name  # Public attribute
        self._salary = salary  # Protected attribute
        self.__age= age   # private attribute

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self._salary}")

    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        if age>0:
            self.__age=age
        else:
            print("invalid age")


emp = employee("Alice", 50000,21)
print(emp.name)  
emp.set_age(10)
print(emp.get_age())
print(emp._salary)
emp.display_info()  
