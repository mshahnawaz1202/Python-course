class E:
    def __init__(self):
        print("--Constructor of E--")
    a=1

class P(E):
    def __init__(self):
        super().__init__()
        print("--Constructor of P--")
    b=2

class M(P):
    def __init__(self):
        super().__init__()
        print("--Constructor of M--")
    c=3



o=E()
print(o.a)
o=P()
print(o.a,o.b)
o=M()
print(o.a,o.b,o.c)