name = "Shahnawaz"

# Slice from index 3 to 5 (6 is excluded)
nameshort = name[3:6]
print(nameshort)  # Output: "hna"

# Get the last character using negative index
character1 = name[-1]
print(character1)  # Output: "z"

print(name[:4]) # print 0-4 excluding 4
print(name[-4:]) # print -4 to -1 

# end value is not available means -1
# starting value not available means 0
print(name[1:]) # it means from 1 to end
print(name[1:7:2])
#in above firstly we extract string from 1-7 and then start from 1 and make it our output part then skip 2 digits and then after skipping next digit wil also include in input and repeating till end index means 7


# We are slicing the string with three parts:

# start = 1 → start from index 1

# end = 7 → go up to but not including index 7

# step = 2 → take every second character (skip one each time)

# This means:

# Start at index 1 ('h')

# Move forward in steps of 2:

# index 1 → 'h' 

# index 3 → 'h' 

# index 5 → 'a' 

# index 7 → reached the limit, stop