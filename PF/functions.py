# def avg():
#     a= int(input("Enter a Number : "))
#     b= int(input("Enter a Number : "))
#     c= int(input("Enter a Number : "))

#     average=(a+b+c)/3

#     print(average)

# avg()
# ------------------------------------------------------------------------
# def GoodDay(name,ending):
#     # print(f"Good Day {name}")
#     print("Good Day, "+ name)
#     print(ending)
    


# GoodDay("Shahnawaz","Thank You!")
# -------------------------------------------------------------------------
# def GoodDay(name,ending):
#     # print(f"Good Day {name}")
#     # print("Good Day, "+ name)
#     # print(ending)
#     # return "Done"
#     tr=f"Good Day, {name}\n{ending}"
#     return tr
    

# a=GoodDay("Shahnawaz","Thank You!")
# print(a)

# -------------------------------------------------------------------------
# def GoodDay(name,ending="Thanks"):
#     # print(f"Good Day {name}")
#     # print("Good Day, "+ name)
#     # print(ending)
#     # return "Done"
#     print(f"Good Day, {name}\n{ending}")

    

# GoodDay("Shahnawaz")
# -------------------------------------------------------------------------

# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1)+n

# s=sum(10)
# print("Sum : ",s)
# -------------------------------------------------------------------------
def pattern(n):
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)

p=int(input("Enter a number : "))
pattern(p)
# -------------------------------------------------------------------------