# Multiple inheritance one class has many parents

# class Emplyee:
#     company="ITC"
#     name="Shah Nawaz"
#     def show(self):
#         print(f"The name of Employee is {self.name} and the company is {self.company}")

# class Coder:
#     language="Python"
#     def showLanguage(self):
#         print(f"Your language is {self.language}")


# class Programmer(Emplyee,Coder):
#     company="ITC InfoTech"

#     def programmer(slf):
#         print(f"The name is {slf.name} and the company is {slf.company}")


# a=Emplyee()
# b=Programmer()

# # print(a.company,b.company)


# b.show()
# b.showLanguage()
# b.programmer()


# ------------------------------------ Multi-Level Inheritance------------------------------------------
# hirarchial model of classes one is child and parent at same time 
class E:
    a=1

class P(E):
    b=2

class M(P):
    c=3



o=E()
print(o.a)
o=P()
print(o.a,o.b)
o=M()
print(o.a,o.b,o.c)