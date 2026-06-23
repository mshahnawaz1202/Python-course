# str="Meri rahein tere takk han\nTujhpe hi tou mera haq ha\nIshq mera tu beshaq ha"



# f=open("file_handling/myfile.txt","w")
# f.write(str)
# f.close()
# ----------------------------------------------------------------
# f=open("file_handling/myfile.txt")
# lines=f.readlines()
# print(lines)

# line1=f.readline()
# print(line1)


# line2=f.readline()
# print(line2)


# line3=f.readline()
# print(line3)


# line=f.readline()
# while(line!=""):
#     print(line)
#     line=f.readline()



str="\nMeri rahein tere takk han\nTujhpe hi tou mera haq ha\nIshq mera tu beshaq ha"



f=open("file_handling/file_read.txt","a")
f.write(str)
f.close()