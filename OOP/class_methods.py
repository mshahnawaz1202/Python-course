# class Employee:
#     a=1
#     def show(self):
#         print(f"The class attribute value is {self.a}")



# e=Employee()
# e.a=45
# e.show()

# if we want to show class attribute value in function cll not boject/instance attribute value then we use class method

class Employee:
    a=1
    @classmethod # this will shows value of class attribute not instance attribute
    def show(cls):
        print(f"The class attribute value is {cls.a}")



e=Employee()
e.a=45
e.show()
