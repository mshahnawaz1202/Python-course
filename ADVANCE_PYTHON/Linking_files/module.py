def myFunc():
    print("Hello World")



if(__name__=="__main__"):
    # code will not be imported and run only in that file where code is written like in this case only run in module file 
    print("We are directly running this code")
myFunc()
print(__name__)