# f=open("file_handling/file_read.txt")
# data=f.read()
# print(data)
# f.close()

# the same can be done using with statement and we dont use close() function 

with open("file_handling/file_read.txt") as f:
    print(f.read())


# now we dont have to close the file 


