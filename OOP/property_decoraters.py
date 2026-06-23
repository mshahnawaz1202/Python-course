class Employee:
    a=1
    @classmethod # this will shows value of class attribute not instance attribute
    def show(cls):
        print(f"The class attribute value is {cls.a}")
    
    # name is not a class attribute we make it by own
    @property
    def name(self):
        return (f"First name : {self.fname}, Last name : {self.lname}")
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]



e=Employee()
e.a=45
e.name="Shah Nawaz"
print(e.name)
e.show()

