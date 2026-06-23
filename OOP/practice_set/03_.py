class Complex:
    def __init__(self,r,i):
        self.i=i
        self.r=r

    def __add__(self,c2):
        return(self.r + c2.r,self.r+c2.r)
    


c1=Complex(2,4)
c2=Complex(5,4)

print(c1 + c2)
