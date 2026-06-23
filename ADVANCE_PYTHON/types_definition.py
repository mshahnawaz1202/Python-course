# telling types at initialization time
n:int =5

name : str ="Shah"

def sum(a:int,b:int) -> int :
    return(a+b)


# ---------------------------------------------------------------------------------------------
from typing import List,Union,Tuple,Dict

number:List[int]={1,2,3,4}

# Person=Tuple[int,str]=(1,"MS")

scores:Dict[str,int]={
    "shah":90,
    "ALi":91
}

# ------------------------------ Merge Dictionary --------------------------------------------------------------------
dic1={'a':1,'b':2}
dic2={'c':3,'d':4}
merge=dic1|dic2
print(merge)


# ----------------------------------------File handling new features ------------------------
# Python 3.10+ syntax
with(
    open("File1.txt") as f1,
    open("File2.txt") as f2
):
    # Do something with f1 and f2
    data1 = f1.read()
    data2 = f2.read()
    print(data1)
    print(data2)
