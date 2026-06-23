class Employee:
    
    lanaguage="Python"
    salary=1200000
    # constructor
    # or also known as dunder method that automatically calls when an object is created
    def __init__(self,name,language,salary):
        self.name=name
        self.salary=salary
        self.lanaguage=language
        print("I am creating an object")
    # for every method we have to give a self either we use or not we can also give some other name 
    def getinfo(self):
        print(f"The language is {self.lanaguage} and salary is {self.salary}")

    def greet(self):
        print("Good morning.")

    # if we dont want to give self obj1 to a function/method we mark it as static 
    @staticmethod
    def greetNoon():
        print("Good Afternoon")

# ---------------------------------------------------------------------------------------------------------
obj=Employee("M.Shah nawaz","C++",1300000)
#  obj.name="Shahnawaz"
print(obj.name,obj.lanaguage,obj.salary)

# obj1=Employee()
# obj1.name="Shahnawaz"
# print(obj1.name,obj1.lanaguage,obj1.salary)

