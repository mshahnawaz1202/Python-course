f=open("file_handling/practice_set/poem.txt")
data=f.read()
if("twinkle" in data):
    print("Twinkle is present")
else:
    print("Twinkle is not present")
# print(data)
f.close()