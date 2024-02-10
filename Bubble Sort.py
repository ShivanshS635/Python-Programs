a=int(input("ENTER SIZE OF LIST:"))
l=[]
for i in range(a):
    n=int(input("ENTER NUMBER:"))
    l.append(n)
print("UNSORTED LIST:",l)

def Sort(l):
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                t=l[j]
                l[j]=l[j+1]
                l[j+1]=t
    return l

print("SORTED LIST:",Sort(l))
