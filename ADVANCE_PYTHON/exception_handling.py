# try:
#     # a=int(input("Enter a Number : "))
#     # print(a)

# except Exception as e:
#     print(e)

# -------------------------------------------------------------------------------
a=int(input("Enter Number : "))
b=int(input("Enter 2nd Number : "))

if(b==0):
    raise ZeroDivisionError("Number can't be divided b zero")
else:
    print(f"The division of {a} / {b} is  {a/b}")