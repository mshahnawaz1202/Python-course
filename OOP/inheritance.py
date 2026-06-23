class Emplyee:
    company="ITC"
    def show(self):
        print(f"The name of Employee is {self.name} and the salary is {self.salary}")


class Programmer(Emplyee):
    company="ITC InfoTech"

    def programmer(slf):
        print(f"The name is {slf.name} and the salary is {slf.salary}")


a=Emplyee()
b=Programmer()

print(a.company,b.company)