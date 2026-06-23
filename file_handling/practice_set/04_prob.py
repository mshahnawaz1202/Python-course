word="Donkey"
with open("file_handling/practice_set/04_file.txt","r") as f:
    content=f.read()
    
newContent=content.replace(word,"####")

with open("file_handling/practice_set/04_file.txt","w") as f:
    f.write(newContent)

