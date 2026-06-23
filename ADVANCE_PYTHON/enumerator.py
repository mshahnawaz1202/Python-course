l=[23,45,66,78,96]

# index=0
# for item in l:
#     print(f"The item at index {index} is {item}")
#     index+=1

# the same thing can be done using enumerate

for index,item in enumerate(l):
    print(f"The item at index {index} is {item}")