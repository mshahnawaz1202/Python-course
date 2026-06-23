words=["Donkey","chomu","raja"]
with open("file_handling/practice_set/04_file.txt","r") as f:
    content=f.read()
for word in words:    
    content=content.replace(word,"#"*len(word))

with open("file_handling/practice_set/04_file.txt","w") as f:
    f.write(content)




