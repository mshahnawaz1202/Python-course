# a=(3,4,6,7,"Shahnawaz",False,12.2)
# print(type(a))
# print(a)
# for a tuple consiting of one element
# a=(1,)  comma will tell that it is tuple otherwise it will become int

# -----------------------------Tuple Methods-------------------------------------------------------------------
# a=(3,4,6,7,"Shahnawaz",False,12.2,7)
# print(a.count(7)) # count number of value in a tuple

t = (5, 2, 9, 2, 7, 2, 1)

print("Original Tuple :", t)

# Tuple methods
print("Count of 2 :", t.count(2))
print("Index of 9 :", t.index(9))



print("Length :", len(t))
print("Max value :", max(t))
print("Min value :", min(t))
print("Sum :", sum(t))
print("Sorted :", sorted(t))  # Returns a list

# Type conversion
l = [10, 20, 30]
print("List to tuple :", tuple(l))

# Tuple operations
print("Concatenation :", t + (100, 200))
print("Repetition :", t * 2)

# Indexing and slicing
print("Element at index 0 :", t[0])
print("Slice from 2 to 5 :", t[2:5])

# Membership
print("Is 7 in tuple? :", 7 in t)
print("Is 100 in tuple? :", 100 in t)






















