def max(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c
a=int(input("ENTER 1ST NUMBER:"))
b=int(input("ENTER 2ND NUMBER:"))
c=int(input("ENTER 3RD NUMBER:"))

print(max(a,b,c))
