def sod(d):
    n=d
    s=0
    while(n!=0):
        r=n%10
        s=s+r
        n=n//10
    return s
d=int(input("ENTER THE DIGIT:"))
c=sod(d)
print(c)
