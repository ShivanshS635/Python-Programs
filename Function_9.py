import math
def hypo(p,b):
    h=math.sqrt(p**2+b**2)
    return h
a=int(input("ENTER PERPENDICULAR:"))
b=int(input("ENTER BASE:"))
print(hypo(a,b))

