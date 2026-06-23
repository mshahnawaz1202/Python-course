def generateTables(n):
    table=""
    for i in range(1,11):
        table+=f"{n} x {i} = {n*i}\n"
        with open(f"file_handling/practice_set/table/table_{n}.txt","w") as f:
            f.write(table)



for i in range(2,21):
    generateTables(i)
