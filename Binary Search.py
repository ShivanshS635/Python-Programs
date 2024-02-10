###BINARY SEARCH###

pos=0

n=int(input("ENTER NUMBER OF ELEMENTS IN A LIST:"))
l=[]
p=0
for i in range (n):
    a=int(input("Enter :"))
    l.append(a)

def Search(l,m):
    lo=0
    up=len(l)-1

    while(lo<=up):
        mid=(lo+up)//2

        if l[mid]==m:
            global pos
            pos=mid
            return True
        else:
            if l[mid]<m:
                lo=mid
            else:
                up=mid
m=int(input("ENTER NUMBER TO SEARCH:"))
if Search(l,m):
    print(m,"FOUND AT",pos)
else:
    print(m,"NOT FOUND")
