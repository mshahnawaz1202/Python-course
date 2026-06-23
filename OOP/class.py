class Employee:
    
    lanaguage="Python"
    salary=1200000



    # for every method we have to give a self either we use or not we can also give some other name 
    def getinfo(self):
        print(f"The language is {self.lanaguage} and salary is {self.salary}")

    def greet(self):
        print("Good morning.")

    # if we dont want to give self obj to a function/method we mark it as static 
    @staticmethod
    def greetNoon():
        print("Good Afternoon")

# ---------------------------------------------------------------------------------------------------------
obj=Employee()
obj.name="Shahnawaz"
# print(obj.name,obj.lanaguage,obj.salary)

# here name is object/instance attribute and salary & langauage is class attributes
# instance attributes take preference over class attribute


obj.getinfo()
Employee.getinfo(obj)  
# both do same work

obj.greet()

obj.greetNoon()
